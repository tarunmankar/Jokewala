import React, { useState, useCallback } from 'react';
import { View, Text, FlatList, StyleSheet, RefreshControl } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import JokeCard from '../components/JokeCard';
import { getFavorites, toggleFavorite } from '../db/database';
import { typography } from '../theme';

export default function FavoritesScreen({ colors }) {
  const [favorites, setFavorites] = useState([]);
  const [refreshing, setRefreshing] = useState(false);

  const loadFavorites = async () => {
    try {
      const list = await getFavorites();
      setFavorites(list);
    } catch (err) {
      console.log('Error loading favorites:', err);
    }
  };

  useFocusEffect(
    useCallback(() => {
      loadFavorites();
    }, [])
  );

  const onRefresh = async () => {
    setRefreshing(true);
    await loadFavorites();
    setRefreshing(false);
  };

  const onToggleFav = async (joke) => {
    await toggleFavorite(joke.id, false);
    setFavorites((prev) => prev.filter((item) => item.id !== joke.id));
  };

  return (
    <View style={[styles.container, { backgroundColor: colors.bg }]}>
      {favorites.length > 0 && (
        <View style={styles.header}>
          <Text style={[styles.headerCount, { color: colors.textMuted }]}>
            {favorites.length} Favorite Jokes
          </Text>
        </View>
      )}

      <FlatList
        data={favorites}
        keyExtractor={(item) => String(item.id)}
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
        contentContainerStyle={{ paddingVertical: 8, paddingBottom: 24 }}
        ListEmptyComponent={
          <View style={styles.emptyContainer}>
            <Text style={{ fontSize: 50, marginBottom: 12 }}>❤️</Text>
            <Text style={[styles.emptyTitle, { color: colors.text }]}>
              Koi Favorite Joke Nahi Hai
            </Text>
            <Text style={[styles.emptySubtitle, { color: colors.textMuted }]}>
              Home ya Search screen par kisi bhi joke ke niche diye ❤️ Like button ko dabakar use yahan save karein.
            </Text>
          </View>
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  header: {
    paddingHorizontal: 20,
    paddingTop: 12,
    paddingBottom: 4,
  },
  headerCount: {
    fontFamily: typography.medium,
    fontSize: 13,
  },
  emptyContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 100,
    paddingHorizontal: 40,
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
