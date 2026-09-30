# Jokewala: Hindi Jokes Chutkule

Jokewala is a production-ready React Native (Expo) mobile application and curated open humor dataset delivering authentic Hindi and Hinglish comedy.

## 📱 Mobile Application
- **App Name:** Jokewala: Hindi Jokes Chutkule
- **Package:** `com.tarunmankar.jokewala`
- **Framework:** React Native (Expo SDK 57), React 19, SQLite local storage, Text-to-Speech audio voice playback.
- **Publishing Guide:** [`PLAY_STORE_PUBLISHING_GUIDE.md`](file:///d:/my-apps/Jokewala/PLAY_STORE_PUBLISHING_GUIDE.md)
- **Privacy Policy:** [`PRIVACY_POLICY.md`](file:///d:/my-apps/Jokewala/PRIVACY_POLICY.md)

### Running the App
```bash
# Start Expo development server
npx expo start

# Run on Android emulator or connected device
npx expo start --android

# Build production Android App Bundle (AAB) for Play Store
eas build -p android --profile production
```

## 🧪 Automated Quality Testing
To run the automated 28-point comprehensive test suite:
```bash
python tests/test_runner.py
```
Test results and verification ledger: [`tests/TEST_REPORT.md`](file:///d:/my-apps/Jokewala/tests/TEST_REPORT.md)

## 📂 Dataset Location
The complete, categorized dataset is located in [`hinglish-jokes-dataset/`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/):
- [`README.md`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/README.md) - Complete documentation, taxonomy, schema, and methodology.
- [`categories.json`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/categories.json) - 46 categorized taxonomy entries with metadata and counts.
- [`jokes-master.json`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/jokes-master.json) - Master dataset with research attribution, URLs, and safety flags.
- [`exports/`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/exports/) - Production-ready lightweight exports (`all-jokes.json`, `clean-jokes.json`, `jokes.csv`, `categories.json`).
- [`sources/`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/sources/) - Source registry ([`sources.csv`](file:///d:/my-apps/Jokewala/hinglish-jokes-dataset/sources/sources.csv)).
