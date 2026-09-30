import React, { createContext, useContext, useState, useEffect } from 'react';
import * as Speech from 'expo-speech';

const AppContext = createContext();

export const FONT_SIZES = [
  { label: 'A', size: 15, lineHeight: 25, name: 'Normal' },
  { label: 'A+', size: 18, lineHeight: 30, name: 'Medium' },
  { label: 'A++', size: 22, lineHeight: 36, name: 'Large' },
];

export function AppProvider({ children }) {
  const [fontIndex, setFontIndex] = useState(1); // default Medium (18px)
  const [activeSpeakingId, setActiveSpeakingId] = useState(null);

  const currentFont = FONT_SIZES[fontIndex];

  const cycleFontSize = () => {
    setFontIndex((prev) => (prev + 1) % FONT_SIZES.length);
  };

  const speakJoke = async (id, text) => {
    try {
      if (activeSpeakingId === id) {
        await Speech.stop();
        setActiveSpeakingId(null);
        return;
      }

      await Speech.stop();
      setActiveSpeakingId(id);

      Speech.speak(text, {
        language: 'hi-IN',
        pitch: 1.0,
        rate: 0.95,
        onDone: () => setActiveSpeakingId(null),
        onError: () => setActiveSpeakingId(null),
        onStopped: () => setActiveSpeakingId(null),
      });
    } catch (e) {
      console.log('Speech error:', e);
      setActiveSpeakingId(null);
    }
  };

  const stopSpeaking = async () => {
    try {
      await Speech.stop();
      setActiveSpeakingId(null);
    } catch (e) {
      // ignore
    }
  };

  useEffect(() => {
    return () => {
      Speech.stop().catch(() => {});
    };
  }, []);

  return (
    <AppContext.Provider
      value={{
        currentFont,
        cycleFontSize,
        fontIndex,
        activeSpeakingId,
        speakJoke,
        stopSpeaking,
      }}
    >
      {children}
    </AppContext.Provider>
  );
}

export const useApp = () => useContext(AppContext);
