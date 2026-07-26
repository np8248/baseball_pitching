"use strict";
/* Shared localStorage-backed collections for the Save Pitchers / Save Teams /
   Saved Games / Records home-screen features. No backend - everything lives
   in the browser, same as the rest of the app. */
const Store = (() => {
  function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 8); }

  function read(key, fallback) {
    try {
      const raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }
  function write(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) { /* private browsing / full */ }
  }

  function collection(key) {
    return {
      list() { return read(key, []); },
      get(id) { return read(key, []).find(i => i.id === id) || null; },
      save(item) {
        const items = read(key, []);
        const idx = items.findIndex(i => i.id === item.id);
        if (idx >= 0) items[idx] = item; else items.unshift(item);
        write(key, items);
        return item;
      },
      remove(id) {
        write(key, read(key, []).filter(i => i.id !== id));
      },
      clear() { write(key, []); }
    };
  }

  return {
    uid,
    pitchers: collection("pp.pitchers.v1"),
    teams: collection("pp.teams.v1"),
    games: collection("pp.games.v1"),
    records: collection("pp.records.v1")
  };
})();
