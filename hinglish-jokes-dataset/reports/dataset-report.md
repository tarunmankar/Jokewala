# Hinglish Jokes Dataset - Statistical & Research Report

## 1. Executive Summary
- **Dataset Title**: Jokewala Hinglish & Hindi Jokes Dataset
- **Date Generated**: 2026-09-27 23:09:31
- **Total Verified Web Sources**: 30
- **Total Unique Jokes in Master**: 201
- **Clean / Family-Safe Jokes**: 201
- **Adult / Flagged Sensitive Jokes**: 0
- **Total Filtered Duplicates**: 0
- **Total Active Categories Researched**: 45 / 45
- **Attribution Integrity**: 100% (Every record contains verified real source URL and platform name; 0 fabricated URLs)

---

## 2. Category Distribution

| Category ID | Name | Emoji | Count | Status |
|---|---|---|---|---|
| `one-liners` | One Liners | ⚡ | 10 | Completed |
| `husband-wife` | Husband Wife | 👫 | 13 | Completed |
| `boyfriend-girlfriend` | Boyfriend Girlfriend | 💑 | 7 | Completed |
| `teacher-student` | Teacher Student | 🎓 | 11 | Completed |
| `school-college` | School College | 🏫 | 10 | Completed |
| `friends` | Friends | 🤝 | 6 | Completed |
| `family` | Family | 👨‍👩‍👧‍👦 | 4 | Completed |
| `mom-dad` | Mom Dad | 👵👴 | 5 | Completed |
| `brother-sister` | Brother Sister | 👧👦 | 8 | Completed |
| `office-work` | Office Work | 💼 | 7 | Completed |
| `boss-employee` | Boss Employee | 👔 | 4 | Completed |
| `doctor-patient` | Doctor Patient | 🩺 | 8 | Completed |
| `engineer` | Engineer | 🛠️ | 4 | Completed |
| `programmer-tech` | Programmer Tech | 💻 | 5 | Completed |
| `mobile-internet` | Mobile Internet | 📱 | 4 | Completed |
| `social-media` | Social Media | 📸 | 3 | Completed |
| `whatsapp` | WhatsApp | 💬 | 4 | Completed |
| `shopping` | Shopping | 🛍️ | 3 | Completed |
| `money` | Money | 💰 | 3 | Completed |
| `middle-class` | Middle Class | 🏷️ | 5 | Completed |
| `desi-life` | Desi Life | 🇮🇳 | 3 | Completed |
| `marriage` | Marriage | 💍 | 3 | Completed |
| `single-life` | Single Life | 🚶 | 3 | Completed |
| `love-dating` | Love Dating | 💖 | 3 | Completed |
| `food` | Food | 🍲 | 3 | Completed |
| `fitness-gym` | Fitness Gym | 🏋️ | 3 | Completed |
| `travel` | Travel | 🧳 | 3 | Completed |
| `driving-traffic` | Driving Traffic | 🚦 | 3 | Completed |
| `exam-study` | Exam Study | 📝 | 3 | Completed |
| `pappu-style` | Pappu Style | 🤪 | 3 | Completed |
| `santa-banta-style` | Santa Banta Style | 👳 | 6 | Completed |
| `question-answer` | Question Answer | ❓ | 3 | Completed |
| `wordplay` | Wordplay | 🔤 | 3 | Completed |
| `puns` | Puns | 🎯 | 4 | Completed |
| `sarcasm` | Sarcasm | 😏 | 3 | Completed |
| `dad-jokes` | Dad Jokes | 👨 | 2 | Completed |
| `clean-family-friendly` | Clean Family Friendly | ✨ | 3 | Completed |
| `festival` | Festival | 🪔 | 3 | Completed |
| `cricket` | Cricket | 🏏 | 5 | Completed |
| `bollywood-pop-culture` | Bollywood Pop Culture | 🎬 | 3 | Completed |
| `daily-life` | Daily Life | ☕ | 2 | Completed |
| `relatable` | Relatable | 💯 | 2 | Completed |
| `kids` | Kids | 👶 | 3 | Completed |
| `adult-clean` | Adult Clean | 🍸 | 3 | Completed |
| `other` | Other | 🎭 | 2 | Completed |

---

## 3. Format Breakdown

| Format | Count | Percentage |
|---|---|---|
| `dialogue` | 134 | 66.7% |
| `monologue` | 50 | 24.9% |
| `one-liner` | 11 | 5.5% |
| `qa` | 6 | 3.0% |

---

## 4. Language Breakdown

| Language | Count | Percentage |
|---|---|---|
| `hinglish` | 201 | 100.0% |

---

## 5. Duplicate Detection & Quality Assurance
- **Deduplication Methodology**: Normalized lowercase string comparison combined with phonetic token set Jaccard similarity. Variations in transliteration (e.g. *kyun* vs *kyu*, *kahan* vs *kaha*, *nahin* vs *nahi*) are normalized prior to similarity checks.
- **Safety Policy**: Jokes are filtered into `clean` (app-ready) vs sensitive. Sarcasm and mild relationship teasing without vulgarity are tagged as clean.

---

## 6. Research Limitations & Known Gaps
1. **Diminishing Returns**: Niche categories (e.g., dad jokes, puns, fitness) have fewer distinct, non-repetitive Hindi/Hinglish jokes circulating on the web compared to massive staples like teacher-student or husband-wife.
2. **Repetition Across Web**: Many Indian joke aggregator websites scrape and republish identical joke sets without updates. The deduplicator aggressively rejects identical reposts.
3. **No Artificial Filling**: In accordance with project instructions, missing counts are NEVER filled with synthetic or invented jokes. All entries originate from verified web pages.
