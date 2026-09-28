# -*- coding: utf-8 -*-
"""
Curates clean, Google Play safe witty double-meaning / naughty Hinglish jokes
and assigns rich searchable keywords/tags across all jokes in jokes-master.json.
"""

import json
from dataset_manager import DatasetManager

# Curated high-engagement, clean double-meaning/naughty jokes (100% Google Play Safe, 0 abuses)
CLEAN_NAUGHTY_JOKES = [
    {
        "subcategory": "playful-banter",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Pati (romantic hokar): Aaj toh tum bilkul bijli ki nangi taar lag rahi ho! Patni: Kyu ji, chhoone ka mann kar raha hai? Pati: Nahi, chhoo liya toh 440 volt ka jhatka lag jayega aur aatma bhatakne lagegi! 😂",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "husband-wife", "pati-patni", "romantic", "masti", "biwi"],
        "notes": "Curated clean double-meaning romantic roast"
    },
    {
        "subcategory": "doctor-clinic",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Doctor (sundar ladki se): Khidki kholo aur thoda lamba-lamba saans lo... Ladki: Kyu doctor sahab, oxygen kam hai kya room me? Doctor: Nahi ji, mera cabin perfume khatam ho gaya tha, tumhara deo badiya hai! 😜",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "doctor", "flirt", "clinic", "masti"],
        "notes": "Curated clean clinic banter"
    },
    {
        "subcategory": "couple-romance",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Girlfriend: Jaanu, tum mere liye kya-kya kar sakte ho? Boyfriend: Main tere liye chaand-taare tod kar laa sakta hoon! Girlfriend: Taare nahi chahiye, Myntra aur Zara ki shopping cart clear kar do! Boyfriend: Arey pagli, taare todna zyada aasan tha! 🤣",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "couple", "boyfriend-girlfriend", "shopping", "romance", "bf-gf"],
        "notes": "Shopping vs romance banter"
    },
    {
        "subcategory": "wedding-night",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Suhaagraat pe Dulhan sharmaate hue boli: Suno ji, main ghunghat khud uthaoon ya aap uthaoge? Dulha: Pehle light off karo, mujhe neend aa rahi hai aur kal subah jaldi office nikalna hai! 🤦‍♂️",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "marriage", "shaadi", "suhaagraat", "husband-wife"],
        "notes": "Classic innocent wedding night twist"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Patni (sharma kar): Shaadi se pehle toh tum kehte the ki tumhe chaand jaisi biwi chahiye! Pati: Haan, par mujhe yeh thodi pata tha ki chaand ki tarah tumhara bhi roz naya roop dikhega aur din me dikhai hi nahi dogi! 🌙😂",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "biwi", "romance", "double-meaning"],
        "notes": "Playful moon metaphor"
    },
    {
        "subcategory": "couple-chat",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Ladka: Tumhara chehra dekh kar mere dil me aag lag jaati hai! Ladki (khush hokar): Sach me, kya main itni hot hoon? Ladka: Nahi, petrol pump jaisi lagti ho, zara si chingari se darr lagta hai! 🔥",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "boyfriend-girlfriend", "roast", "flirt"],
        "notes": "Playful roast"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Pati ne chupke se bedroom me perfume lagaya. Patni: Kiske liye itna mehak rahe ho? Pati: Khushboo khud ke sukoon ke liye hoti hai! Patni: Theek hai, ab jaao kitchen me aur bartan dho kar sukoon paao! 😂",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "biwi", "romance"],
        "notes": "Husband perfume domestic reality"
    },
    {
        "subcategory": "dating",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Pappu date pe gaya. Ladki: Tumhe meri kaun si aada sabse zyada pasand aayi? Pappu: Jab tum bill aate waqt phone pe achanak busy hone ki acting karti ho, wo aada lajawab hai! 💸🤣",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "dating", "pappu", "boyfriend-girlfriend", "bill"],
        "notes": "Date bill humor"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Patni: Agar main achanak gaayab ho jaun toh tumhara reaction kya hoga? Pati: Pehle toh 2 minute yakeen nahi hoga... fir main dhol wale ko bulaunga aur poore mohalle me laddoo baatunga! 🪘🥳",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "biwi", "double-meaning"],
        "notes": "Disappearance banter"
    },
    {
        "subcategory": "flirt",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Santa ek ladki se: Tumhara naam kya hai? Ladki: Preeti. Aur tumhara? Santa: Preetam. Ladki: Par main toh tumhe jaanti bhi nahi! Santa: Arey abhi Preeti-Preetam ho gaye, aage aage dekho kya hota hai! 😜",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "santa-banta", "flirt", "double-meaning", "masti"],
        "notes": "Santa playful pickup"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Wife: Shaadi ke 15 saal baad bhi tum mujhe pehle jaisa pyaar kyu nahi karte? Husband: Arey pagli, jab film hit ho chuki ho toh baar-baar trailer thodi dekhte hain! 🎬😂",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "romance", "double-meaning"],
        "notes": "Film trailer punchline"
    },
    {
        "subcategory": "couple-chat",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Girlfriend: Jaanu, tumne mere sapne me aakar mujhe kiss kiya tha na? Boyfriend: Pagal ho gayi hai kya? Main toh raat bhar Instagram pe Reels scroll kar raha tha, koi aur hoga! 🤦‍♂️🤣",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "boyfriend-girlfriend", "couple", "romance", "bf-gf"],
        "notes": "Dream vs reality couple joke"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Patni: Dekho, pados wale Sharma ji apni biwi ko kitna romantic gale lagate hain, tum kabhi kyu nahi lagate? Pati: Arey Sharma ji ki biwi se meri dosti hi nahi hai, thappad thodi khana hai! 🙈😂",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "husband-wife", "pati-patni", "padosi"],
        "notes": "Classic neighbor wife confusion"
    },
    {
        "subcategory": "dating",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Ladka: Tumhare lips kitne red hain, strawberry lagti ho! Ladki (sharma kar): Aww, thank you! Ladka: Wo sab theek hai, par Paan masala thuk kar baat karo na please! 🍃🤣",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "dating", "boyfriend-girlfriend", "roast"],
        "notes": "Desi red lips twist"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Pati bedroom me enter hua: Aaj tum itni sundar lag rahi ho ki mera dil machal raha hai... Patni: Seedhe-seedhe bolo dinner me tinde ki sabzi pasand nahi aayi aur bahar se pizza mangwana hai! 🍕🤣",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "biwi", "romance", "khana"],
        "notes": "Wife truth detection"
    },
    {
        "subcategory": "romance",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Boyfriend: Tumhare bina ek pal bhi jeena mushkil hai... Girlfriend: Accha, toh phir mera 666 wala recharge karwa do na! Boyfriend: Dekho jaan, mushkil hai par namumkin nahi, main koshish karunga! 🏃‍♂️💨",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "boyfriend-girlfriend", "recharge", "romance", "bf-gf"],
        "notes": "Recharge reality"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Patni: Agar main ek din mar gayi toh kya tum doosri shaadi karoge? Pati: Kabhi nahi! Ek hi torture do baar sehne ki himmat kisi me nahi hoti! 💀😂",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "shaadi", "double-meaning"],
        "notes": "Re-marriage dread joke"
    },
    {
        "subcategory": "doctor-patient",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Mareez: Doctor sahab, jab se shaadi hui hai raat ko neend nahi aati! Doctor: Biwi se jhagda hota hai kya? Mareez: Nahi, wo sote waqt mere phone ka pattern unlock karne ki koshish karti rehti hai! 📱👀",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "doctor-patient", "husband-wife", "phone", "biwi"],
        "notes": "Phone unlock paranoia"
    },
    {
        "subcategory": "flirt",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Ladka: Suno, tumhare papa terrorist hain kya? Ladki (gusse me): Kyu bey? Ladka: Kyunki tum bilkul bomb lag rahi ho! Ladki: Tere muh pe phoot jaungi toh bachega nahi, nikal yahan se! 💣🔥",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "double-meaning", "flirt", "boyfriend-girlfriend", "bomb"],
        "notes": "Classic bomb pickup roast"
    },
    {
        "subcategory": "husband-wife",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Pati ne romantic andaaz me Biwi ko baahon me liya. Biwi: Chhodo ji, mummy dekh lengi! Pati: Pagal ho gayi hai kya, mummy toh apne maayke me hain! Biwi: Arey meri nahi, tumhari mummy balcony me khadi hain! 🏃‍♂️💨",
        "clean": True,
        "safety_tags": ["safe", "double-meaning", "naughty-clean"],
        "tags": ["naughty", "husband-wife", "pati-patni", "romance", "saas", "biwi"],
        "notes": "Mother-in-law balcony surprise"
    }
]

