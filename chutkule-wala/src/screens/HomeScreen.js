import React, { useEffect, useState, useCallback } from 'react';
import {
  FlatList,
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import JokeCard from '../components/JokeCard';
import {
  getAllJokes,
  getByCategory,
  getCategories,
  toggleFavorite,
  getRandomJoke,
} from '../db/database';
import { typography } from '../theme';

export default function HomeScreen({ colors }) {
  const [jokes, setJokes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [activeCategory, setActiveCategory] = useState('Sab');
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [randomJokeModal, setRandomJokeModal] = useState(null);

  const loadCategories = async () => {
    try {
      const cats = await getCategories();
      setCategories(cats);
    } catch (err) {
      console.log('Error fetching categories:', err);
    }
  };

  const loadJokes = useCallback(async () => {
    try {
      const list =
        activeCategory === 'Sab'
          ? await getAllJokes()
          : await getByCategory(activeCategory);
      setJokes(list);
    } catch (err) {
      console.log('Error fetching jokes:', err);
    } finally {
      setLoading(false);
    }
  }, [activeCategory]);

  useEffect(() => {
    loadCategories();
  }, []);

  useEffect(() => {
    setLoading(true);
    loadJokes();
  }, [loadJokes]);

  const onRefresh = async () => {
    setRefreshing(true);
    await loadCategories();
    await loadJokes();
    setRefreshing(false);
  };

  const onToggleFav = async (joke) => {
    const newFav = !joke.is_favorite;
    await toggleFavorite(joke.id, newFav);
    setJokes((prev) =>
      prev.map((item) =>
        item.id === joke.id ? { ...item, is_favorite: newFav ? 1 : 0 } : item
      )
    );
  };

  const handleRandomJoke = async () => {
    const joke = await getRandomJoke();
    if (joke) {
      setRandomJokeModal(joke);
    }
  };

  return (
    <View style={[styles.container, { backgroundColor: colors.bg }]}>
      {/* Category Chips Bar */}
      <View style={{ backgroundColor: colors.card, borderBottomWidth: 1, borderBottomColor: colors.border }}>
        <FlatList
          horizontal
          data={[{ id: 'Sab', name: 'Sab', emoji: '✨' }, ...categories]}
          keyExtractor={(item) => item.id}
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.chipList}
          renderItem={({ item }) => {
            const isActive = activeCategory === item.id;
            return (
              <TouchableOpacity
                onPress={() => setActiveCategory(item.id)}
                activeOpacity={0.8}
                style={[
                  styles.chip,
                  {
                    backgroundColor: isActive ? colors.chipActiveBg : colors.chipBg,
                    borderColor: isActive ? colors.chipActiveBg : colors.border,
                  },
                ]}
              >
                <Text
                  style={[
                    styles.chipText,
                    { color: isActive ? colors.chipActiveText : colors.chipText },
                  ]}
                >
                  {item.emoji} {item.name}
                </Text>
              </TouchableOpacity>
            );
          }}
        />
      </View>

      {/* Floating / Top Surprise Me Bar */}
      <View style={styles.topBar}>
        <Text style={[styles.jokeCountText, { color: colors.textMuted }]}>
          {jokes.length} Desi Jokes
        </Text>
        <TouchableOpacity
          style={[styles.surpriseBtn, { backgroundColor: colors.primaryLight }]}
          onPress={handleRandomJoke}
          activeOpacity={0.8}
        >
          <Ionicons name="sparkles" size={15} color={colors.primary} />
          <Text style={[styles.surpriseText, { color: colors.primary }]}>
            Random Joke
          </Text>
        </TouchableOpacity>
      </View>

      {/* Random Joke Preview Card if triggered */}
      {randomJokeModal && (
        <View style={styles.randomBannerContainer}>
          <View style={styles.randomHeader}>
            <Text style={[styles.randomTitle, { color: colors.primary }]}>
              🎲 Surprise Joke (Random)
            </Text>
            <TouchableOpacity onPress={() => setRandomJokeModal(null)}>
              <Ionicons name="close-circle" size={22} color={colors.textMuted} />
            </TouchableOpacity>
          </View>
          <JokeCard
            joke={randomJokeModal}
            onToggleFav={handleToggleFav}
            colors={colors}
          />
        </View>
      )}

      {/* Main Jokes Feed */}
      {loading ? (
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color={colors.primary} />
          <Text style={[styles.loadingText, { color: colors.textMuted }]}>
            चुटकले लोड हो रहे हैं...
          </Text>
        </View>
      ) : (
        <FlatList
          data={jokes}
          keyExtractor={(j) => String(j.id)}
          renderItem={({ item }) => (
            <JokeCard joke={item} onToggleFav={onToggleFav} colors={colors} />
          )}
          refreshControl={
            <RefreshControl
              refreshing={refreshing}
              onRefresh={onRefresh}
              tintColor={colors.primary}
              colors={[colors.primary]}
            />
          }
          contentContainerStyle={{ paddingBottom: 24 }}
        />
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  chipList: {
    paddingHorizontal: 12,
    paddingVertical: 10,
    gap: 8,
  },
  chip: {
    paddingHorizontal: 16,
    paddingVertical: 7,
    borderRadius: 20,
    borderWidth: 1,
  },
  chipText: {
    fontFamily: typography.medium,
    fontSize: 13,
  },
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 8,
  },
  jokeCountText: {
    fontFamily: typography.regular,
    fontSize: 13,
  },
  surpriseBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 12,
    paddingVertical: 5,
    borderRadius: 14,
  },
  surpriseText: {
    fontFamily: typography.bold,
    fontSize: 12,
  },
  randomBannerContainer: {
    paddingHorizontal: 16,
    marginBottom: 6,
  },
  randomCard: {
    borderWidth: 1.5,
    borderRadius: 14,
    padding: 14,
  },
  randomHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 6,
  },
  randomTitle: {
    fontFamily: typography.bold,
    fontSize: 13,
  },
  randomText: {
    fontFamily: typography.regular,
    fontSize: 15,
    lineHeight: 24,
  },
  centerContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    gap: 12,
  },
  loadingText: {
    fontFamily: typography.medium,
    fontSize: 14,
  },
});
