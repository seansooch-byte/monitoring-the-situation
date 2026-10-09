# Sensor accounts

Accounts that tend to post or repost what is about to be everywhere. Each group is read in one
`search_posts_all` call: `(from:a OR from:b ...) -is:reply`, newest first, 25 results. Follow every
reference (`quoted`, `retweeted`, `media_source`) to the origin and capture the origin as well as
the sensor's copy.

Columns: handle; desks served; own = mostly posts its own material, repost = mostly reposts or
re-uploads other people's material, mixed = both; why.
"Seen" means the account has a post in capture 2026-10-09T0552Z or 0615Z. "Untested" means it is
chosen from what the account is known for and has not yet produced a captured post; drop it if two
weeks of runs show nothing.

The first sensor probe (30 accounts, 2026-10-09) showed that `-is:reply` is required and that
miraghini, _papawere and Spazzzie mostly reply, so they are left out.

## news (politics, world, defense, justice, disaster)

| Handle | Desks | Own or repost | Why |
|---|---|---|---|
| atrupar | politics, defense | own | Seen 4 times; clips officials on camera within minutes. |
| EricLDaugh | politics, disaster | repost | Seen twice; fast reposts of political clips. |
| LeadingReport | politics | repost | Seen; headline aggregator, early on breaking items. |
| visegrad24 | world | repost | Untested; high reach world news aggregator. |
| Osint613 | world, defense | own | Only account in the probe with original news. |
| sethharpesq | defense | own | Seen twice; veteran commentary that travels. |
| nfergus | world | own | Seen; long posts on world affairs. |
| rawsalerts | justice, disaster, world | repost | Seen; breaking alerts with video. |
| streetmediatv | justice | repost | Seen twice; police and street video, usually own uploads without media_source. |
| WFLA | disaster | own | Seen; local station with storm video. |
| JimCantore | disaster | own | Seen; storm coverage that spreads during events. |
| BrandonCopicWx | disaster | own | Seen; forecast maps during storms. |
| BBCBreaking | world, disaster | own | Seen; first headline for many world stories. |
| SkyNews | world | own | Seen; video of world and UK events. |
| Reuters | world, politics | own | Seen in the first capture; wire headlines. |
| MeidasTouch | politics | mixed | Seen; political clips with large repost counts. |
| CollinRugg | politics, justice | repost | Untested in captures; frequent viral clip reposts. |
| Gerashchenko_en | world, defense | own | Seen; subtitled Ukraine clips, 462k views in this run. |

## money (markets, business, crypto)

| Handle | Desks | Own or repost | Why |
|---|---|---|---|
| unusual_whales | markets | repost | Seen; market headlines that spread fast. |
| TheStalwart | markets, ai | own | Seen 3 times; markets commentary. |
| biancoresearch | markets | own | Seen; rates and bond charts. |
| markgurman | business, tech | own | Seen; Apple company news first. |
| MacRumors | business, tech | own | Seen twice; Apple news. |
| Variety | business | own | Seen; media business news. |
| DiscussingFilm | business, entertainment | repost | Seen; media deal and studio news. |
| WatcherGuru | crypto, markets | repost | Seen; one-line headlines that get reposted widely. |
| BitcoinMagazine | crypto | own | Seen twice. |
| Cointelegraph | crypto, markets | own | Seen. |
| cryptorover | crypto, markets | repost | Seen twice. |
| AshCrypto | crypto, markets | repost | Seen twice. |
| BullTheoryio | markets | repost | Seen. |
| scottmelker | crypto, markets | own | Seen. |
| BitcoinArchive | crypto | repost | Seen. |
| GrantCardone | crypto, business | own | Seen twice. |

## science (ai, tech, science, medicine)

| Handle | Desks | Own or repost | Why |
|---|---|---|---|
| AndrewCurran_ | ai, tech, science | own | Seen twice; early on AI lab news. |
| kimmonismus | ai, tech | repost | Seen; AI news aggregation. |
| jukan05 | tech | own | Seen twice; chip and hardware leaks. |
| Hesamation | ai, tech | repost | Seen. |
| marclou | ai | own | Seen. |
| ryancarson | ai | own | Seen. |
| NASAAdmin | science | own | Seen twice. |
| NASA | science | own | Untested; launches and mission video. |
| SpaceX | science | own | Untested; launch video that gets reposted. |
| elonmusk | science, tech, ai | mixed | Seen twice; pinned watch post; very high reach. |
| sciencegirl | science, offbeat | repost | Untested; science clips with large reach. |
| ChildrensHD | medicine | own | Seen in the first capture. |
| SecKennedy | medicine | own | Seen in the first capture; health agency announcements. |
| CDCgov | medicine | own | Untested; official health announcements. |

