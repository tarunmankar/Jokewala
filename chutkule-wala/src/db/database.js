import * as SQLite from 'expo-sqlite';
import jokesData from '../../assets/jokes.json';
import categoriesData from '../../assets/categories.json';

let db;

const categoryMetaMap = {};
categoriesData.forEach((c) => {
  categoryMetaMap[c.id] = c;
});

export const getCategoryMeta = (catId) =>
  categoryMetaMap[catId] || { id: catId, name: catId, emoji: '😄' };

export async function initDB() {
  if (!db) {
    db = await SQLite.openDatabaseAsync('jokewala.db');
  }

  await db.execAsync(`
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

  // Ensure 'tags' column exists if upgraded
  try {
    await db.execAsync(`ALTER TABLE jokes ADD COLUMN tags TEXT;`);
  } catch (e) {
    // Column already exists
  }

  // Pehli baar ya dataset update par naye jokes insert karega (favorites intact rahenge)
  await db.withTransactionAsync(async () => {
    for (const j of jokesData) {
      const jokeText = j.text || j.joke || j.content;
      if (!jokeText) continue;
      const jokeId = String(j.id);
      const cat = j.category || 'General';
      const subcat = j.subcategory || '';
      const tagsStr = Array.isArray(j.tags) ? j.tags.join(' ') : (j.tags || '');

      await db.runAsync(
        `INSERT OR REPLACE INTO jokes (id, text, category, subcategory, tags, is_favorite) VALUES (?, ?, ?, ?, ?, COALESCE((SELECT is_favorite FROM jokes WHERE id = ?), 0))`,
        [jokeId, jokeText, cat, subcat, tagsStr, jokeId]
      );
    }
  });

  return db;
}

export const getAllJokes = async () => {
  if (!db) await initDB();
  return db.getAllAsync('SELECT * FROM jokes ORDER BY id ASC');
};

export const getByCategory = async (category) => {
  if (!db) await initDB();
  return db.getAllAsync(
    'SELECT * FROM jokes WHERE category = ? ORDER BY id ASC',
    [category]
  );
};

export const getFavorites = async () => {
  if (!db) await initDB();
  return db.getAllAsync(
    'SELECT * FROM jokes WHERE is_favorite = 1 ORDER BY id DESC'
  );
};

export const searchJokes = async (query) => {
  if (!db) await initDB();
  const trimmed = query.trim();
  if (!trimmed) return [];

  // Stop words strip karein taaki "pati patni jokes" ya "naughty chutkule" accurately match ho sake
  const stopWords = new Set(['joke', 'jokes', 'chutkule', 'chutkula', 'ke', 'ka', 'ki', 'ko', 'me', 'mein', 'in', 'hindi', 'hinglish']);
  const words = trimmed
    .toLowerCase()
    .split(/\s+/)
    .filter((w) => w.length > 1 && !stopWords.has(w));

  const searchTerms = words.length > 0 ? words : [trimmed.toLowerCase()];

  // Har keyword text, category, subcategory ya tags me match hoga
  const conditions = searchTerms.map(
    () => `(text LIKE ? OR category LIKE ? OR subcategory LIKE ? OR tags LIKE ?)`
  );
  const whereClause = conditions.join(' AND ');

  const params = [];
  searchTerms.forEach((term) => {
    const p = `%${term}%`;
    params.push(p, p, p, p);
  });

  return db.getAllAsync(
    `SELECT * FROM jokes WHERE ${whereClause} ORDER BY id ASC`,
    params
  );
};

export const toggleFavorite = async (id, isFav) => {
  if (!db) await initDB();
  return db.runAsync(
    'UPDATE jokes SET is_favorite = ? WHERE id = ?',
    [isFav ? 1 : 0, String(id)]
  );
};

export const getCategories = async () => {
  if (!db) await initDB();
  const rows = await db.getAllAsync(
    'SELECT DISTINCT category FROM jokes ORDER BY category ASC'
  );
  return rows
    .map((r) => r.category)
    .filter(Boolean)
    .map((catId) => getCategoryMeta(catId));
};

export const getRandomJoke = async () => {
  if (!db) await initDB();
  return db.getFirstAsync('SELECT * FROM jokes ORDER BY RANDOM() LIMIT 1');
};
