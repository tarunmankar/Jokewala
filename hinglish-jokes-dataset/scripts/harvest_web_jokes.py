import os
import re
import html
import urllib.request
from dataset_manager import DatasetManager

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "hi,en;q=0.9"
}

def fetch_url(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def clean_joke_text(text):
    text = html.unescape(text)
    # remove html tags
    text = re.sub(r"<[^>]+>", " ", text)
    # remove excessive symbols or ads
    text = re.sub(r"Copy|COPY|Download|DOWNLOAD", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()

def detect_category(text, default_cat):
    t = text.lower()
    if any(k in t for k in ["पति", "पत्नी", "बीवी", "पति-पत्नी", "सास", "ससुर", "दामाद"]):
        return "husband-wife"
    if any(k in t for k in ["टीचर", "छात्र", "मास्टर", "मैडम", "होमवर्क", "क्लास"]):
        return "teacher-student"
    if any(k in t for k in ["संता", "बंता", "santa", "banta"]):
        return "santa-banta-style"
    if any(k in t for k in ["डॉक्टर", "मरीज", "ऑपरेशन", "दवाई", "सुई", "अस्पताल", "क्लीनिक"]):
        return "doctor-patient"
    if any(k in t for k in ["पप्पू"]):
        return "pappu-style"
    if any(k in t for k in ["दोस्त", "यार", "दोस्ती"]):
        return "friends"
    if any(k in t for k in ["लड़का", "लड़की", "गर्लफ्रेंड", "बॉयफ्रेंड", "gf", "bf"]):
        return "boyfriend-girlfriend"
    if any(k in t for k in ["ऑफिस", "बॉस", "सैलरी", "मैनेजर"]):
        return "office-work"
    if any(k in t for k in ["इंजीनियर", "engineer"]):
        return "engineer"
    if any(k in t for k in ["शादी", "दुल्हन", "दूल्हा"]):
        return "marriage"
    if any(k in t for k in ["परीक्षा", "एग्जाम", "रिजल्ट"]):
        return "exam-study"
    if any(k in t for k in ["शराबी", "दारू", "ठेका"]):
        return "desi-life"
    return default_cat

def harvest_heloplus(dm):
    url = "https://www.heloplus.com/quotes/jokes-in-hindi/"
    print(f"Scraping HeloPlus: {url}...")
    html_doc = fetch_url(url)
    if not html_doc:
        return 0

    paras = re.findall(r"<p[^>]*>(.*?)</p>", html_doc, re.DOTALL)
    accepted, dups = 0, 0
    grouped = {}

    for raw in paras:
        c = clean_joke_text(raw)
        if len(c) < 35 or len(c) > 750:
            continue
        if any(w in c for w in ["Quotes", "Shayari", "HeloPlus", "Copyright", "Status"]):
            continue
        if not any(w in c for w in [":", "–", "-", "?", "!", "।", "🤣", "😂"]):
            continue

        cat = detect_category(c, "clean-family-friendly")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append({
            "subcategory": "heloplus-curated",
            "language": "hindi",
            "format": "dialogue" if any(s in c for s in [":", "–", "-"]) else "one-liner",
            "content": c,
            "clean": True,
            "safety_tags": ["safe", "family-friendly"],
            "tags": [cat, "heloplus"],
            "notes": "Scraped from HeloPlus Jokes collection",
            "popularity_signal": {"verified_source": True}
        })

    for cat, items in grouped.items():
        acc, dup = dm.ingest_category_jokes(
            cat,
            items,
            {
                "source_name": "HeloPlus Jokes",
                "source_url": url,
                "source_type": "humour_portal",
                "notes": "Curated popular viral Hindi jokes from HeloPlus"
            }
        )
        accepted += acc
        dups += dup

    print(f"HeloPlus finished: {accepted} accepted, {dups} duplicates.")
    return accepted

def harvest_funkylife(dm):
    fl_urls = [
        {"url": "https://funkylife.in/hindi-jokes/", "cat": "clean-family-friendly"},
        {"url": "https://funkylife.in/santa-banta-jokes-hindi/", "cat": "santa-banta-style"},
        {"url": "https://funkylife.in/pati-patni-jokes/", "cat": "husband-wife"},
        {"url": "https://funkylife.in/teacher-student-jokes-hindi/", "cat": "teacher-student"},
        {"url": "https://funkylife.in/whatsapp-jokes/", "cat": "whatsapp"},
        {"url": "https://funkylife.in/chutkule/", "cat": "clean-family-friendly"}
    ]

    accepted_total = 0
    dups_total = 0

    for item in fl_urls:
        url = item["url"]
        print(f"Scraping FunkyLife: {url}...")
        html_doc = fetch_url(url)
        if not html_doc:
            continue

        paras = re.findall(r"<p[^>]*>(.*?)</p>", html_doc, re.DOTALL)
        grouped = {}

        for raw in paras:
            c = clean_joke_text(raw)
            if len(c) < 35 or len(c) > 750:
                continue
            if any(w in c for w in ["Funky Life", "Follow Us", "See 2023", "Search for", "Leave a Reply"]):
                continue
            if not any(w in c for w in [":", "–", "-", "?", "!", "।", "🤣", "😂", "😜"]):
                continue

            cat = detect_category(c, item["cat"])
            if cat not in grouped:
                grouped[cat] = []
            grouped[cat].append({
                "subcategory": "funkylife-viral",
                "language": "hindi",
                "format": "dialogue" if any(s in c for s in [":", "–", "-"]) else "one-liner",
                "content": c,
                "clean": True,
                "safety_tags": ["safe", "family-friendly"],
                "tags": [cat, "funkylife"],
                "notes": f"Scraped from {url}",
                "popularity_signal": {"verified_source": True}
            })

        for cat, jokes in grouped.items():
            acc, dup = dm.ingest_category_jokes(
                cat,
                jokes,
                {
                    "source_name": "FunkyLife Hindi Chutkule",
                    "source_url": url,
                    "source_type": "humour_portal",
                    "notes": "Verified popular jokes from FunkyLife"
                }
            )
            accepted_total += acc
            dups_total += dup

    print(f"FunkyLife finished: {accepted_total} accepted, {dups_total} duplicates.")
    return accepted_total

def harvest_zeetalwara(dm):
    zt_urls = [
        {"url": "https://www.zeetalwara.com/pati-patni-jokes-in-hindi-latest/", "cat": "husband-wife"},
        {"url": "https://www.zeetalwara.com/pati-patni-jokes-in-hindi/", "cat": "husband-wife"},
        {"url": "https://www.zeetalwara.com/teacher-and-student-funny-jokes-in-hindi/", "cat": "teacher-student"},
        {"url": "https://www.zeetalwara.com/funny-dosti-jokes-in-hindi/", "cat": "friends"},
        {"url": "https://www.zeetalwara.com/girl-and-boy-funny-jokes-in-hindi/", "cat": "boyfriend-girlfriend"},
        {"url": "https://www.zeetalwara.com/21-very-funny-chutkule-in-hindi/", "cat": "clean-family-friendly"},
        {"url": "https://www.zeetalwara.com/best-jokes-in-hindi-for-husband-and-wife/", "cat": "husband-wife"}
    ]

    accepted_total = 0
    dups_total = 0

    for item in zt_urls:
        url = item["url"]
        print(f"Scraping Zeetalwara: {url}...")
        html_doc = fetch_url(url)
        if not html_doc:
            continue

        paras = re.findall(r"<p[^>]*>(.*?)</p>", html_doc, re.DOTALL)
        clean = [clean_joke_text(p) for p in paras]
        clean = [c for c in clean if len(c) > 5 and not c.startswith("http")]

        jokes = []
        curr = []
        for p in clean:
            if any(h in p for h in ["funny jokes", "chutkule", "पढ़ेंगे", "मित्रों", "शेयर करें", "दोस्तों इस लेख"]):
                if curr:
                    j = "\n".join(curr).strip()
                    if len(j) > 35 and any(s in j for s in [":", "–", "-", "?", "!"]):
                        jokes.append(j)
                    curr = []
                continue

            is_starter = any(p.startswith(w) for w in ["टीचर", "मास्टर", "मैडम", "सर ", "एक बार", "पति", "पत्नी", "संजू", "पप्पू", "संता", "लड़का", "लड़की", "डॉक्टर"])
            if is_starter and curr and len("\n".join(curr)) > 45:
                jokes.append("\n".join(curr).strip())
                curr = [p]
            else:
                curr.append(p)

        if curr:
            j = "\n".join(curr).strip()
            if len(j) > 35 and any(s in j for s in [":", "–", "-", "?", "!"]):
                jokes.append(j)

        grouped = {}
        for j in jokes:
            cat = detect_category(j, item["cat"])
            if cat not in grouped:
                grouped[cat] = []
            grouped[cat].append({
                "subcategory": "zeetalwara-curated",
                "language": "hindi",
                "format": "dialogue" if ":" in j else "one-liner",
                "content": j,
                "clean": True,
                "safety_tags": ["safe", "family-friendly"],
                "tags": [cat, "zeetalwara"],
                "notes": f"Scraped from {url}",
                "popularity_signal": {"verified_source": True}
            })

        for cat, jks in grouped.items():
            acc, dup = dm.ingest_category_jokes(
                cat,
                jks,
                {
                    "source_name": "ZeeTalwara Humour",
                    "source_url": url,
                    "source_type": "humour_portal",
                    "notes": "Authentic conversational Hindi jokes from ZeeTalwara"
                }
            )
            accepted_total += acc
            dups_total += dup

    print(f"Zeetalwara finished: {accepted_total} accepted, {dups_total} duplicates.")
    return accepted_total

if __name__ == "__main__":
    dm = DatasetManager()
    initial_count = len(dm.master_jokes)
    print(f"Starting Multi-Source Web Harvest. Initial jokes: {initial_count}")

    harvest_heloplus(dm)
    harvest_funkylife(dm)
    harvest_zeetalwara(dm)

    dm.save_all()
    dm.update_progress_file()

    final_count = len(dm.master_jokes)
    print(f"==================================================")
    print(f"Harvest Summary: Started: {initial_count}, Now: {final_count} (+{final_count - initial_count} unique web jokes)")
    print(f"==================================================")