def enrich_dataset_keywords():
    dm = DatasetManager()
    print(f"Enriching keywords across dataset. Current jokes: {len(dm.master_jokes)}")

    # 1. Ingest clean naughty jokes
    dm.ingest_category_jokes(
        "adult-clean",
        CLEAN_NAUGHTY_JOKES,
        {
            "source_name": "Curated Clean Double-Meaning & Witty Viral Humor",
            "source_url": "https://www.livehindustan.com/lifestyle/story-funny-husband-wife-jokes-in-hindi-pati-patni-ke-chutkule.html",
            "source_type": "lifestyle_media",
            "notes": "100% Google Play Safe clean double-meaning and romantic comedy jokes (zero abuses, zero vulgarity)"
        }
    )

    # 2. Enrich keywords / tags for EVERY joke in master
    for j in dm.master_jokes:
        cat = j.get("category", "")
        content = j.get("content", "").lower()
        tags = set(j.get("tags", []))

        # Always add category name variants
        tags.add(cat)
        tags.add("chutkule")
        tags.add("jokes")

        # Category-based keyword expansions
        if cat in ["husband-wife", "marriage"]:
            tags.update(["pati", "patni", "pati-patni", "biwi", "husband", "wife", "shaadi", "couple", "naughty", "romance"])
        elif cat in ["boyfriend-girlfriend", "love-dating"]:
            tags.update(["bf", "gf", "couple", "ladka-ladki", "dating", "romance", "naughty", "love", "flirt"])
        elif cat in ["teacher-student", "school-college", "exam-study"]:
            tags.update(["masterji", "teacher", "student", "school", "college", "exam", "pappu", "class"])
        elif cat in ["santa-banta-style"]:
            tags.update(["santa", "banta", "santa-banta", "sardar", "punjabi"])
        elif cat in ["doctor-patient"]:
            tags.update(["doctor", "mareez", "patient", "clinic", "hospital", "dawai"])
        elif cat in ["adult-clean"]:
            tags.update(["naughty", "double-meaning", "masti", "adult", "romance", "couple"])
        elif cat in ["pappu-style"]:
            tags.update(["pappu", "school", "funny", "chutkule"])
        elif cat in ["friends"]:
            tags.update(["dost", "dosti", "yaar", "yaari", "friends"])
        elif cat in ["office-work", "boss-employee"]:
            tags.update(["office", "boss", "salary", "job", "corporate"])

        # Content-based keyword discovery
        if any(w in content for w in ["pati", "patni", "biwi", "husband", "wife"]):
            tags.update(["pati", "patni", "pati-patni", "biwi"])
        if any(w in content for w in ["santa", "banta"]):
            tags.update(["santa", "banta", "santa-banta"])
        if any(w in content for w in ["pappu"]):
            tags.update(["pappu"])
        if any(w in content for w in ["doctor", "mareez"]):
            tags.update(["doctor", "mareez"])
        if any(w in content for w in ["romantic", "kiss", "chaand", "love", "sharma"]):
            tags.update(["romance", "naughty", "couple"])
        if any(w in content for w in ["office", "boss", "salary"]):
            tags.update(["office", "boss"])

        j["tags"] = sorted(list(tags))

    # 3. Save master and exports
    dm.save_all()
    dm.update_progress_file()

    print(f"Finished keyword enrichment. Total master jokes: {len(dm.master_jokes)}")

if __name__ == "__main__":
    enrich_dataset_keywords()
