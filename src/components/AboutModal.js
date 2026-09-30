import React from 'react';
import {
  Modal,
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  Image,
  Share,
  Linking,
  ScrollView,
  TouchableWithoutFeedback,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { typography } from '../theme';

export default function AboutModal({ visible, onClose, colors }) {
  const handleShareApp = async () => {
    try {
      await Share.share({
        message:
          'हंसी और ठहाकों का खजाना! 😂 Jokewala App डाउनलोड करें और 1,300+ मजेदार हिंदी जोक्स और चुटकुले पढ़ें व सुनें: https://play.google.com/store/apps/details?id=com.tarunmankar.jokewala',
      });
    } catch (e) {
      console.log('Share error:', e);
    }
  };

  return (
    <Modal
      visible={visible}
      transparent
      animationType="fade"
      onRequestClose={onClose}
    >
      <TouchableWithoutFeedback onPress={onClose}>
        <View style={styles.overlay}>
          <TouchableWithoutFeedback>
            <View style={[styles.dialog, { backgroundColor: colors.card, borderColor: colors.border }]}>
              {/* Header Close Button */}
              <TouchableOpacity
                style={styles.closeBtn}
                onPress={onClose}
                hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
              >
                <Ionicons name="close-circle" size={26} color={colors.textMuted} />
              </TouchableOpacity>

              <ScrollView
                showsVerticalScrollIndicator={false}
                contentContainerStyle={styles.scrollContent}
              >
                {/* App Brand Icon */}
                <View style={[styles.iconWrapper, { backgroundColor: colors.primaryLight }]}>
                  <Image
                    source={require('../../assets/icon.png')}
                    style={styles.appIcon}
                  />
                </View>

                {/* App Name & Version */}
                <Text style={[styles.appName, { color: colors.text }]}>
                  Jokewala
                </Text>
                <Text style={[styles.appSubtitle, { color: colors.primary }]}>
                  Hindi Jokes & Chutkule
                </Text>

                <View style={[styles.versionBadge, { backgroundColor: colors.cardSecondary }]}>
                  <Text style={[styles.versionText, { color: colors.textSecondary }]}>
                    Version 1.0.0
                  </Text>
                </View>

                {/* Developer Info Box */}
                <View style={[styles.devBox, { backgroundColor: colors.primaryLight, borderColor: colors.borderLight }]}>
                  <View style={styles.devRow}>
                    <Ionicons name="code-slash" size={17} color={colors.primary} />
                    <Text style={[styles.devTitle, { color: colors.text }]}>
                      Developed by
                    </Text>
                  </View>
                  <Text style={[styles.devName, { color: colors.primary }]}>
                    Tarun Mankar
                  </Text>
                  <Text style={[styles.madeWithLove, { color: colors.textSecondary }]}>
                    Made with ❤️ in India
                  </Text>
                </View>

                {/* Features List */}
                <View style={styles.featuresList}>
                  <View style={styles.featureItem}>
                    <Ionicons name="sparkles" size={15} color={colors.gold} />
                    <Text style={[styles.featureText, { color: colors.textSecondary }]}>
                      1,338+ हाथ से चुने गए शुद्ध देसी चुटकले
                    </Text>
                  </View>
                  <View style={styles.featureItem}>
                    <Ionicons name="volume-medium" size={15} color={colors.speaker} />
                    <Text style={[styles.featureText, { color: colors.textSecondary }]}>
                      आवाज में जोक सुनने की सुविधा (Audio Reader)
                    </Text>
                  </View>
                  <View style={styles.featureItem}>
                    <Ionicons name="logo-whatsapp" size={15} color={colors.whatsapp} />
                    <Text style={[styles.featureText, { color: colors.textSecondary }]}>
                      1-क्लिक व्हाट्सएप स्टेटस व चैट शेयरिंग
                    </Text>
                  </View>
                  <View style={styles.featureItem}>
                    <Ionicons name="shield-checkmark" size={15} color={colors.copy} />
                    <Text style={[styles.featureText, { color: colors.textSecondary }]}>
                      100% फैमिली-फ्रेंडली व सुरक्षित सामग्री
                    </Text>
                  </View>
                </View>

                {/* Action Buttons */}
                <View style={styles.actions}>
                  <TouchableOpacity
                    style={[styles.shareAppBtn, { backgroundColor: colors.primary }]}
                    onPress={handleShareApp}
                    activeOpacity={0.8}
                  >
                    <Ionicons name="share-social" size={18} color="#FFFFFF" />
                    <Text style={styles.shareAppText}>दोस्तों के साथ शेयर करें</Text>
                  </TouchableOpacity>

                  <TouchableOpacity
                    style={[styles.doneBtn, { backgroundColor: colors.cardSecondary, borderColor: colors.border }]}
                    onPress={onClose}
                    activeOpacity={0.7}
                  >
                    <Text style={[styles.doneBtnText, { color: colors.text }]}>बंद करें</Text>
                  </TouchableOpacity>
                </View>
              </ScrollView>
            </View>
          </TouchableWithoutFeedback>
        </View>
      </TouchableWithoutFeedback>
    </Modal>
  );
}

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.55)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  dialog: {
    width: '100%',
    maxWidth: 380,
    maxHeight: '85%',
    borderRadius: 24,
    borderWidth: 1,
    overflow: 'hidden',
    elevation: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.3,
    shadowRadius: 16,
  },
  closeBtn: {
    position: 'absolute',
    top: 14,
    right: 14,
    zIndex: 10,
  },
  scrollContent: {
    padding: 24,
    alignItems: 'center',
  },
  iconWrapper: {
    width: 72,
    height: 72,
    borderRadius: 20,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 12,
    overflow: 'hidden',
  },
  appIcon: {
    width: 68,
    height: 68,
    borderRadius: 18,
  },
  appName: {
    fontFamily: typography.bold,
    fontSize: 22,
    marginBottom: 2,
  },
  appSubtitle: {
    fontFamily: typography.medium,
    fontSize: 14,
    marginBottom: 8,
  },
  versionBadge: {
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
    marginBottom: 16,
  },
  versionText: {
    fontFamily: typography.medium,
    fontSize: 12,
  },
  devBox: {
    width: '100%',
    padding: 14,
    borderRadius: 16,
    borderWidth: 1,
    alignItems: 'center',
    marginBottom: 16,
  },
  devRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 3,
  },
  devTitle: {
    fontFamily: typography.medium,
    fontSize: 12.5,
  },
  devName: {
    fontFamily: typography.bold,
    fontSize: 17,
    letterSpacing: 0.3,
    marginBottom: 2,
  },
  madeWithLove: {
    fontFamily: typography.regular,
    fontSize: 12,
  },
  featuresList: {
    width: '100%',
    gap: 9,
    marginBottom: 20,
  },
  featureItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  featureText: {
    fontFamily: typography.regular,
    fontSize: 12.5,
    flex: 1,
  },
  actions: {
    width: '100%',
    gap: 10,
  },
  shareAppBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 12,
    borderRadius: 20,
  },
  shareAppText: {
    fontFamily: typography.bold,
    color: '#FFFFFF',
    fontSize: 14,
  },
  doneBtn: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 11,
    borderRadius: 20,
    borderWidth: 1,
  },
  doneBtnText: {
    fontFamily: typography.medium,
    fontSize: 13.5,
  },
});
