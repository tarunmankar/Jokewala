import json
import random
from hindi_to_hinglish import hindi_to_hinglish

d = json.load(open('jokes-master.json', encoding='utf-8'))
dev_jokes = [j for j in d if any('\u0900' <= c <= '\u097f' for c in j['content'])]
random.seed(42)
samples = random.sample(dev_jokes, 5)

for i, s in enumerate(samples):
    print(f"=== SAMPLE {i+1} ({s['category']}) ===")
    print("--- Hindi ---")
    print(s['content'])
    print("--- Hinglish ---")
    print(hindi_to_hinglish(s['content']))
    print()
