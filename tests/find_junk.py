import json, re

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

junk_patterns = [
    r'Leave a Comment',
    r'Save my name',
    r'document\.getElementById',
    r'Notify me',
    r'\*{4,}',
    r'Loading…',
    r'Cancel reply',
    r'WhatsApp Jokes.*Hindi',
    r'phani WhatsApp',
    r'Pati par jokes',
    r'Pati Patni jokes in hindi',
    r'Pati Patni ke jokes',
]

found_junk = []
for j in jokes:
    for pat in junk_patterns:
        if re.search(pat, j['content'], re.IGNORECASE):
            found_junk.append((j['id'], pat, j['content'][:100]))
            break

print(f"Jokes with scraper junk/headers: {len(found_junk)}")
for fid, pat, snippet in found_junk[:15]:
    print(f"{fid} matched {pat}: {repr(snippet)}")
