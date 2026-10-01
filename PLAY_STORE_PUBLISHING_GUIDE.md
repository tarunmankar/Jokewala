# 🚀 Google Play Store Publishing Guide - Jokewala: Hindi Jokes Chutkule

यह गाइड **Jokewala (com.tarunmankar.jokewala)** ऐप को Google Play Console पर शुरू से लेकर अंत तक पब्लिश करने के लिए बनाई गई है। इसमें हर एक फॉर्म, पॉलिसी और सेटिंग्स में क्या भरना है, साथ ही ऐप के सभी ग्राफ़िक्स एसेट्स (Icon, Feature Graphic, Screenshots) के लिए **AI Image Prompts** दिए गए हैं।

---

## 📑 विषय-सूची (Table of Contents)
1. [स्टेप 0: जरूरी तैयारी (Prerequisites & AAB Build)](#स्टेप-0-जरूरी-तैयारी-prerequisites--aab-build)
2. [स्टेप 1: नया ऐप बनाएँ (Create App)](#स्टेप-1-नया-ऐप-बनाएँ-create-app)
3. [स्टेप 2: स्टोर लिस्टिंग विवरण (Store Listing Details)](#स्टेप-2-स्टोर-लिस्टिंग-विवरण-store-listing-details)
4. [स्टेप 3: ऐप कंटेंट और पॉलिसी फॉर्म्स (App Content & Policy - सबसे महत्वपूर्ण)](#स्टेप-3-ऐप-कंटेन्ट-और-पॉलिसी-फॉर्म्स-app-content--policy)
5. [स्टेप 4: स्टोर सेटिंग्स और संपर्क जानकारी (Store Settings)](#स्टेप-4-स्टोर-सेटिंग्स-और-संपर्क-जानकारी-store-settings)
6. [स्टेप 5: ऐप रिलीज और टेस्टिंग (App Release & Testing Track)](#स्टेप-5-ऐप-रिलीज-और-टेस्टिंग-app-release--testing-track)
7. [🎨 AI Image Prompts (Icon, Feature Graphic & Screenshots)](#-ai-image-prompts-icon-feature-graphic--screenshots)

---

## स्टेप 0: जरूरी तैयारी (Prerequisites & AAB Build)

### 1. Google Play Console Account
- Google Play Console अकाउंट ($25 वन-टाइम रजिस्ट्रेशन फीस)।
- पहचान सत्यापन (Identity Verification) और पता सत्यापन (Address Verification) पूरा होना चाहिए।
> **⚠️ जरूरी नोट (Google Policy):** यदि आपका पर्सनल डेवलपर अकाउंट 13 नवंबर 2023 के बाद बना है, तो प्रोडक्शन रिलीज से पहले **20 टेस्टर के साथ 14 दिन का Closed Testing** अनिवार्य है।

### 2. AAB (Android App Bundle) फाइल तैयार करना
Play Store पर अब `.apk` नहीं, बल्कि `.aab` फाइल अपलोड होती है।
Expo प्रोजेक्ट में AAB बनाने के लिए:

```bash
# EAS CLI इंस्टॉल करें (यदि पहले से नहीं है)
npm install -g eas-cli

# EAS लॉगिन करें
eas login

# प्रोडक्शन AAB बिल्ड करें
eas build -p android --profile production
```
बिल्ड पूरा होने पर आपको `.aab` डाउनलोड करने का लिंक मिलेगा।

---

## स्टेप 1: नया ऐप बनाएँ (Create App)

Google Play Console में **"Create App"** बटन पर क्लिक करें और निम्नलिखित भरें:

| फ़ील्ड का नाम | क्या भरना / चुनना है |
|---|---|
| **App Name** | `Jokewala: Hindi Jokes Chutkule` |
| **Default Language** | `English (United States)` *(Recommended)* |
| **App or Game** | `App` चुनें |
| **Free or Paid** | `Free` चुनें |
| **Declarations** | दोनों चेकबॉक्स टिक करें:<br>✅ Developer Program Policies<br>✅ US export laws |

क्लिक करें: **Create app**.

---

## स्टेप 2: स्टोर लिस्टिंग विवरण (Store Listing Details - English Metadata)

Play Console के बाएं मेन्यू में **Grow > Store presence > Main store listing** पर जाएँ।

### 1. टेक्स्ट डिटेल्स (English SEO Optimized)

#### **App name (अधिकतम 30 अक्षर):**
```text
Jokewala: Hindi Jokes Chutkule
```
*(अक्षर: ठीक 30 | ASO के दो सबसे बड़े सर्च कीवर्ड्स: "Hindi Jokes" + "Chutkule")*

#### **Short description (अधिकतम 80 अक्षर):**
```text
Funny Hindi jokes, desi chutkule, hilarious comedy and laughter!
```
*(अक्षर: ठीक 65 | इसमें "Hindi jokes", "chutkule", "comedy", "laughter" सभी मुख्य कीवर्ड्स शामिल हैं)*

#### **Full description (अधिकतम 4000 अक्षर):**
*(नीचे दिया गया पूरा इंग्लिश ASO टेक्स्ट कॉपी-पेस्ट करें)*
```markdown
Looking for non-stop laughter and daily desi comedy? Welcome to Jokewala, your ultimate destination for hilarious Hindi jokes, viral chutkule, and witty desi humor! 😂🎉

Whether you want to lighten your mood after a tiring day or share laughter in WhatsApp group chats, Jokewala brings you thousands of handpicked, clean, and rib-tickling Hindi and Hinglish jokes across 45+ trending categories.

🌟 KEY FEATURES:

• 🎙️ Text-to-Speech Audio Jokes (Listen & Laugh):
Too lazy to read? Tap the "Listen" button and let the app read aloud the funniest Hindi jokes with high-quality voice playback!

• 🚀 1-Click WhatsApp & Social Share:
Instantly share your favorite chutkule and comedy messages to WhatsApp status, WhatsApp chats, Instagram, and Facebook with a single click.

• 📋 Quick Copy to Clipboard:
Easily copy any joke to your clipboard and paste it anywhere in seconds.

• 📂 45+ Hilarious Categories:
- Santa Banta Jokes
- Husband & Wife (Pati Patni) Humor
- Teacher & Student Classroom Comedy
- Office & Boss Funny Banter
- Name Jokes & Trending Desi Roasts
- Friendship & College Masti
- Bollywood & Meme Humor
- Short Funny One-Liners

• 📴 100% Offline App (No Internet Needed):
No mobile data or Wi-Fi? No problem! Jokewala works completely offline with lightning-fast performance anytime, anywhere.

• ❤️ Save Your Favorites:
Bookmark the jokes that made you laugh the hardest and revisit them whenever you need a quick giggle.

• 🌙 Eye-Friendly Dark & Light Modes:
Switch between a sleek dark theme and clean light theme for comfortable reading day or night.

• 🛡️ 100% Family-Friendly & Clean Humor:
Enjoy wholesome desi comedy suitable for sharing with family, relatives, colleagues, and friends.

Download Jokewala: Hindi Jokes Chutkule today and start spreading smiles and non-stop laughter! 😆✨
```

---

## स्टेप 3: ऐप कंटेंट और पॉलिसी फॉर्म्स (App Content & Policy)

Play Console के बाएं मेन्यू में नीचे **Policy and programs > App content** पर जाएँ। यहाँ निम्नलिखित टास्क एक-एक करके भरें:

### 1. Privacy Policy (गोपनीयता नीति)
- **URL दर्ज करें**: एक सार्वजनिक वेब पेज का लिंक जहाँ प्राइवेसी पॉलिसी हो।
- *टिप:* आप GitHub Pages, Google Sites, Notion या free privacy policy generator पर होस्ट कर सकते हैं।
- **URL उदाहरण**: `https://tarunmankar.github.io/jokewala/privacy-policy.html`
- *नोट:* Jokewala में कोई डेटा कलेक्ट नहीं होता, पॉलिसी में स्पष्ट रखें: "Jokewala does not collect, store, or share any personal user data. All data is stored locally on device."

### 2. App Access (ऐप एक्सेस)
- विकल्प चुनें: **"All functionality is available without special access"** (क्योंकि ऐप में कोई लॉगिन/पासवर्ड या रेस्ट्रिक्टेड एरिया नहीं है).
- **Save** करें.

### 3. Ads (विज्ञापन)
- क्या आपके ऐप में विज्ञापन हैं?
- चुनें: **"No, my app does not contain ads"** (वर्तमान कोडबेस में कोई एडमॉब/ऐड्स नहीं हैं).
- **Save** करें.

### 4. Content Rating (कंटेंट रेटिंग - IARC प्रश्नावली)
**Start questionnaire** पर क्लिक करें:
1. **Email address**: अपना ईमेल डालें।
2. **Category**: चुनें **"All Other App Types"** या **"Entertainment"**.
3. प्रश्नों के उत्तर:
   - **Violence (हिंसा)**: `No`
   - **Sexuality / Nudity**: `No`
   - **Language (गाली-गलौज/अपशब्द)**: `No`
   - **Controlled Substance (शराब/ड्रग्स)**: `No`
   - **Miscellaneous**:
     - Does the app natively allow users to interact or exchange content? `No`
     - Does the app share current physical location? `No`
     - Does the app allow purchasing digital goods? `No`
4. **Summary**: रेटिंग आएगी `Everyone` / `PEGI 3`.
5. **Save** और **Submit** करें.

### 5. Target Audience and Content (लक्षित दर्शक)
- **Target age groups**: चुनें **`13-15`**, **`16-17`**, **`18 and over`**
  > **⚠️ महत्वपूर्ण सलाह:** `Under 13` (जैसे 9-12, 5 and under) **बिल्कुल न चुनें**, वरना Google की कड़ी 'Designed for Families' और COPPA पॉलिसी लागू हो जाएगी और रिव्यू में रिजेक्शन के चांस बढ़ जाते हैं।
- **Appeal to children**:
  - प्रश्न: "Could your store listing unintentionally appeal to children?"
  - उत्तर: **`No`**.
- **Save** करें.

### 6. News Apps (समाचार ऐप)
- प्रश्न: "Is your app a news app?"
- उत्तर: **`No`**.
- **Save** करें.

### 7. COVID-19 Contact Tracing and Status Apps
- उत्तर: चुनें **"My app is not a publicly available COVID-19 contact tracing or status app"**.
- **Save** करें.

### 8. Data Safety (डेटा सुरक्षा - सबसे महत्वपूर्ण सेक्शन)
प्रश्नावली शुरू करें:
1. **Data collection and security**:
   - Does your app collect or share any of the required user data types? 👉 **`No`**
2. **Is all user data collected by your app encrypted in transit?** 👉 N/A (क्योंकि डेटा कलेक्ट नहीं होता)
3. **Do you provide a way for users to request that their data be deleted?** 👉 **`No`** (क्योंकि कोई यूजर डेटा या अकाउंट सिस्टम नहीं है)
4. रिव्यू स्क्रीन पर चेक करें कि "No data collected" आ रहा है।
5. **Save** करें.

### 9. Government Apps (सरकारी ऐप)
- प्रश्न: "Is your app developed by or on behalf of a government?"
- उत्तर: **`No`**.
- **Save** करें.

### 10. Financial Features (वित्तीय सुविधाएं)
- उत्तर: **"My app does not provide any financial features"**.
- **Save** करें.

### 11. Health Apps (स्वास्थ्य ऐप)
- उत्तर: **"My app does not provide any health-related features"**.
- **Save** करें.

---

## स्टेप 4: स्टोर सेटिंग्स और संपर्क जानकारी (Store Settings)

Play Console में **Grow > Store presence > Store settings** पर जाएँ:

| सेटिंग | मान |
|---|---|
| **App Category** | `Entertainment` (मनोरंजन) |
| **Tags** | Manage tags पर क्लिक करें और चुनें: `Entertainment`, `Humor`, `Comics` |
| **Email Address** | आपका सपोर्ट ईमेल (यह यूजर्स को Play Store पर दिखेगा) |
| **Phone Number** | खाली छोड़ सकते हैं (Optional) |
| **Website** | अपनी वेबसाइट या GitHub प्रोफाइल URL (Optional) |
| **External Marketing** | Checkbox टिक रखें |

---

## स्टेप 5: ऐप रिलीज और टेस्टिंग (App Release & Testing Track)

### व्यक्तिगत खातों (Personal Accounts) के लिए:
1. **Testing > Closed testing** पर जाएँ.
2. एक नया ट्रैक बनाएँ: **"Closed testing - Alpha"**.
3. **Testers** टैब में 20 ईमेल आईडी (Gmail IDs) की लिस्ट जोड़ें.
4. **Create new release** पर क्लिक करें.
5. अपनी तैयार की हुई `.aab` फाइल अपलोड करें.
6. **Release name**: `1.0.0 (Initial Release)`
7. **Release notes**:
   ```text
   Initial release of Jokewala: Hindi Jokes Chutkule! Enjoy thousands of hilarious Hindi jokes and viral chutkule with text-to-speech audio voice reading, offline access, and instant 1-click WhatsApp sharing.
   ```
8. **Save** और **Review release** पर क्लिक करें और टेस्टिंग के लिए रोलआउट करें.
9. 14 दिन के सफल टेस्टिंग के बाद **Production** ट्रैक में अप्लाई करने का विकल्प अनलॉक हो जाएगा.

---

## 🎨 AI Image Prompts (Icon, Feature Graphic & Screenshots)

आप इन प्रॉम्ट्स को सीधे **Midjourney, DALL-E 3 (ChatGPT), Bing Image Creator, Flux.1, या Leonardo.ai** में डालकर इमेज जनरेट कर सकते हैं।

---

### 1. App Icon Prompts (साइज़: 512 x 512 px)
> **Google Play नियम:** 512x512 PNG, 32-bit color, पारदर्शी (transparent) बैकग्राउंड न हो, कोई ऐप स्टोर बैज न हो।

#### 🌟 विकल्प A: 3D Pixar/Disney स्टाइल कैरेक्टर (Recommended - सबसे ज्यादा आकर्षक)
```text
3D app icon of a cheerful Indian young man character laughing hysterically with tears of joy, wide comic smile, expressive eyes, modern stylized cartoon character, vibrant saffron-orange (#FF8A00) gradient background, soft studio rim lighting, 3D clay render, Pixar and Disney animated style, smooth glossy finish, minimalist clean rounded squircle badge, centered composition, high resolution, 8k, mobile app icon --no text, no watermark, no blur
```

#### 🌟 विकल्प B: मॉडर्न फ्लैट वेक्टर / मिनिमलिस्टिक इमोजी मास्कॉट
```text
Modern minimalist app icon for comedy jokes app named Jokewala, bold happy laughing emoji face with desi Indian mustache, sunglasses with cheerful reflection, warm yellow and bright orange gradient background, clean vector illustration, sharp edges, Apple iOS and Material You style, eye-catching, simple, high contrast, app icon design --no realistic photos, no blurry edges
```

#### 🌟 विकल्प C: कॉमेडी माइक और लाफ्टर बर्स्ट
```text
Playful 3D app icon featuring a vintage silver microphone wearing cool sunglasses and laughing with a huge smile, surrounded by colorful pop-art laugh bubbles (Haha, LOL), rich golden-orange and deep purple gradient background, 3D isometric render, vibrant colors, premium glossy texture, mobile icon template --v 6.0
```

---

### 2. Feature Graphic Prompts (साइज़: 1024 x 500 px)
> **Google Play नियम:** 1024x500 PNG या JPEG (24-bit). केंद्र में मुख्य कंटेंट रखें ताकि किनारों पर कटने का खतरा न रहे।

#### 🌟 विकल्प A: वाइब्रेंट देसी कॉमेडी स्टेज और कैरेक्टर (Widescreen Banner)
```text
Widescreen mobile app feature graphic banner, 1024x500 aspect ratio, vibrant Indian stand-up comedy theme, center-left has an adorable 3D cartoon young Indian comic performer holding a microphone laughing heartily, cheerful audience silhouettes, glowing stage neon lights, floating colorful 3D emojis (rolling on the floor laughing, tears of joy), warm energetic orange, magenta and deep violet ambient lighting, ample clean copy space on the right side for typography, high-end 3D cinema 4d render, festive fun atmosphere --ar 1024:500 --no text, no letters
```

#### 🌟 विकल्प B: पॉप-आर्ट और कॉमिक बुक देसी मस्ती थीम
```text
Wide horizontal banner for a Hindi comedy app, modern Indian pop-art comic illustration, vibrant yellow and tangerine orange background with halftone dots and dynamic sunburst rays, cute expressive Indian cartoon characters bursting into laughter, speech bubbles with comic shapes, cheerful fiesta confetti, modern flat design with bold outlines, clean layout with negative space in middle for logo, 1024x500 banner --ar 1024:500
```

#### 🌟 विकल्प C: ग्लासमोर्फिज्म और फ्लोटिंग 3D एलिमेंट्स (Clean & Modern)
```text
Sleek modern 1024x500 Play Store feature graphic background, warm golden-orange and royal purple smooth gradient, floating translucent 3D laughing emojis, comedy theater masks, microphone with golden accents, subtle festive bokeh, premium clean corporate aesthetic with creative comedic energy, wide horizontal composition --ar 1024:500 --no text
```

---

### 3. Screenshots (Phone Screenshots - 1080 x 1920 या 1080 x 2400 px)
> **Google Play नियम:** न्यूनतम 2 स्क्रीनशॉट, अधिकतम 8। रेकमेंडेड: 4 स्क्रीनशॉट। ऊपर आकर्षक हिंदी हेडलाइन और नीचे ऐप का स्क्रीनशॉट।

स्क्रीनशॉट तैयार करने के लिए आप **Canva**, **Figma**, या **AppMockUp.com** का उपयोग करके नीचे दिए गए टाइटल्स और बैकग्राउंड्स के साथ मॉकअप बना सकते हैं:

#### 📱 स्क्रीनशॉट 1: होम स्क्रीन (Category Overview)
- **Top Caption / Banner Text**:
  - `45+ मजेदार श्रेणियां 🎭`
  - `हर मूड के लिए चुटकुले!`
- **Visual Prompt for Mockup Background**:
  ```text
  Minimalist mobile mockup background, clean modern soft pastel orange and white abstract backdrop, floating subtle 3D emoji spheres, vertical portrait 9:16 orientation, high aesthetic marketing banner template for smartphone showcase --ar 9:16
  ```

#### 📱 स्क्रीनशॉट 2: जोक्स कार्ड और ऑडियो फीचर (Audio Reader)
- **Top Caption / Banner Text**:
  - `सुनो और लोटपोट हो जाओ! 🎙️`
  - `बोलकर सुनाने वाला ऑडियो फीचर`
- **Visual Focus**: Jokewala ऐप का जोक्स स्क्रीन जिसमें "Listen / बोलें" और "Next" बटन हाइलाइट हों।

#### 📱 स्क्रीनशॉट 3: 1-क्लिक व्हाट्सएप शेयर
- **Top Caption / Banner Text**:
  - `दोस्तों को हँसाओ एक क्लिक में! 📲`
  - `सीधे WhatsApp पर शेयर करें`
- **Visual Focus**: जोक कार्ड के नीचे WhatsApp का हरा शेयर बटन चमकता हुआ।

#### 📱 स्क्रीनशॉट 4: 100% ऑफलाइन मोड
- **Top Caption / Banner Text**:
  - `बिना इंटरनेट कभी भी, कहीं भी! 📴`
  - `सुपरफास्ट और 100% फ्री`
- **Visual Focus**: बिना इंटरनेट तुरंत खुलने वाला और तेज चलने वाला ऑफलाइन इंटरफ़ेस।

---

## 🚀 क्विक चेकलिस्ट (Publishing Ready Checklist)
- [ ] 512x512 App Icon तैयार किया
- [ ] 1024x500 Feature Graphic तैयार किया
- [ ] कम से कम 4 फोन स्क्रीनशॉट्स (1080x1920) तैयार किए
- [ ] `eas build -p android --profile production` से `.aab` फाइल डाउनलोड की
- [ ] Privacy Policy URL लाइव किया
- [ ] Data Safety में "No Data Collected" भरा
- [ ] 20 टेस्टर्स के साथ Closed Testing शुरू की
