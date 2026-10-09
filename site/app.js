// Two small conveniences. The page reads fine without this file.
(function () {
  'use strict';

  // ---- Which worlds do you live in? Kept in this browser only.
  var KEY = 'mts.worlds';
  var picks = [];
  try { picks = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { picks = []; }
  if (!Array.isArray(picks)) picks = [];

  var buttons = Array.prototype.slice.call(document.querySelectorAll('.pick'));
  var out = document.getElementById('yours-out');
  var stories = Array.prototype.slice.call(document.querySelectorAll('.story'));
  var rows = Array.prototype.slice.call(document.querySelectorAll('.rec-row'));
  var rec = document.querySelector('.rec');

  function apply() {
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', picks.indexOf(b.dataset.desk) >= 0 ? 'true' : 'false'); });
    rows.forEach(function (r) { r.classList.toggle('is-mine', picks.indexOf(r.dataset.desk) >= 0); });
    if (rec) rec.classList.toggle('has-mine', picks.length > 0);
    if (!out) return;
    if (!picks.length) { out.hidden = true; return; }
    var outside = stories.filter(function (s) {
      return !s.dataset.desks.split(' ').some(function (d) { return picks.indexOf(d) >= 0; });
    });
    stories.forEach(function (s) { s.classList.toggle('is-outside', outside.indexOf(s) >= 0); });
    out.hidden = false;
    out.textContent = '';
    var b = document.createElement('b');
    if (!stories.length) {
      b.textContent = 'Saved.';
      out.appendChild(b);
      out.appendChild(document.createTextNode(' Stories outside your worlds will be marked here as they are written up.'));
      return;
    }
    var top = outside.slice().sort(function (a, c) { return c.dataset.mag - a.dataset.mag; })[0];
    b.textContent = outside.length + ' of ' + stories.length + ' stories';
    out.appendChild(b);
    out.appendChild(document.createTextNode(' in the bulletin are outside your worlds' + (top ? '. The largest is a ' + Number(top.dataset.mag).toFixed(1) + ': ' : '.')));
    if (top) {
      var a = document.createElement('a');
      a.href = '#' + top.id;
      a.textContent = top.querySelector('h3').textContent;
      out.appendChild(a);
    }
  }

  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      var i = picks.indexOf(b.dataset.desk);
      if (i >= 0) picks.splice(i, 1); else picks.push(b.dataset.desk);
      try { localStorage.setItem(KEY, JSON.stringify(picks)); } catch (e) { /* private window: still works for this visit */ }
      apply();
    });
  });
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

  // ---- Order of the bulletin
  var list = document.querySelector('.bulletin .stories');
  var sorts = Array.prototype.slice.call(document.querySelectorAll('.sort button'));
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
})();
