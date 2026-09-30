import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  Share,
  StyleSheet,
  Linking,
  ToastAndroid,
  Platform,
  Alert,
} from 'react-native';
import * as Clipboard from 'expo-clipboard';
import { Ionicons } from '@expo/vector-icons';
import { typography } from '../theme';
import { getCategoryMeta } from '../db/database';
import { useApp } from '../context/AppContext';

export default function JokeCard({ joke, onToggleFav, colors }) {
  const [copied, setCopied] = useState(false);
  const { currentFont, activeSpeakingId, speakJoke } = useApp();
  const isSpeaking = activeSpeakingId === joke.id;
  const meta = getCategoryMeta(joke.category);

  const shareText = `${joke.text}\n\n😂 Haso aur hasao! Jokewala App se`;

  const shareJoke = async () => {
    try {
      await Share.share({
        message: shareText,
      });
    } catch (error) {
      console.log('Share error:', error);
    }
  };

  const shareOnWhatsApp = async () => {
    const url = `whatsapp://send?text=${encodeURIComponent(shareText)}`;
    try {
      await Linking.openURL(url);
    } catch {
      // If WhatsApp is not installed or scheme fails, fallback to system share
      shareJoke();
    }
  };

  const copyJoke = async () => {
    await Clipboard.setStringAsync(joke.text);
    setCopied(true);
    if (Platform.OS === 'android') {
      ToastAndroid.show('Joke copy ho gaya! 🎉', ToastAndroid.SHORT);
    } else {
      Alert.alert('Copied!', 'Joke clipboard me copy ho gaya 🎉');
    }
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <View
      style={[
        styles.card,
        {
          backgroundColor: colors.card,
          borderColor: colors.border,
        },
      ]}
    >
      {/* Top Accent Strip */}
      <View style={[styles.accentStrip, { backgroundColor: colors.primaryLight }]} />

      {/* Header Row: Category Badge & Status */}
      <View style={styles.headerRow}>
        <View style={[styles.categoryTag, { backgroundColor: colors.primaryLight }]}>
          <Text style={[styles.categoryEmoji]}>{meta.emoji}</Text>
          <Text style={[styles.categoryText, { color: colors.primary }]}>{meta.name}</Text>
        </View>

        {isSpeaking ? (
          <View style={[styles.speakingBadge, { backgroundColor: colors.heartBg }]}>
            <Ionicons name="volume-high" size={13} color={colors.heart} />
            <Text style={[styles.speakingText, { color: colors.heart }]}>Bol raha hai...</Text>
          </View>
        ) : joke.subcategory ? (
          <View style={[styles.subcatBadge, { backgroundColor: colors.cardSecondary }]}>
            <Text style={[styles.subcatText, { color: colors.textSecondary }]}>
              {joke.subcategory}
            </Text>
          </View>
        ) : null}
      </View>

      {/* Joke Text Content */}
      <Text
        style={[
          styles.jokeText,
          {
            color: colors.text,
            fontSize: currentFont.size,
            lineHeight: currentFont.lineHeight,
          },
        ]}
      >
        {joke.text}
      </Text>

      {/* Divider */}
      <View style={[styles.divider, { backgroundColor: colors.borderLight }]} />

      {/* Modern Action Bar */}
      <View style={styles.actionsRow}>
        {/* Like */}
        <TouchableOpacity
          style={[
            styles.actionBtn,
            joke.is_favorite && { backgroundColor: colors.heartBg },
          ]}
          onPress={() => onToggleFav(joke)}
          activeOpacity={0.65}
        >
          <Ionicons
            name={joke.is_favorite ? 'heart' : 'heart-outline'}
            size={18}
            color={joke.is_favorite ? colors.heart : colors.textMuted}
          />
          <Text
            style={[
              styles.btnLabel,
              { color: joke.is_favorite ? colors.heart : colors.textSecondary },
              joke.is_favorite && { fontFamily: typography.bold },
            ]}
          >
            {joke.is_favorite ? 'Liked' : 'Like'}
          </Text>
        </TouchableOpacity>

        {/* Voice Sunao (TTS) */}
        <TouchableOpacity
          style={[
            styles.actionBtn,
            isSpeaking
              ? { backgroundColor: colors.heartBg }
              : { backgroundColor: colors.speakerBg },
          ]}
          onPress={() => speakJoke(joke.id, joke.text)}
          activeOpacity={0.65}
        >
          <Ionicons
            name={isSpeaking ? 'stop-circle' : 'volume-medium'}
            size={18}
            color={isSpeaking ? colors.heart : colors.speaker}
          />
          <Text
            style={[
              styles.btnLabel,
              { color: isSpeaking ? colors.heart : colors.speaker },
              { fontFamily: typography.bold },
            ]}
          >
            {isSpeaking ? 'Ruko' : 'Sunao'}
          </Text>
        </TouchableOpacity>

        {/* Copy */}
        <TouchableOpacity
          style={[
            styles.actionBtn,
            copied && { backgroundColor: colors.copyBg },
          ]}
          onPress={copyJoke}
          activeOpacity={0.65}
        >
          <Ionicons
            name={copied ? 'checkmark-circle' : 'copy-outline'}
            size={17}
            color={copied ? colors.copy : colors.textMuted}
          />
          <Text
            style={[
              styles.btnLabel,
              { color: copied ? colors.copy : colors.textSecondary },
              copied && { fontFamily: typography.bold },
            ]}
          >
            {copied ? 'Copied' : 'Copy'}
          </Text>
        </TouchableOpacity>

        {/* WhatsApp Share */}
        <TouchableOpacity
          style={[styles.actionBtn, { backgroundColor: colors.whatsappBg }]}
          onPress={shareOnWhatsApp}
          activeOpacity={0.65}
        >
          <Ionicons name="logo-whatsapp" size={17} color={colors.whatsapp} />
          <Text
            style={[
              styles.btnLabel,
              { color: colors.whatsapp, fontFamily: typography.bold },
            ]}
          >
            Share
          </Text>
        </TouchableOpacity>

        {/* More Share */}
        <TouchableOpacity
          style={styles.actionBtnIconOnly}
          onPress={shareJoke}
          activeOpacity={0.65}
        >
          <Ionicons name="share-social-outline" size={18} color={colors.textMuted} />
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderRadius: 20,
    padding: 18,
    marginHorizontal: 16,
    marginVertical: 8,
    borderWidth: 1,
    overflow: 'hidden',
    // Elevated drop shadow
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.07,
    shadowRadius: 10,
    elevation: 3,
  },
  accentStrip: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    height: 3,
  },
  headerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  categoryTag: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 14,
  },
  categoryEmoji: {
    fontSize: 13,
  },
  categoryText: {
    fontFamily: typography.bold,
    fontSize: 11.5,
    letterSpacing: 0.3,
  },
  subcatBadge: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
  },
  subcatText: {
    fontFamily: typography.medium,
    fontSize: 11,
  },
  speakingBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
  },
  speakingText: {
    fontFamily: typography.bold,
    fontSize: 11,
  },
  jokeText: {
    fontFamily: typography.regular,
    marginBottom: 14,
    letterSpacing: 0.2,
  },
  divider: {
    height: 1,
    marginBottom: 10,
  },
  actionsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  actionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingVertical: 6,
    paddingHorizontal: 10,
    borderRadius: 12,
  },
  actionBtnIconOnly: {
    paddingVertical: 6,
    paddingHorizontal: 8,
    borderRadius: 12,
  },
  btnLabel: {
    fontFamily: typography.medium,
    fontSize: 12,
  },
});
