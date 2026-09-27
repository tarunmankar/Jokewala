# Jokewala: Hinglish & Hindi Jokes Dataset

A curated, clean, categorized dataset of short Hindi and Hinglish jokes collected through structured internet research.

Designed specifically for mobile humor applications, chatbots, entertainment platforms, and content recommendation engines.

---

## 1. Project Purpose
The goal of this dataset is to build an authentic, verifiable collection of circulating Indian jokes in Roman-script Hinglish and Hindi without generating synthetic or fake content. Every joke in this repository originates from publicly accessible online sources, with full attribution, source tracking, and duplicate filtering.

---

## 2. Directory Structure

```text
hinglish-jokes-dataset/
├── README.md                           # This comprehensive guide
├── categories.json                     # Categories metadata with IDs, names, emojis, descriptions, counts
├── jokes-master.json                   # Complete master dataset with research metadata and source links
│
├── 01-one-liners/                      # Category 01: One-liner punchy jokes
├── 02-husband-wife/                    # Category 02: Pati-patni jokes
├── 03-boyfriend-girlfriend/            # Category 03: Dating & relationship humor
├── 04-teacher-student/                 # Category 04: Classroom & exam wit
├── 05-school-college/                  # Category 05: College masti & canteen life
├── 06-friends/                         # Category 06: Dosti & buddy roasts
├── 07-family/                          # Category 07: Desi joint family dynamics
├── 08-mom-dad/                         # Category 08: Mummy-papa parenting & flying chappals
├── 09-brother-sister/                  # Category 09: Sibling rivalry & remote fights
├── 10-office-work/                     # Category 10: Corporate routines & appraisals
├── 11-boss-employee/                   # Category 11: Boss-subordinate humor & leaves
├── 12-doctor-patient/                  # Category 12: Medical clinic comedy & symptoms
├── 13-engineer/                        # Category 13: Engineering life & jugaad
├── 14-programmer-tech/                 # Category 14: Coding, bugs, and IT life
├── 15-mobile-internet/                 # Category 15: Battery panic, slow WiFi, data packs
├── 16-social-media/                    # Category 16: Reels, selfies, algorithms & vanity
├── 17-whatsapp/                        # Category 17: Family groups, forwards & blue ticks
├── 18-shopping/                        # Category 18: Bargaining, discounts & free dhaniya
├── 19-money/                           # Category 19: Budgeting, borrowing & empty wallets
├── 20-middle-class/                    # Category 20: Desi middle-class habits & frugality
├── 21-desi-life/                       # Category 21: Quintessential Indian daily experiences
├── 22-marriage/                        # Category 22: Shaadi season, rishtey & wedding food
├── 23-single-life/                     # Category 23: Singlehood & Valentine survival
├── 24-love-dating/                     # Category 24: Crushes, dating fails & romance
├── 25-food/                            # Category 25: Chai love, street food & diet breaks
├── 26-fitness-gym/                     # Category 26: Gym memberships & sore muscles
├── 27-travel/                          # Category 27: Train journeys, packing & vacations
├── 28-driving-traffic/                 # Category 28: Indian traffic, honking & autos
├── 29-exam-study/                      # Category 29: Hall tickets & last-night revisions
├── 30-pappu-style/                     # Category 30: Classic innocent Pappu jokes
├── 31-santa-banta-style/               # Category 31: Folklore duo humor
├── 32-question-answer/                 # Category 32: Witty Q&A riddles & quick quips
├── 33-wordplay/                        # Category 33: Bilingual English-Hindi wordplay
├── 34-puns/                            # Category 34: Puns and phonetic double takes
├── 35-sarcasm/                         # Category 35: Dry wit and biting comebacks
├── 36-dad-jokes/                       # Category 36: Wholesome eye-roll dad humor
├── 37-clean-family-friendly/           # Category 37: 100% wholesome family humor
├── 38-festival/                        # Category 38: Diwali, Holi, and soan papdi humor
├── 39-cricket/                         # Category 39: Gully cricket & IPL enthusiasm
├── 40-bollywood-pop-culture/           # Category 40: Filmy dialogues & Bollywood parodies
├── 41-daily-life/                      # Category 41: Morning routines & small absurdities
├── 42-relatable/                       # Category 42: Hyper-relatable life situations
├── 43-kids/                            # Category 43: Innocent child logic & questions
├── 44-adult-clean/                     # Category 44: Adult life (aging, bills, fatigue) kept clean
├── 45-other/                           # Category 45: Miscellaneous humor
│
├── sources/
│   ├── sources.csv                     # Tabular index of all researched URLs
│   └── source-summary.md               # Detailed source descriptions & domain breakdown
│
├── exports/
│   ├── all-jokes.json                  # App-ready lightweight JSON containing all jokes
│   ├── clean-jokes.json                # Filtered app-ready JSON containing only clean jokes
│   ├── jokes.csv                       # Export for tabular / data science workflows
│   └── categories.json                 # Categories list with live counts
│
├── reports/
│   └── dataset-report.md               # Statistical report (counts, formats, languages)
│
├── research-log/
│   └── progress.md                     # Running log of queries, progress, and checklist
│
└── scripts/
    └── dataset_manager.py              # Automation script for ingestion, deduplication & exports
```

