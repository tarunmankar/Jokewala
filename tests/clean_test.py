import json
import re

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

# 1. Clean scraper junk and website boilerplate from joke contents
def clean_joke_content(text):
    original = text
    # Remove HTML / JS snippets
    text = re.sub(r'Δ document\.getElementById\(.*?\);?', '', text)
    text = re.sub(r'Loading…\s*Leave a Comment.*', '', text, flags=re.DOTALL)
    text = re.sub(r'Save my name, email.*', '', text, flags=re.DOTALL)
    text = re.sub(r'Notify me of.*', '', text, flags=re.DOTALL)
    
    # Remove asterisks dividers
    text = re.sub(r'\*{3,}', '', text)
    
    # Remove website header garbage like "Whatsapp Jokes in Hindi", "See Also: ...", "phani WhatsApp joks in hindi"
    header_patterns = [
        r'^(?:Whatsapp Jokes (?:Chutkule )?in Hindi\s*)+',
        r'^(?:Hindi Jokes >>\s*(?:See Also:\s*)?(?:hindi chutakule\s*)?(?:Teacher Student Jokes in Hindi\s*)?(?:WhatsApp Jokes in Hindi\s*)?)+',
        r'^(?:veri\s+)?phani WhatsApp (?:stetas\s+)?joks?(?:\s+in\s+hindi)?\s*',
        r'^(?:hasy chutakule hindi mein\s*)+',
        r'^(?:WhatsApp Jokes Status\s*)+',
        r'^(?:WhatsApp ke chutakule\s*)+',
        r'^(?:Pati par jokes\s*)+',
        r'^(?:Pati Patni (?:ke )?jokes(?:\s+in\s+hindi(?:\s+latest)?)?\s*)+',
        r'^(?:shaharee Ladka Dehaati Mahila Funny Jokes In Hindi\s*)+',
        r'^(?:Long WhatsApp Jokes in Hindi\s*)+',
        r'^(?:Ladka Ladki Funny Jokes In Hindi\s*)+',
        r'^(?:Teacher Student Funny Jokes In Hindi\s*)+',
    ]
    for hp in header_patterns:
        text = re.sub(hp, '', text, flags=re.IGNORECASE | re.MULTILINE)
    
    # Remove leading/trailing empty lines and spaces
    lines = [l.strip() for l in text.split('\n')]
    # drop empty lines at start and end
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    
    text = '\n'.join(lines)
    return text.strip()

# Test cleaning on jokes
cleaned_count = 0
for j in jokes:
    cleaned = clean_joke_content(j['content'])
    if cleaned != j['content']:
        cleaned_count += 1

print(f"Total jokes needing text cleaning: {cleaned_count}")
