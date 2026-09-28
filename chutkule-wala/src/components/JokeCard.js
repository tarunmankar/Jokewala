import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Share, StyleSheet, Linking, ToastAndroid, Platform, Alert } from 'react-native';
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
    const supported = await Linking.canOpenURL(url).catch(() => false);
    if (supported) {
      await Linking.openURL(url);
    } else {
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
    <View style={[styles.card, { backgroundColor: colors.card, borderColor: colors.border }]}>
      {/* Header Tag / Category & Speaking Indicator */}
      <View style={styles.headerRow}>
        <View style={[styles.categoryTag, { backgroundColor: colors.primaryLight }]}>
          <Text style={[styles.categoryText, { color: colors.primary }]}>
            {meta.emoji} {meta.name}
          </Text>
        </View>

        {isSpeaking ? (
          <View style={[styles.speakingBadge, { backgroundColor: '#FEE2E2' }]}>
            <Ionicons name="volume-high" size={14} color="#EF4444" />
            <Text style={styles.speakingText}>Bol raha hai...</Text>
          </View>
        ) : joke.subcategory ? (
          <Text style={[styles.subcatText, { color: colors.textMuted }]}>
            {joke.subcategory}
          </Text>
        ) : null}
      </View>

      {/* Joke Text with Dynamic Zoom Font Size */}
      <Text
        style={[
          styles.text,
          {
            color: colors.text,
            fontSize: currentFont.size,
            lineHeight: currentFont.lineHeight,
          },
        ]}
      >
        {joke.text}
      </Text>

      {/* Action Buttons: Like, Sunao, Copy, WhatsApp, Share */}
      <View style={[styles.actionsRow, { borderTopColor: colors.border }]}>
        {/* Like */}
        <TouchableOpacity
          style={styles.actionBtn}
          onPress={() => onToggleFav(joke)}
          activeOpacity={0.7}
        >
          <Ionicons
            name={joke.is_favorite ? 'heart' : 'heart-outline'}
            size={19}
            color={joke.is_favorite ? colors.heart : colors.textMuted}
          />
          <Text
            style={[
              styles.btnLabel,
              { color: joke.is_favorite ? colors.heart : colors.textMuted },
            ]}
          >
            {joke.is_favorite ? 'Liked' : 'Like'}
          </Text>
        </TouchableOpacity>

        {/* Sunao / Voice TTS */}
        <TouchableOpacity
          style={styles.actionBtn}
          onPress={() => speakJoke(joke.id, joke.text)}
          activeOpacity={0.7}
        >
          <Ionicons
            name={isSpeaking ? 'stop-circle' : 'volume-medium-outline'}
            size={19}
            color={isSpeaking ? '#EF4444' : colors.primary}
          />
          <Text
            style={[
              styles.btnLabel,
              { color: isSpeaking ? '#EF4444' : colors.primary, fontWeight: '600' },
            ]}
          >
            {isSpeaking ? 'Ruko' : 'Sunao'}
          </Text>
        </TouchableOpacity>

        {/* Copy */}
        <TouchableOpacity style={styles.actionBtn} onPress={copyJoke} activeOpacity={0.7}>
          <Ionicons
            name={copied ? 'checkmark-circle' : 'copy-outline'}
            size={18}
            color={copied ? '#10B981' : colors.textMuted}
          />
          <Text style={[styles.btnLabel, { color: copied ? '#10B981' : colors.textMuted }]}>
            {copied ? 'Copied' : 'Copy'}
          </Text>
        </TouchableOpacity>

        {/* WhatsApp */}
        <TouchableOpacity style={styles.actionBtn} onPress={shareOnWhatsApp} activeOpacity={0.7}>
          <Ionicons name="logo-whatsapp" size={18} color="#25D366" />
          <Text style={[styles.btnLabel, { color: '#25D366', fontWeight: '600' }]}>
            WhatsApp
          </Text>
        </TouchableOpacity>

        {/* System Share */}
        <TouchableOpacity style={styles.actionBtn} onPress={shareJoke} activeOpacity={0.7}>
          <Ionicons name="share-social-outline" size={18} color={colors.textMuted} />
          <Text style={[styles.btnLabel, { color: colors.textMuted }]}>Share</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderRadius: 16,
    padding: 16,
    marginHorizontal: 16,
    marginVertical: 7,
    borderWidth: 1,
    elevation: 2,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.06,
    shadowRadius: 6,
  },
  headerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  categoryTag: {
    paddingHorizontal: 10,
    paddingVertical: 3,
    borderRadius: 12,
  },
  categoryText: {
    fontFamily: typography.bold,
    fontSize: 12,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  speakingBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 10,
  },
  speakingText: {
    fontFamily: typography.medium,
    fontSize: 11,
    color: '#EF4444',
  },
  subcatText: {
    fontFamily: typography.regular,
    fontSize: 12,
  },
  text: {
    fontFamily: typography.regular,
    marginBottom: 14,
  },
  actionsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderTopWidth: 1,
    paddingTop: 10,
  },
  actionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
    paddingVertical: 4,
    paddingHorizontal: 3,
  },
  btnLabel: {
    fontFamily: typography.medium,
    fontSize: 11.5,
  },
});