## culture (entertainment, music, gaming, ideas)

| Handle | Desks | Own or repost | Why |
|---|---|---|---|
| PopBase | entertainment, music | repost | In the probe list; pop culture headlines. |
| PopCrave | entertainment, music | repost | In the probe list; pop culture headlines. |
| CultureCrave | entertainment, business | repost | Seen; film and TV news. |
| DiscussingFilm | entertainment | repost | Seen; film news. |
| superTV247 | entertainment | repost | Seen 3 times. |
| scottygb | entertainment | own | Seen twice. |
| IGN | entertainment, gaming | own | Seen; film and game reviews. |
| Dexerto | gaming, internet | repost | In the probe list; gaming and streamer news. |
| flolikethis | music | own | Seen twice. |
| chaovampz | music | own | Seen; k-pop fan posts with reach. |
| HYBE_LABELS | music | own | Untested; k-pop releases. |
| billboard | music | own | Untested; charts. |
| Wuthering_Waves | gaming | own | Untested; source of the fan wave seen in both captures. |
| Nintendo | gaming | own | Untested; announcements. |
| PlayStation | gaming | own | Untested; announcements. |
| wahalaondirocks | ideas | repost | Seen; history posts with 53k likes in this run. |

## sports (sports)

| Handle | Desks | Own or repost | Why |
|---|---|---|---|
| NFL | sports | own | Seen in the first capture. |
| NFLMemes | sports | repost | Seen 3 times; game night reactions. |
| RapSheet | sports | own | Seen twice; NFL news first. |
| AdamSchefter | sports | own | Untested; NFL news first. |
| ShamsCharania | sports | own | Untested; NBA news first. |
| MLB | sports | own | Seen twice. |
| SportsCenter | sports | own | Seen. |
| BleacherReport | sports | own | Seen; game clips with media_source. |
| espnW | sports | own | Seen. |
| stephenasmith | sports | own | Seen; reaction posts with high reach. |
| barstoolsports | sports | repost | Seen in the first capture; reposts clips with media_source. |
| FearedBuck | sports, internet | repost | Seen; sports gossip that travels. |
| TotalProSports | sports | repost | Seen. |
| Underdog | sports | own | Seen. |
| FabrizioRomano | sports | own | Untested; soccer transfers. |

## online (internet, life, offbeat)

| Handle | Desks | Own or repost | Why |
|---|---|---|---|
| SinClipd | internet | repost | Seen twice; streamer clips with media_source. |
| Clipdyz | internet | own | Seen twice as the origin of streamer clips. |
| DramaAlert | internet | repost | In the probe list; creator drama. |
| NoContextHumans | online | repost | In the probe list; viral clips. |
| crazyclipsonly | online | repost | In the probe list; viral clips. |
| interesting_aIl | offbeat | repost | In the probe list; odd clips. |
| AMAZlNGNATURE | offbeat | repost | In the probe list; nature clips. |
| insanevideos | online | repost | Seen; viral video uploads. |
| MarioNawfal | online, world | repost | Seen; re-uploads with media_source. |
| SomaKazima2 | internet | own | Seen; 1.7M view clip found through the probe. |
| IAmLilRico | life | repost | Seen; relationship clips, 699k views. |
| lyricsmotions | internet | repost | Seen; prompt posts. |
| kenyasgossips | offbeat, internet | repost | Seen as origin of the 5M view giraffe video. |
| hayasaka_aryan | internet | repost | Seen twice; reaction videos reused by others. |
| TheNairobiTimez | online | repost | In the probe list. |

## Prune clock

Started 2026-10-09 (run 2026-10-09T0629Z, the first run that read all six groups). On the first run
after 2026-10-12T06:29Z, drop every account that has not produced a kept post (its own or an
origin it reposted) in any capture since 2026-10-09, and list the dropped handles in
capture/NOTES.md. Accounts that authored a kept post in run 2026-10-09T0629Z (origins they reposted not yet counted): Reuters, SkyNews,
Osint613, visegrad24, Gerashchenko_en, EricLDaugh (news); unusual_whales, WatcherGuru,
Cointelegraph, cryptorover, AshCrypto (money); AndrewCurran_, jukan05, elonmusk, sciencegirl
(science); PopBase, PopCrave, IGN, billboard, Nintendo, Wuthering_Waves (culture); NFL, NFLMemes,
RapSheet, MLB, SportsCenter, barstoolsports, FearedBuck, FabrizioRomano (sports); MarioNawfal,
IAmLilRico (online). This list is a starting tally, not a verdict.
