import React, { useEffect, useState, useCallback } from 'react';
import { View, useColorScheme, StatusBar, TouchableOpacity, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import * as SplashScreen from 'expo-splash-screen';
import {
  useFonts,
  NotoSansDevanagari_400Regular,
  NotoSansDevanagari_500Medium,
  NotoSansDevanagari_700Bold,
} from '@expo-google-fonts/noto-sans-devanagari';
import { Ionicons } from '@expo/vector-icons';

import { initDB } from './src/db/database';
import { lightColors, darkColors, typography } from './src/theme';
import { AppProvider, useApp } from './src/context/AppContext';
import HomeScreen from './src/screens/HomeScreen';
import SearchScreen from './src/screens/SearchScreen';
import FavoritesScreen from './src/screens/FavoritesScreen';

// Keep the splash screen visible while loading resources
SplashScreen.preventAutoHideAsync().catch(() => {});

const Tab = createBottomTabNavigator();

function FontZoomButton({ colors }) {
  const { currentFont, cycleFontSize } = useApp();
  return (
    <TouchableOpacity
      onPress={cycleFontSize}
      activeOpacity={0.7}
      style={{
        marginRight: 16,
        paddingHorizontal: 12,
        paddingVertical: 6,
        borderRadius: 16,
        backgroundColor: colors.primaryLight,
        flexDirection: 'row',
        alignItems: 'center',
        gap: 5,
        borderWidth: 1,
        borderColor: colors.borderLight,
      }}
    >
      <Ionicons name="text" size={13} color={colors.primary} />
      <Text style={{ fontFamily: typography.bold, fontSize: 12.5, color: colors.primary }}>
        {currentFont.label}
      </Text>
    </TouchableOpacity>
  );
}

export default function App() {
  const systemScheme = useColorScheme();
  const colors = systemScheme === 'dark' ? darkColors : lightColors;

  const [dbReady, setDbReady] = useState(false);

  const [fontsLoaded] = useFonts({
    NotoSansDevanagari_400Regular,
    NotoSansDevanagari_500Medium,
    NotoSansDevanagari_700Bold,
  });

  useEffect(() => {
    async function prepare() {
      try {
        await initDB();
        setDbReady(true);
      } catch (e) {
        console.warn('Initialization error:', e);
        setDbReady(true);
      }
    }
    prepare();
  }, []);

  const onLayoutRootView = useCallback(async () => {
    if (fontsLoaded && dbReady) {
      await SplashScreen.hideAsync().catch(() => {});
    }
  }, [fontsLoaded, dbReady]);

  if (!fontsLoaded || !dbReady) {
    return null;
  }

  return (
    <AppProvider>
      <View style={{ flex: 1, backgroundColor: colors.bg }} onLayout={onLayoutRootView}>
        <StatusBar
          barStyle={systemScheme === 'dark' ? 'light-content' : 'dark-content'}
          backgroundColor={colors.card}
        />
        <NavigationContainer>
          <Tab.Navigator
            screenOptions={({ route }) => ({
              headerStyle: {
                backgroundColor: colors.card,
                elevation: 0,
                shadowOpacity: 0,
                borderBottomWidth: 1,
                borderBottomColor: colors.border,
              },
              headerTitleStyle: {
                fontFamily: typography.bold,
                fontSize: 20,
                color: colors.text,
              },
              headerRight: () => <FontZoomButton colors={colors} />,
            tabBarStyle: {
              backgroundColor: colors.card,
              borderTopColor: colors.border,
              height: 60,
              paddingBottom: 8,
              paddingTop: 6,
            },
            tabBarLabelStyle: {
              fontFamily: typography.medium,
              fontSize: 12,
            },
            tabBarActiveTintColor: colors.primary,
            tabBarInactiveTintColor: colors.textMuted,
            tabBarIcon: ({ focused, color, size }) => {
              let iconName;
              if (route.name === 'HomeTab') {
                iconName = focused ? 'home' : 'home-outline';
              } else if (route.name === 'SearchTab') {
                iconName = focused ? 'search' : 'search-outline';
              } else if (route.name === 'FavoritesTab') {
                iconName = focused ? 'heart' : 'heart-outline';
              }
              return <Ionicons name={iconName} size={size} color={color} />;
            },
          })}
        >
          <Tab.Screen
            name="HomeTab"
            options={{
              title: 'Jokewala',
              tabBarLabel: 'Home',
            }}
          >
            {(props) => <HomeScreen {...props} colors={colors} />}
          </Tab.Screen>

          <Tab.Screen
            name="SearchTab"
            options={{
              title: 'खोजें',
              tabBarLabel: 'Search',
            }}
          >
            {(props) => <SearchScreen {...props} colors={colors} />}
          </Tab.Screen>

          <Tab.Screen
            name="FavoritesTab"
            options={{
              title: 'पसंदीदा',
              tabBarLabel: 'Favorites',
            }}
          >
            {(props) => <FavoritesScreen {...props} colors={colors} />}
          </Tab.Screen>
        </Tab.Navigator>
      </NavigationContainer>
      </View>
    </AppProvider>
  );
}
