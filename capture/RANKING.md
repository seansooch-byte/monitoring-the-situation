> A guide to where to look on X, for the grabber and the editor. It must not change what goes into a capture: a capture still holds what X returned and no judgement of it.

# X "For You" algorithm: cheat sheet

Source: github.com/xai-org/x-algorithm, commit `cb45b5501423126adfc508052116c2d67c0e3fec` (Oct 9, 2026, 1:42 AM ET). The param defaults were last synced from production on 2026-10-08 (`home-mixer/params/param.rs:1`). The repo says these defaults mirror the primary production values. Live experiments can override them.

## 1. What the ranking model predicts (FACT)
Phoenix is a transformer that reads the viewer's recent engagement history and scores each candidate post separately (candidates can't attend to each other; `phoenix/README.md`). For each post it outputs the viewer's own probability of these actions (`xai-value-model/scoring.rs` `compute_weighted_score`):
- **Engagement:** like, reply, repost, quote, share, share via DM, share via copy link
- **Clicks:** post click, profile click, link open, photo expand, video open, quoted-post click
- **Attention:** video quality view, dwell, dwell time, click dwell time, video continuation, profile visit seconds
- **Author:** follow author
- **Negative:** not interested, block, mute, report, not dwelled

## 2. Weights (FACT, `home-mixer/params/param.rs`, mirrored in `vm-ranker/params.rs`)
Score = Σ weight × P(action). The weights multiply predicted probabilities, not raw counts (`param.rs` ~L287-313).

| Action | Weight | Line |
|---|---|---|
| Share via copy link | **20.0** | L358 |
| Reply | 5.0 (**+15** if mutual follow = 20) | L315, L317 |
| Quote | 5.0 | L364 |
| Share via DM | 5.0 | L352 |
| Follow author | 4.0 | L378 |
| Share | 2.0 | L350 |
| Repost | 1.0 | L328 |
| Like | 0.5 | L314 |
| Click dwell time | 0.4 | L396 |
| Click | 0.3 | L341 |
| Open link | 0.2 | L342 |
| Video open / photo expand / dwell / quoted click | 0.07 / 0.05 / 0.05 / 0.05 | L336, L330, L363, L366 |
| Post unexplored (in-network only) | 0.015 (0.02 in vm-ranker) | L384 |
| Dwell time | 0.004 | L390 |
| Profile click, VQV, quoted VQV | 0.0 | L344, L349, L372 |
| **Report** | **−234** | L420 |
| Mute | −58.8 | L415 |
| Not interested | −47.52 | L403 |
| Block | −31.2 | L409 |
| Not dwelled | −0.02 | L422 |

A negative total gets squashed below a small offset of 0.001 (`xai-value-model/weights.rs:4`, `scoring.rs` `offset_score`). The code comment says a report's baseline probability is more than 1000× lower than a like's, which is why its weight is so large.

## 3. Sourcing and in-network vs out-of-network (FACT)
- **In-network:** Thunder, up to 1,200 posts (`param.rs:24`).
- **Out-of-network:**
  - Phoenix retrieval, up to 1,000 (`param.rs:5`)
  - SimClusters, max age 48 h
  - Popular posts, up to 500 (`param.rs:950`). This is a shared list of original posts (no replies or reposts) from the top-follower authors who posted in the last 7 days. It's ranked by views ÷ age, with an 8 h half-life over a 24 h window and at most 5 posts per author (`home-mixer/util/popular_posts.rs`, `popular_posts_job.rs`).
- All sources are ranked by the same model.
- **Out-of-network penalty:** score × **0.75** (`vm-ranker/params.rs:206`), or × 0.5 on topic requests (L200). The same 0.75 also applies to replies and reposts from accounts the viewer follows (L182, `scoring.rs` `oon_applies`).

## 4. Diversity, recency and filters (FACT)
- **Author diversity:** the k-th post by the same author is multiplied by 0.75·0.5^k + 0.25, which gives 1, 0.625, 0.44, … down to a floor of 0.25 (`vm-ranker/params.rs:164-180`, `scoring.rs` `diversity_multiplier`).
- **DPP reranker:** reorders the top 150 to trade score against embedding similarity, with θ = 0.65 (`vm-ranker/params.rs:235-240`, `vm-ranker/dpp.rs`).
- **Recency:** a hard 48 h cutoff (`home-mixer/params/config.rs:40` `MAX_POST_AGE`).
- **New-author boost:** applies to authors under 200 impressions and ≤50k followers, on posts ≤2 h old. These are lifted toward slots 15–16, with Thompson sampling (`param.rs:478-552`, `scorers/author_cold_start.rs`).
- **Filters** (`home-mixer/candidate_pipeline/phoenix_candidate_pipeline.rs:396-423`):
  - Out-of-network reposts and replies are dropped (`filters/oon_retweet_reply_filter.rs`; `EnablePhoenixOonReplies` = false).
  - Also removed: duplicates, already-seen or served posts, blocked or muted authors, muted keywords, and the Brazil election filter.
  - After ranking, visibility filtering drops posts by label. A post is also dropped if its parent or quoted post was dropped.
  - The like-count-based `FavHoldoutFilter` exists but is off (`param.rs:884`).

## 5. What this implies (all INFERENCE)
- **INFERENCE:** Distribution rewards conversation and private sharing (copy link 20, reply 5–20, quote 5, DM 5) far more than likes (0.5). A post that people quote, argue with, or pass around in DMs can spread further than one with more likes.
- **INFERENCE:** Viral reach outside a following comes mostly from Phoenix retrieval and from the popular-posts list. That list is built on views per hour from big accounts, so large-account originals get an extra lane.
- **INFERENCE:** The 48 h cutoff, the 8 h half-life, and the 0.75 out-of-network penalty mean For You reach drops off fast. Stories that last longer are carried by new posts, quotes, and replies, not by the original post.
- **INFERENCE:** Rage-bait gets reach from replies and quotes but has to beat its predicted report, mute, and not-interested costs. Because scoring is personalized, a post can be huge for one audience and invisible to another.
- **INFERENCE for the Monitoring briefings:**
  - Judge virality by quote count, reply count, and views per hour within the first 24 h, not by likes.
  - Quote-heavy posts are the ones the algorithm is pushing.
  - Treat a post older than 48 h as no longer spreading through For You.
  - Note that the repo has no view-based "trending" signal beyond the popular-posts list.
  - The author-diversity penalty means one account rarely dominates a feed. Many accounts posting the same story is a better sign of a real wave.

Not in the repo: trained model weights, Grox prompts, some botmaker rules, and live experiment overrides (`README.md` "What's not in this repo?").
