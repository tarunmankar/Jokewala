# -*- coding: utf-8 -*-
"""
High-quality Hindi (Devanagari) to colloquial Hinglish (Roman script) converter
Designed specifically for Indian humor, jokes, and dialogues.
"""

import re
import json

COMMON_WORDS = {
    # Pronouns & Questions
    "मैं": "main", "मुझे": "mujhe", "मुझसे": "mujhse", "मेरा": "mera", "मेरी": "meri", "मेरे": "mere",
    "तुम": "tum", "तुम्हें": "tumhe", "तुमसे": "tumse", "तुम्हारा": "tumhara", "तुम्हारी": "tumhari", "तुम्हारे": "tumhare",
    "आप": "aap", "आपको": "aapko", "आपसे": "aapse", "आपका": "aapka", "आपकी": "aapki", "आपके": "aapke",
    "वह": "woh", "वो": "woh", "उसने": "usne", "उसे": "use", "उसको": "usko", "उससे": "usse", "उसका": "uska", "उसकी": "uski", "उसके": "uske",
    "वे": "ve", "उन्होंने": "unhone", "उन्हें": "unhe", "उनको": "unko", "उनसे": "unse", "उनका": "unka", "उनकी": "unki", "उनके": "unke",
    "यह": "yeh", "ये": "yeh", "इसने": "isne", "इसे": "ise", "इसको": "isko", "इससे": "isse", "इसका": "iska", "इसकी": "iski", "इसके": "iske",
    "हम": "hum", "हमने": "humne", "हमें": "humein", "हमको": "humko", "हमसे": "humse", "हमारा": "hamara", "हमारी": "hamari", "हमारे": "hamare",
    "क्या": "kya", "क्यों": "kyu", "क्यो": "kyu", "कैसे": "kaise", "कैसा": "kaisa", "कैसी": "kaisi",
    "कब": "kab", "कहाँ": "kaha", "कहा": "kaha", "किधर": "kidhar", "किसने": "kisne", "किसे": "kise", "किसको": "kisko",
    "कौन": "kaun", "कितना": "kitna", "कितने": "kitne", "कितनी": "kitni",

    # Conjunctions & Prepositions
    "और": "aur", "या": "ya", "लेकिन": "lekin", "पर": "par", "मगर": "magar", "किंतु": "kintu", "परंतु": "parantu",
    "कि": "ki", "तो": "toh", "भी": "bhi", "ही": "hi", "तक": "tak", "से": "se", "में": "mein", "पे": "pe", "को": "ko",
    "का": "ka", "की": "ki", "के": "ke", "ने": "ne", "लिए": "liye", "बिना": "bina", "साथ": "saath", "पास": "paas",

    # Auxiliaries & Verbs
    "है": "hai", "हैं": "hain", "हो": "ho", "हूँ": "hoon", "हूं": "hoon",
    "था": "tha", "थी": "thi", "थे": "the",
    "नहीं": "nahi", "न": "na", "ना": "na", "मत": "mat",
    "कहा": "kaha", "बोला": "bola", "बोली": "boli", "बोले": "bole",
    "पूछा": "pucha", "पूछी": "puchi", "पूछे": "puche",
    "दिया": "diya", "दी": "dee", "दिए": "diye", "दे": "de", "दो": "do", "देना": "dena",
    "लिया": "liya", "ली": "lee", "लिए": "liye", "ले": "le", "लो": "lo", "लेना": "lena",
    "किया": "kiya", "की": "kee", "किए": "kiye", "कर": "kar", "करो": "karo", "करना": "karna", "करते": "karte", "करती": "karti", "करता": "karta",
    "गया": "gaya", "गई": "gayi", "गए": "gaye", "जा": "jaa", "जाओ": "jao", "जाना": "jaana", "जाता": "jaata", "जाती": "jaati", "जाते": "jaate",
    "आया": "aaya", "आई": "aayi", "आए": "aaye", "आ": "aa", "आओ": "aao", "आना": "aana", "आता": "aata", "आती": "aati", "आते": "aate",
    "रहा": "raha", "रही": "rahi", "रहे": "rahe", "रहना": "rahna",
    "सकता": "sakta", "सकती": "sakti", "सकते": "sakte", "सका": "saka", "सकी": "saki",
    "चाहिए": "chahiye", "होगा": "hoga", "होगी": "hogi", "होंगे": "honge",
    "बनाया": "banaya", "बना": "bana", "बनाओ": "banao", "बताया": "bataya", "बताओ": "batao",
    "सुना": "suna", "सुनो": "suno", "सुनाओ": "sunao",
    "देखा": "dekha", "देखो": "dekho", "देख": "dekh",
    "सोचा": "socha", "सोचो": "socho", "सोच": "soch",
    "हंसा": "hansa", "हंसी": "hansi", "हंसते": "hanste",

    # Joke Character Roles & Titles
    "पति": "Pati", "पत्नी": "Patni", "बीवी": "Biwi", "पति-पत्नी": "Pati-Patni",
    "सास": "Saas", "ससुर": "Sasur", "दामाद": "Damad", "बहू": "Bahu",
    "संता": "Santa", "बंता": "Banta",
    "पप्पू": "Pappu", "संजू": "Sanju",
    "टीचर": "Teacher", "मास्टर": "Master", "मास्टरजी": "Masterji", "मैडम": "Madam",
    "छात्र": "Student", "बच्चा": "Baccha", "बच्चे": "Bacche",
    "डॉक्टर": "Doctor", "डॉ": "Dr.", "मरीज": "Mareez", "पेशेंट": "Patient",
    "लड़का": "Ladka", "लड़का": "Ladka", "लड़की": "Ladki", "लड़की": "Ladki",
    "दोस्त": "Dost", "यार": "Yaar", "मित्र": "Mitra",
    "बाप": "Baap", "बेटा": "Beta", "पिता": "Pita", "माता": "Mata", "पापा": "Papa", "मम्मी": "Mummy",
    "भाई": "Bhai", "बहन": "Behen",
    "ग्राहक": "Grahak", "दुकानदार": "Dukandar",
    "बॉस": "Boss", "कर्मचारी": "Employee", "चपरासी": "Chaprasi",
    "शराबी": "Sharabi", "पुलिस": "Police", "चोर": "Chor",
    "पंडित": "Pandit", "पंडितजी": "Panditji", "जज": "Judge", "वकील": "Vakeel",
    "भिखारी": "Bhikhari",

    # Common Joke Nouns & Adjectives
    "एक": "Ek", "दो": "Do", "तीन": "Teen", "चार": "Chaar", "पांच": "Paanch",
    "बार": "baar", "दिन": "din", "रात": "raat", "सुबह": "subah", "शाम": "shaam",
    "घर": "ghar", "स्कूल": "school", "कॉलेज": "college", "क्लास": "class",
    "हॉस्पिटल": "hospital", "दुकान": "dukaan", "होटल": "hotel",
    "गाड़ी": "gaadi", "गाड़ी": "gaadi", "कार": "car", "बस": "bus", "ट्रेन": "train",
    "शादी": "shaadi", "विवाह": "vivah", "दुल्हन": "dulhan", "दूल्हा": "dulha",
    "पैसा": "paisa", "पैसे": "paise", "रुपए": "rupaye", "रुपया": "rupaya",
    "बात": "baat", "जवाब": "jawab", "सवाल": "sawal", "प्रश्न": "prashna", "उत्तर": "uttar",
    "खाना": "khana", "रोटी": "roti", "पानी": "paani", "चाय": "chai", "दूध": "doodh",
    "शराब": "sharab", "दारू": "daaru",
    "मोबाइल": "mobile", "फोन": "phone", "व्हाट्सएप": "WhatsApp", "फेसबुक": "Facebook",
    "अच्छा": "accha", "अच्छी": "acchi", "अच्छे": "acche",
    "बुरा": "bura", "बुरी": "buri", "बुरे": "bure",
    "बड़ा": "bada", "बड़ी": "badi", "बड़े": "bade",
    "छोटा": "chhota", "छोटी": "chhoti", "छोटे": "chhote",
    "नया": "naya", "नई": "nayi", "नए": "naye",
    "पुराना": "purana", "पुरानी": "purani", "पुराने": "purane",
    "बहुत": "bahut", "ज्यादा": "zyada", "कम": "kam", "थोड़ा": "thoda", "थोड़ी": "thodi",
    "आज": "aaj", "कल": "kal", "परसों": "parso", "रोज": "roz", "हमेशा": "hamesha",
    "कभी": "kabhi", "अभी": "abhi", "तभी": "tabhi", "जब": "jab", "तब": "tab",
    "यहाँ": "yahan", "वहाँ": "wahan", "कहाँ": "kahan", "जहाँ": "jahan",
    "अगर": "agar", "सच्ची": "sacchi", "झूठ": "jhooth", "पागल": "pagal",
    "खुश": "khush", "गुस्सा": "gussa", "मजाक": "mazaak", "चुटकुला": "chutkula",
    # Loan words & common terms in jokes
    "ऑफिस": "office", "टाइम": "time", "मूवी": "movie", "बैंक": "bank", "बोर्ड": "board",
    "लोन": "loan", "टॉयलेट": "toilet", "टूथब्रश": "toothbrush", "साफ": "saaf", "पेपर": "paper",
    "वाइफ": "wife", "हस्बैंड": "husband", "हसबैंड": "husband", "मोरल": "moral", "पार्टी": "party",
    "डॉक्टर": "Doctor", "पुलिस": "police", "बस": "bus", "ट्रेन": "train", "स्टेशन": "station",
    "टिकट": "ticket", "कॉलेज": "college", "स्कूल": "school", "क्लास": "class", "टीचर": "Teacher",
    "मैडम": "Madam", "सर": "Sir", "फोन": "phone", "मोबाइल": "mobile", "मैसेज": "message",
    "व्हाट्सएप": "WhatsApp", "फेसबुक": "Facebook", "इंटरनेट": "internet", "बर्थडे": "birthday",
    "सरदार": "Sardar", "सपना": "sapna", "सोने": "sone", "कमाल": "kamaal", "दरवाजे": "darwaje",
    "दरवाजा": "darwaza", "दरवजा": "darwaza", "चुनाव": "chunav", "चिन्ह": "chinh", "स्वागत": "swagat",
    "केजरीवाल": "Kejriwal", "बीजेपी": "BJP", "कांग्रेस": "Congress", "पड़ोसी": "padosi", "पड़ोसी": "padosi",
    "मस्ती": "masti", "तबला": "tabla", "बजाता": "bajata", "बजाती": "bajati", "बजाते": "bajate",
    "पंगा": "panga", "चिल्लाता": "chillata", "चिल्लाती": "chillati", "चिल्लाना": "chillana",
    "बेवकूफ": "bewakoof", "औरत": "aurat", "आदमी": "aadmi", "जोर": "zor", "हंसते": "hanste"
}

