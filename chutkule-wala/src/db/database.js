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
    db = await SQLite.openDatabaseAsync('chutkule.db');
  }

  await db.execAsync(`
    CREATE TABLE IF NOT EXISTS jokes (
      id TEXT PRIMARY KEY NOT NULL,
      text TEXT NOT NULL,
      category TEXT NOT NULL,
      subcategory TEXT,
      is_favorite INTEGER DEFAULT 0,
      created_at INTEGER DEFAULT (strftime('%s', 'now'))
    );
  `);

  // Pehli baar ya dataset update par naye jokes insert karega (favorites intact rahenge)
  await db.withTransactionAsync(async () => {
    for (const j of jokesData) {
      const jokeText = j.text || j.joke || j.content;
      if (!jokeText) continue;
      const jokeId = String(j.id);
      const cat = j.category || 'General';
      const subcat = j.subcategory || '';

      await db.runAsync(
        `INSERT OR IGNORE INTO jokes (id, text, category, subcategory, is_favorite) VALUES (?, ?, ?, ?, 0)`,
        [jokeId, jokeText, cat, subcat]
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
  const searchPattern = `%${query}%`;
  return db.getAllAsync(
    'SELECT * FROM jokes WHERE text LIKE ? OR category LIKE ? OR subcategory LIKE ? ORDER BY id ASC',
    [searchPattern, searchPattern, searchPattern]
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
