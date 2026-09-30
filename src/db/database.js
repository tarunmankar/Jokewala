import * as SQLite from 'expo-sqlite';
import jokesData from '../../assets/jokes.json';
import categoriesData from '../../assets/categories.json';

let db = null;
let initPromise = null;

const categoryMetaMap = {};
categoriesData.forEach((c) => {
  categoryMetaMap[c.id] = c;
});

export const getCategoryMeta = (catId) =>
  categoryMetaMap[catId] || { id: catId, name: catId, emoji: '😄' };

export async function initDB() {
  if (db) return db;
  if (initPromise) return initPromise;

  initPromise = (async () => {
    try {
      const database = await SQLite.openDatabaseAsync('jokewala_v2.db');

      await database.execAsync(`
        CREATE TABLE IF NOT EXISTS jokes (
          id TEXT PRIMARY KEY NOT NULL,
          text TEXT NOT NULL,
          category TEXT NOT NULL,
          subcategory TEXT,
          tags TEXT,
          is_favorite INTEGER DEFAULT 0,
          created_at INTEGER DEFAULT (strftime('%s', 'now'))
        );
      `);

      // Check existing jokes count
      const countResult = await database.getFirstAsync('SELECT count(*) as count FROM jokes');
      const currentCount = countResult ? countResult.count : 0;

      // Sync jokes if count differs
      if (currentCount !== jokesData.length) {
        // Clean up any obsolete jokes
        try {
          const validIds = new Set(jokesData.map((j) => String(j.id)));
          const existing = await database.getAllAsync('SELECT id FROM jokes');
          const obsolete = existing.filter((r) => !validIds.has(r.id)).map((r) => r.id);
          for (const oldId of obsolete) {
            await database.runAsync('DELETE FROM jokes WHERE id = ?', [oldId]);
          }
        } catch (cleanErr) {
          console.warn('DB cleanup warning:', cleanErr);
        }

        // Insert or update jokes in a safe transaction
        await database.withTransactionAsync(async () => {
          for (const j of jokesData) {
            const jokeText = j.text || j.joke || j.content;
            if (!jokeText) continue;
            const jokeId = String(j.id);
            const cat = j.category || 'General';
            const subcat = j.subcategory || '';
            const tagsStr = Array.isArray(j.tags) ? j.tags.join(' ') : (j.tags || '');

            await database.runAsync(
              `INSERT OR REPLACE INTO jokes (id, text, category, subcategory, tags, is_favorite) VALUES (?, ?, ?, ?, ?, COALESCE((SELECT is_favorite FROM jokes WHERE id = ?), 0))`,
              [jokeId, jokeText, cat, subcat, tagsStr, jokeId]
            );
          }
        });

        // Try migrating favorites from old database if any
        try {
          const oldDb = await SQLite.openDatabaseAsync('jokewala.db');
          const oldFavs = await oldDb.getAllAsync('SELECT id FROM jokes WHERE is_favorite = 1');
          if (oldFavs && oldFavs.length > 0) {
            for (const f of oldFavs) {
              await database.runAsync('UPDATE jokes SET is_favorite = 1 WHERE id = ?', [f.id]);
            }
          }
        } catch (migErr) {
          // No old database to migrate from
        }
      }

      db = database;
      return db;
    } catch (err) {
      console.error('initDB error:', err);
      initPromise = null;
      throw err;
    }
  })();

  return initPromise;
}

export const getAllJokes = async () => {
  const database = await initDB();
  return database.getAllAsync('SELECT * FROM jokes ORDER BY id ASC');
};

export const getByCategory = async (category) => {
  const database = await initDB();
  return database.getAllAsync(
    'SELECT * FROM jokes WHERE category = ? ORDER BY id ASC',
    [category]
  );
};

export const getFavorites = async () => {
  const database = await initDB();
  return database.getAllAsync(
    'SELECT * FROM jokes WHERE is_favorite = 1 ORDER BY id DESC'
  );
};

export const searchJokes = async (query) => {
  const database = await initDB();
  const trimmed = query.trim();
  if (!trimmed) return [];

  // Stop words strip karein
  const stopWords = new Set([
    'joke',
    'jokes',
    'chutkule',
    'chutkula',
    'ke',
    'ka',
    'ki',
    'ko',
    'me',
    'mein',
    'in',
    'hindi',
    'hinglish',
  ]);
  const words = trimmed
    .toLowerCase()
    .split(/\s+/)
    .filter((w) => w.length > 1 && !stopWords.has(w));

  const searchTerms = words.length > 0 ? words : [trimmed.toLowerCase()];

  const conditions = searchTerms.map(
    () => `(text LIKE ? OR category LIKE ? OR subcategory LIKE ? OR tags LIKE ?)`
  );
  const whereClause = conditions.join(' AND ');

  const params = [];
  searchTerms.forEach((term) => {
    const p = `%${term}%`;
    params.push(p, p, p, p);
  });

  return database.getAllAsync(
    `SELECT * FROM jokes WHERE ${whereClause} ORDER BY id ASC`,
    params
  );
};

export const toggleFavorite = async (id, isFav) => {
  const database = await initDB();
  return database.runAsync(
    'UPDATE jokes SET is_favorite = ? WHERE id = ?',
    [isFav ? 1 : 0, String(id)]
  );
};

export const getCategories = async () => {
  // Instantly return the pre-configured categories array with rich emojis
  return categoriesData;
};

export const getRandomJoke = async () => {
  const database = await initDB();
  return database.getFirstAsync('SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1');
};
