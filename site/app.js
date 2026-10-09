// Three small conveniences. The page reads fine without this file.
(function () {
  'use strict';
  var all = function (sel) { return Array.prototype.slice.call(document.querySelectorAll(sel)); };

  // ---- Which worlds do you live in? Kept in this browser only.
  var KEY = 'mts.worlds';
  var picks = [];
  try { picks = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { picks = []; }
  if (!Array.isArray(picks)) picks = [];

  // A desk card on the front page is the switch for that desk.
  var cards = all('.dk[data-desk]');
  // Everything on the page that belongs to a desk: the lead, the pulse items, the researched stories.
  var items = all('[data-desks]');
  var tools = document.getElementById('mine-tools');
  var count = document.getElementById('mine-count');
  var clear = document.getElementById('mine-clear');
  var mine = function (desk) { return picks.indexOf(desk) >= 0; };

  function apply() {
    var on = 0;
    cards.forEach(function (b) {
      var picked = mine(b.dataset.desk);
      if (picked) on++;
      b.setAttribute('aria-pressed', picked ? 'true' : 'false');
    });
    // An item is outside your worlds when you have picked some desks and none of them is its own.
    items.forEach(function (el) {
      el.classList.toggle('is-outside', picks.length > 0 && !el.dataset.desks.split(' ').some(mine));
    });
    if (count) count.textContent = on ? on + ' of ' + cards.length + ' selected' : 'None selected';
    if (clear) clear.disabled = !picks.length;
  }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(picks)); } catch (e) { /* private window: still works for this visit */ }
    apply();
  }

  cards.forEach(function (b) {
    b.addEventListener('click', function () {
      var i = picks.indexOf(b.dataset.desk);
      if (i >= 0) picks.splice(i, 1); else picks.push(b.dataset.desk);
      save();
    });
  });
  if (clear) clear.addEventListener('click', function () { picks = []; save(); });
  if (tools) tools.hidden = false;
  apply();

  // ---- Say so when the record is old. The page is static; the reader's clock is the only one that knows.
  var asof = document.getElementById('asof');
  var stale = document.getElementById('stale');
  if (asof && stale) {
    var hours = (Date.now() - Date.parse(asof.getAttribute('datetime'))) / 3600000;
    if (hours >= 3) {
      stale.textContent = 'This record was last updated ' + (hours < 48 ? Math.round(hours) + ' hours' : Math.round(hours / 24) + ' days') + ' ago. Anything still developing has moved on since.';
      stale.hidden = false;
    }
  }

  // ---- Order of a list: each set of sort buttons orders the list in its own section. On the pulse
  // the stylesheet sizes an item by its place in the list, so moving the items is all there is to do.
  all('.sort').forEach(function (group) {
    var section = group.closest('section');
    var list = section && section.querySelector('.pg, .stories');
    var sorts = Array.prototype.slice.call(group.querySelectorAll('button'));
    sorts.forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (!list) return;
        var key = btn.dataset.sort;
        sorts.forEach(function (o) { o.setAttribute('aria-pressed', o === btn ? 'true' : 'false'); });
        Array.prototype.slice.call(list.children)
          .sort(function (a, b) { return Number(b.dataset[key]) - Number(a.dataset[key]); })
          .forEach(function (li) { list.appendChild(li); });
      });
    });
  });
})();
