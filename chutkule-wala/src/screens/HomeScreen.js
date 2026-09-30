import React, { useEffect, useState, useCallback, useMemo } from 'react';
import {
  FlatList,
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  ActivityIndicator,
  RefreshControl,
  ScrollView,
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

export default function HomeScreen({ colors, navigation }) {
  const [jokes, setJokes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [activeCategory, setActiveCategory] = useState('Sab');
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [jokeOfTheDay, setJokeOfTheDay] = useState(null);
  const [randomJoke, setRandomJoke] = useState(null);

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

      // Pick a featured Joke of the Day on first load
      if (!jokeOfTheDay && list.length > 0) {
        // Pick an entertaining one with good length
        const candidate = list.find((j) => j.text.length > 80 && j.text.length < 250) || list[0];
        setJokeOfTheDay(candidate);
      }
    } catch (err) {
      console.log('Error fetching jokes:', err);
    } finally {
      setLoading(false);
    }
  }, [activeCategory, jokeOfTheDay]);

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
    if (jokeOfTheDay && jokeOfTheDay.id === joke.id) {
      setJokeOfTheDay((prev) => ({ ...prev, is_favorite: newFav ? 1 : 0 }));
    }
    if (randomJoke && randomJoke.id === joke.id) {
      setRandomJoke((prev) => ({ ...prev, is_favorite: newFav ? 1 : 0 }));
    }
  };

  const handleRandomJoke = async () => {
    const rJoke = await getRandomJoke();
    if (rJoke) {
      setRandomJoke(rJoke);
    }
  };

  // List Header with Joke of the Day & Category Chips
  const renderHeader = () => (
    <View style={styles.headerContainer}>
      {/* Category Pills Bar */}
      <View style={[styles.categoriesWrapper, { backgroundColor: colors.card, borderBottomColor: colors.border }]}>
        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.chipScroll}
        >
          {[{ id: 'Sab', name: 'Sab', emoji: '✨' }, ...categories].map((item) => {
            const isActive = activeCategory === item.id;
            return (
              <TouchableOpacity
                key={item.id}
                onPress={() => setActiveCategory(item.id)}
                activeOpacity={0.75}
                style={[
                  styles.chip,
                  {
                    backgroundColor: isActive ? colors.chipActiveBg : colors.chipBg,
                    borderColor: isActive ? colors.chipActiveBg : colors.chipBorder,
                  },
                ]}
              >
                <Text style={styles.chipEmoji}>{item.emoji}</Text>
                <Text
                  style={[
                    styles.chipText,
                    {
                      color: isActive ? colors.chipActiveText : colors.chipText,
                      fontFamily: isActive ? typography.bold : typography.medium,
                    },
                  ]}
                >
                  {item.name}
                </Text>
              </TouchableOpacity>
            );
          })}
        </ScrollView>
      </View>

      {/* Sub Header: Counter & Surprise Me Button */}
      <View style={styles.statsBar}>
        <View style={styles.statsLeft}>
          <Text style={[styles.statsTitle, { color: colors.text }]}>
            {activeCategory === 'Sab' ? 'Sabhi Desi Chutkule' : activeCategory}
          </Text>
          <Text style={[styles.statsSubtitle, { color: colors.textMuted }]}>
            {jokes.length} मजेदार चुटकले
          </Text>
        </View>

        <TouchableOpacity
          style={[styles.randomBtn, { backgroundColor: colors.primaryLight, borderColor: colors.primary }]}
          onPress={handleRandomJoke}
          activeOpacity={0.7}
        >
          <Ionicons name="sparkles" size={15} color={colors.primary} />
          <Text style={[styles.randomBtnText, { color: colors.primary }]}>
            Random Joke
          </Text>
        </TouchableOpacity>
      </View>

      {/* Random Joke Preview Card if triggered */}
      {randomJoke && (
        <View style={[styles.randomCardWrapper, { backgroundColor: colors.heroBg, borderColor: colors.heroBorder }]}>
          <View style={styles.randomCardHeader}>
            <View style={styles.randomBadge}>
              <Text style={{ fontSize: 13 }}>🎲</Text>
              <Text style={[styles.randomBadgeText, { color: colors.heroText }]}>
                Surprise Joke
              </Text>
            </View>
            <TouchableOpacity
              onPress={() => setRandomJoke(null)}
              hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
            >
              <Ionicons name="close-circle" size={22} color={colors.textMuted} />
            </TouchableOpacity>
          </View>
          <JokeCard joke={randomJoke} onToggleFav={onToggleFav} colors={colors} />
        </View>
      )}

      {/* Joke of the Day Highlight Banner (only on 'Sab' tab and when no random card is showing) */}
      {activeCategory === 'Sab' && jokeOfTheDay && !randomJoke && (
        <View style={styles.heroSection}>
          <View style={[styles.heroCard, { backgroundColor: colors.heroBg, borderColor: colors.heroBorder }]}>
            <View style={styles.heroHeader}>
              <View style={styles.heroBadge}>
                <Ionicons name="star" size={13} color={colors.gold} />
                <Text style={[styles.heroBadgeText, { color: colors.heroText }]}>
                  JOKE OF THE DAY
                </Text>
              </View>
              <TouchableOpacity onPress={handleRandomJoke} style={styles.shuffleHeroBtn}>
                <Ionicons name="shuffle" size={15} color={colors.heroText} />
                <Text style={[styles.shuffleHeroText, { color: colors.heroText }]}>बदलें</Text>
              </TouchableOpacity>
            </View>
            <JokeCard joke={jokeOfTheDay} onToggleFav={onToggleFav} colors={colors} />
          </View>
        </View>
      )}
    </View>
  );

  return (
    <View style={[styles.container, { backgroundColor: colors.bg }]}>
      {loading ? (
        <View style={styles.centerContainer}>
          <ActivityIndicator size="large" color={colors.primary} />
          <Text style={[styles.loadingText, { color: colors.textMuted }]}>
            हंसी के चुटकले लोड हो रहे हैं...
          </Text>
        </View>
      ) : (
        <FlatList
          data={jokes}
          keyExtractor={(j) => String(j.id)}
          ListHeaderComponent={renderHeader}
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
          contentContainerStyle={{ paddingBottom: 80 }}
        />
      )}

      {/* Floating Action Button for Next Random Joke */}
      <TouchableOpacity
        style={[styles.fab, { backgroundColor: colors.primary }]}
        onPress={handleRandomJoke}
        activeOpacity={0.85}
      >
        <Ionicons name="dice" size={22} color="#FFFFFF" />
        <Text style={styles.fabText}>Agla Joke</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  headerContainer: {
    marginBottom: 6,
  },
  categoriesWrapper: {
    paddingVertical: 10,
    borderBottomWidth: 1,
  },
  chipScroll: {
    paddingHorizontal: 14,
    gap: 8,
  },
  chip: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 14,
    paddingVertical: 7,
    borderRadius: 22,
    borderWidth: 1,
  },
  chipEmoji: {
    fontSize: 13,
  },
  chipText: {
    fontSize: 12.5,
  },
  statsBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 18,
    paddingTop: 14,
    paddingBottom: 8,
  },
  statsLeft: {
    flex: 1,
  },
  statsTitle: {
    fontFamily: typography.bold,
    fontSize: 16,
  },
  statsSubtitle: {
    fontFamily: typography.regular,
    fontSize: 12,
    marginTop: 2,
  },
  randomBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
    borderWidth: 1,
  },
  randomBtnText: {
    fontFamily: typography.bold,
    fontSize: 12,
  },
  heroSection: {
    paddingHorizontal: 14,
    paddingVertical: 6,
  },
  heroCard: {
    borderRadius: 22,
    borderWidth: 1,
    overflow: 'hidden',
    paddingTop: 10,
  },
  heroHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingBottom: 4,
  },
  heroBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
  },
  heroBadgeText: {
    fontFamily: typography.bold,
    fontSize: 11,
    letterSpacing: 0.8,
  },
  shuffleHeroBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
  },
  shuffleHeroText: {
    fontFamily: typography.bold,
    fontSize: 11,
  },
  randomCardWrapper: {
    marginHorizontal: 14,
    marginVertical: 8,
    borderRadius: 22,
    borderWidth: 1,
    paddingTop: 10,
    overflow: 'hidden',
  },
  randomCardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingBottom: 4,
  },
  randomBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  randomBadgeText: {
    fontFamily: typography.bold,
    fontSize: 12,
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
  fab: {
    position: 'absolute',
    bottom: 20,
    right: 18,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 7,
    paddingVertical: 12,
    paddingHorizontal: 18,
    borderRadius: 28,
    elevation: 6,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.25,
    shadowRadius: 8,
  },
  fabText: {
    fontFamily: typography.bold,
    color: '#FFFFFF',
    fontSize: 13,
  },
});