---

## 3. Schemas

### Master Schema (`jokes-master.json`)
```json
{
  "id": "HJ-000001",
  "category": "teacher-student",
  "subcategory": "homework",
  "language": "hinglish",
  "format": "dialogue",
  "content": "Teacher: Homework kyu nahi kiya?\nStudent: Sir, homework bhi Sunday mana raha tha.",
  "clean": true,
  "safety_tags": ["clean"],
  "source_id": "SRC-0001",
  "source_name": "Navbharat Times",
  "source_url": "https://navbharattimes.indiatimes.com/...",
  "date_accessed": "2026-09-27",
  "source_status": "verified",
  "duplicate_group": null,
  "popularity_signal": null,
  "tags": ["teacher-student", "homework", "classroom"],
  "notes": ""
}
```

### App-Ready Schema (`exports/all-jokes.json` & `exports/clean-jokes.json`)
```json
{
  "id": "HJ-000001",
  "category": "teacher-student",
  "subcategory": "homework",
  "joke": "Teacher: Homework kyu nahi kiya?\nStudent: Sir, homework bhi Sunday mana raha tha.",
  "language": "hinglish",
  "format": "dialogue",
  "clean": true
}
```

---

## 4. Source & Verification Methodology
- **Search Queries**: Targeted searches per category across Indian news websites (Navbharat Times, Dainik Bhaskar, Amar Ujala, Hindustan, Times of India), humor archives (SantaBanta, HindiJokes, JokesInHindi, ShayariBazar), and lifestyle portals (ScoopWhoop, MensXP, Storypick).
- **Zero Fabrication**: Only authentic, publicly retrievable URLs are documented. No placeholders or invented sources are ever used.
- **Traceability**: Every joke record maps to a specific `source_id` in `sources/sources.csv`.

---

## 5. Duplicate Detection & Quality Assurance
1. **Normalization**: Texts are stripped of emojis, converted to lowercase, cleaned of extraneous punctuation and whitespace.
2. **Phonetic & Romanization Mapping**: Common variations in Hinglish transliteration (*kyun* vs *kyu*, *nahin* vs *nahi*, *kahan* vs *kaha*, *hain* vs *hai*, *masterji* vs *teacher*) are unified before comparison.
3. **Similarity Threshold**: Exact duplicates and high-similarity variants (Jaccard similarity >= 0.82) are automatically rejected to ensure freshness.
4. **Length Constraint**: Kept short (1–6 lines), suitable for mobile screens and quick reads.

---

## 6. Safety & Content Tagging
- `clean`: Suitable for all family audiences and general mobile app distribution.
- `mild`: Contains gentle relationship banter or light drinking/mischief references.
- `sensitive`: Contains mature themes, tracked separately to prevent inadvertent display in child-safe modes.

---

## 7. Known Limitations
- Niche categories (e.g. dad jokes, fitness, puns) have fewer unique entries circulating organically in Indian Hindi/Hinglish spaces compared to evergreen staples like teacher-student or husband-wife.
- In accordance with the project guidelines, missing counts are NEVER fabricated. Categories reflect genuine discovered volume.
