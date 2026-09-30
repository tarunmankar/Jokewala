import React, { useState, useCallback } from 'react';
import { View, Text, FlatList, StyleSheet, RefreshControl, TouchableOpacity } from 'react-native';
import { useFocusEffect } from '@react-navigation/native';
import { Ionicons } from '@expo/vector-icons';
import JokeCard from '../components/JokeCard';
import { getFavorites, toggleFavorite } from '../db/database';
import { typography } from '../theme';

export default function FavoritesScreen({ colors, navigation }) {
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
          <Ionicons name="heart" size={16} color={colors.heart} />
          <Text style={[styles.headerCount, { color: colors.textSecondary }]}>
            {favorites.length} पसंदीदा चुटकले
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
            <View style={[styles.emptyIconCircle, { backgroundColor: colors.heartBg }]}>
              <Ionicons name="heart-dislike-outline" size={42} color={colors.heart} />
            </View>
            <Text style={[styles.emptyTitle, { color: colors.text }]}>
              Koi Favorite Joke Nahi Hai
            </Text>
            <Text style={[styles.emptySubtitle, { color: colors.textMuted }]}>
              Home ya Search screen par kisi bhi joke ke niche diye Like ❤️ button ko dabakar use yahan save karein.
            </Text>
            <TouchableOpacity
              style={[styles.exploreBtn, { backgroundColor: colors.primary }]}
              onPress={() => navigation.navigate('HomeTab')}
              activeOpacity={0.8}
            >
              <Ionicons name="happy-outline" size={18} color="#FFFFFF" />
              <Text style={styles.exploreBtnText}>चुटकले देखें</Text>
            </TouchableOpacity>
          </View>
        }
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 20,
    paddingTop: 14,
    paddingBottom: 4,
  },
  headerCount: {
    fontFamily: typography.bold,
    fontSize: 13,
  },
  emptyContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 80,
    paddingHorizontal: 40,
  },
  emptyIconCircle: {
    width: 80,
    height: 80,
    borderRadius: 40,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 16,
  },
  emptyTitle: {
    fontFamily: typography.bold,
    fontSize: 19,
    marginBottom: 8,
    textAlign: 'center',
  },
  emptySubtitle: {
    fontFamily: typography.regular,
    fontSize: 14,
    textAlign: 'center',
    lineHeight: 22,
    marginBottom: 20,
  },
  exploreBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 7,
    paddingVertical: 11,
    paddingHorizontal: 22,
    borderRadius: 22,
  },
  exploreBtnText: {
    fontFamily: typography.bold,
    color: '#FFFFFF',
    fontSize: 14,
  },
});
