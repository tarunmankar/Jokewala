import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  TextInput,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import JokeCard from '../components/JokeCard';
import { searchJokes, toggleFavorite, getCategories } from '../db/database';
import { typography } from '../theme';

export default function SearchScreen({ colors }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    getCategories().then((cats) => setSuggestions(cats.slice(0, 8)));
  }, []);

  const performSearch = async (text) => {
    setLoading(true);
    if (!text || text.trim() === '') {
      setResults([]);
    } else {
      const data = await searchJokes(text.trim());
      setResults(data);
    }
    setLoading(false);
  };

  useEffect(() => {
    const delayDebounceFn = setTimeout(() => {
      performSearch(query);
    }, 200);

    return () => clearTimeout(delayDebounceFn);
  }, [query]);

  const onToggleFav = async (joke) => {
    const newFav = !joke.is_favorite;
    await toggleFavorite(joke.id, newFav);
    setResults((prev) =>
      prev.map((item) =>
        item.id === joke.id ? { ...item, is_favorite: newFav ? 1 : 0 } : item
      )
    );
  };

  return (
    <View style={[styles.container, { backgroundColor: colors.bg }]}>
      {/* Search Bar Input Container */}
      <View
        style={[
          styles.searchBox,
          {
            backgroundColor: colors.card,
            borderColor: colors.border,
          },
        ]}
      >
        <Ionicons name="search" size={20} color={colors.primary} style={styles.searchIcon} />
        <TextInput
          placeholder="Joke, topic ya keyword search karein..."
          placeholderTextColor={colors.textMuted}
          value={query}
          onChangeText={setQuery}
          style={[styles.input, { color: colors.text }]}
          autoCapitalize="none"
          returnKeyType="search"
        />
        {query.length > 0 && (
          <TouchableOpacity
            onPress={() => setQuery('')}
            hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
          >
            <Ionicons name="close-circle" size={19} color={colors.textMuted} />
          </TouchableOpacity>
        )}
      </View>

      {/* Suggested Keywords / Trending Categories */}
      {query.length === 0 && (
        <View style={styles.suggestWrapper}>
          <View style={styles.suggestHeader}>
            <Ionicons name="flame" size={16} color={colors.primary} />
            <Text style={[styles.suggestLabel, { color: colors.textSecondary }]}>
              Trending Searches
            </Text>
          </View>
          <View style={styles.tagWrap}>
            {[
              { label: '📛 Name Jokes', q: 'names' },
              { label: '🔥 Deepak', q: 'deepak' },
              { label: '😎 Rahul', q: 'rahul' },
              { label: '👫 Pati Patni', q: 'pati patni' },
              { label: '😉 Naughty', q: 'naughty' },
              { label: '🎅 Santa Banta', q: 'santa banta' },
              { label: '👶 Pappu', q: 'pappu' },
              { label: '💑 Boyfriend / GF', q: 'girlfriend' },
              { label: '🩺 Doctor', q: 'doctor' },
              { label: '💼 Office', q: 'office' },
              { label: '🎓 Masterji', q: 'teacher' },
              { label: '💍 Shaadi', q: 'shaadi' },
              { label: '🤝 Dosti', q: 'dosti' },
            ].map((item, idx) => (
              <TouchableOpacity
                key={idx}
                style={[
                  styles.tag,
                  {
                    backgroundColor: colors.card,
                    borderColor: colors.border,
                  },
                ]}
                onPress={() => setQuery(item.q)}
                activeOpacity={0.7}
              >
                <Text style={[styles.tagText, { color: colors.text }]}>
                  {item.label}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
        </View>
      )}

      {/* Results Header */}
      {query.length > 0 && (
        <View style={styles.resultHeader}>
          <Text style={[styles.resultCount, { color: colors.textMuted }]}>
            {loading ? 'खोज रहे हैं...' : `${results.length} चुटकले मिले`}
          </Text>
        </View>
      )}

      {loading && (
        <ActivityIndicator style={{ marginTop: 24 }} color={colors.primary} />
      )}

      {/* Results List */}
      <FlatList
        data={results}
        keyExtractor={(item) => String(item.id)}
        renderItem={({ item }) => (
          <JokeCard joke={item} onToggleFav={onToggleFav} colors={colors} />
        )}
        contentContainerStyle={{ paddingBottom: 24 }}
        ListEmptyComponent={
          !loading && query.length > 0 ? (
            <View style={styles.emptyContainer}>
              <Text style={{ fontSize: 44, marginBottom: 12 }}>🧐</Text>
              <Text style={[styles.emptyTitle, { color: colors.text }]}>
                Koi joke nahi mila
              </Text>
              <Text style={[styles.emptySubtitle, { color: colors.textMuted }]}>
                Kuch aur keyword search karein (jaise 'doctor', 'deepak', 'school', 'shadi')
              </Text>
            </View>
          ) : !loading && query.length === 0 ? (
            <View style={styles.emptyContainer}>
              <Text style={{ fontSize: 44, marginBottom: 12 }}>🔍</Text>
              <Text style={[styles.emptyTitle, { color: colors.text }]}>
                Apne Manpasand Jokes Khojein
              </Text>
              <Text style={[styles.emptySubtitle, { color: colors.textMuted }]}>
                Upar diye search bar me koi bhi shabda type karein ya kisi trending tag par tap karein.
              </Text>
            </View>
          ) : null
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 6,
  },
  searchBox: {
    flexDirection: 'row',
    alignItems: 'center',
    marginHorizontal: 16,
    marginVertical: 10,
    paddingHorizontal: 16,
    height: 52,
    borderRadius: 26,
    borderWidth: 1,
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.05,
    shadowRadius: 8,
    elevation: 2,
  },
  searchIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    fontFamily: typography.regular,
    fontSize: 15,
    height: '100%',
  },
  suggestWrapper: {
    paddingHorizontal: 18,
    marginVertical: 10,
  },
  suggestHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 10,
  },
  suggestLabel: {
    fontFamily: typography.bold,
    fontSize: 13,
    letterSpacing: 0.4,
  },
  tagWrap: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  tag: {
    paddingHorizontal: 13,
    paddingVertical: 7,
    borderRadius: 18,
    borderWidth: 1,
  },
  tagText: {
    fontFamily: typography.medium,
    fontSize: 12.5,
  },
  resultHeader: {
    paddingHorizontal: 20,
    paddingVertical: 6,
  },
  resultCount: {
    fontFamily: typography.medium,
    fontSize: 13,
  },
  emptyContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 60,
    paddingHorizontal: 36,
  },
  emptyTitle: {
    fontFamily: typography.bold,
    fontSize: 18,
    marginBottom: 8,
  },
  emptySubtitle: {
    fontFamily: typography.regular,
    fontSize: 14,
    textAlign: 'center',
    lineHeight: 22,
  },
});