VOWELS = {
    'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo',
    'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
    'अं': 'an', 'अः': 'ah', 'ऑ': 'o', 'ऍ': 'e', 'ऎ': 'e', 'ऒ': 'o'
}

MATRAS = {
    'ा': 'a', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo',
    'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au',
    'ॉ': 'o', 'ॅ': 'e', '्': ''
}

CONSONANTS = {
    'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng',
    'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny',
    'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
    'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
    'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm',
    'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v',
    'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h',
    'क्ष': 'ksh', 'त्र': 'tra', 'ज्ञ': 'gya',
    'क़': 'q', 'ख़': 'kh', 'ग़': 'g', 'ज़': 'z', 'ड़': 'd', 'ढ़': 'dh', 'फ़': 'f',
    'क़': 'q', 'ख़': 'kh', 'ग़': 'g', 'ज़': 'z', 'ड़': 'd', 'ढ़': 'dh', 'फ़': 'f', 'य़': 'y'
}

DIGITS = {
    '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
    '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
}

PUNCTUATION_MAP = {
    '।': '.', '॥': '.', '“': '"', '”': '"', '‘': "'", '’': "'",
    'ः': ':', '़': '', '॑': '', '॒': '', '॓': '', '॔': ''
}

def transliterate_word(word):
    punct_prefix = ""
    punct_suffix = ""

    for d_hi, d_ar in DIGITS.items():
        word = word.replace(d_hi, d_ar)

    # Strip leading/trailing punctuation without stripping Devanagari matras
    m_p = re.match(r'^([^a-zA-Z0-9\u0900-\u097f]+)', word)
    if m_p:
        punct_prefix = m_p.group(1)
        word = word[len(punct_prefix):]
    m_s = re.search(r'([^a-zA-Z0-9\u0900-\u097f]+)$', word)
    if m_s:
        punct_suffix = m_s.group(1)
        word = word[:-len(punct_suffix)]

    if not word:
        return punct_prefix + punct_suffix

    if word in COMMON_WORDS:
        return punct_prefix + COMMON_WORDS[word] + punct_suffix
    if word.lower() in COMMON_WORDS:
        return punct_prefix + COMMON_WORDS[word.lower()] + punct_suffix

    if not any('\u0900' <= c <= '\u097f' for c in word):
        return punct_prefix + word + punct_suffix

    n = len(word)
    out = []
    i = 0
    while i < n:
        c = word[i]

        if i + 1 < n and word[i+1] == '़':
            nukta_char = c + '़'
            if nukta_char in CONSONANTS:
                base = CONSONANTS[nukta_char]
                i += 2
                if i < n and word[i] in MATRAS:
                    out.append(base + MATRAS[word[i]])
                    i += 1
                else:
                    out.append(base + ('a' if i < n and word[i] not in [' ', '\n', '।'] else ''))
                continue

        if c in VOWELS:
            out.append(VOWELS[c])
            i += 1
            continue

        if c in CONSONANTS:
            base = CONSONANTS[c]
            i += 1
            if i < n and word[i] == '्':
                out.append(base)
                i += 1
            elif i < n and word[i] in MATRAS:
                matra_str = MATRAS[word[i]]
                i += 1
                if i < n and word[i] in ['ं', 'ँ']:
                    matra_str += 'n'
                    i += 1
                out.append(base + matra_str)
            elif i < n and word[i] in ['ं', 'ँ']:
                out.append(base + 'an')
                i += 1
            else:
                if i >= n:
                    out.append(base)
                else:
                    out.append(base + 'a')
            continue

        if c in MATRAS:
            out.append(MATRAS[c])
            i += 1
            continue

        if c in ['ं', 'ँ']:
            out.append('n')
            i += 1
            continue

        out.append(PUNCTUATION_MAP.get(c, c))
        i += 1

    res = "".join(out)
    res = re.sub(r'aaa+', 'aa', res)
    res = re.sub(r'aee\b', 'aayi', res)
    res = re.sub(r'aao\b', 'aao', res)
    res = re.sub(r'ee\b', 'i', res)
    res = re.sub(r'oo\b', 'u', res)

    return punct_prefix + res + punct_suffix

