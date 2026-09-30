import json
import re

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

print(f"Total jokes in master: {len(jokes)}")

# Look for short jokes (< 75 characters)
short = [j for j in jokes if len(j['content'].strip()) < 75]
print(f"\nJokes < 75 chars ({len(short)}):")
for j in short:
    print(f"  {j['id']} [{j['category']}]: {repr(j['content'])}")

# Look for jokes that end with incomplete punctuation (like commas, dashes, colons)
incomplete_end = []
for j in jokes:
    c = j['content'].strip()
    if c.endswith((',', '–', '-', ':', '…', '...', 'toh')):
        incomplete_end.append((j['id'], c[-40:]))

print(f"\nJokes ending with incomplete trailing punctuation ({len(incomplete_end)}):")
for jid, snippet in incomplete_end:
    print(f"  {jid}: ...{repr(snippet)}")