def hindi_to_hinglish(text):
    lines = text.split("\n")
    converted_lines = []

    for line in lines:
        if not any('\u0900' <= c <= '\u097f' for c in line):
            converted_lines.append(line)
            continue

        tokens = re.split(r'(\s+|[:–\-])', line)
        line_out = []
        for token in tokens:
            if not token or token.isspace() or token in [":", "–", "-", "!", "?", ",", ".", "🤣", "😂", "😜"]:
                line_out.append(token)
            else:
                line_out.append(transliterate_word(token))
        
        c_line = "".join(line_out)
        c_line = re.sub(r'\bPatni:\b', 'Patni:', c_line)
        c_line = re.sub(r'\bPati:\b', 'Pati:', c_line)
        c_line = re.sub(r'\bTeacher:\b', 'Teacher:', c_line)
        c_line = re.sub(r'\bSanta:\b', 'Santa:', c_line)
        c_line = re.sub(r'\bBanta:\b', 'Banta:', c_line)
        c_line = re.sub(r'\bPappu:\b', 'Pappu:', c_line)
        c_line = re.sub(r'\bDoctor:\b', 'Doctor:', c_line)
        c_line = re.sub(r'\bMareez:\b', 'Mareez:', c_line)
        c_line = re.sub(r'\bEk baar\b', 'Ek baar', c_line)
        c_line = re.sub(r'\bArey\b', 'Arre', c_line)
        c_line = re.sub(r'\bNahin\b', 'Nahi', c_line)
        c_line = re.sub(r'\bHain\b', 'Hain', c_line)
        c_line = re.sub(r'\bHai\b', 'Hai', c_line)

        converted_lines.append(c_line)

    return "\n".join(converted_lines)

if __name__ == "__main__":
    sample = "पत्नी: चल तो रहे हो मायके, पर वहां लड़ना मत, वो मेरे पापा का घर है।\nपति: तो मेरे पापा का घर क्या 'कुरुक्षेत्र' है, जो रोज वहां महाभारत करती हो!"
    print("Original Hindi:\n" + sample)
    print("\nConverted Hinglish:\n" + hindi_to_hinglish(sample))
