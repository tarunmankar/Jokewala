import json

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

# Check jokes around the short/fragment ones - they're likely part of a sequence
fragment_ids = ['HJ-001195', 'HJ-001197', 'HJ-001215', 'HJ-001232', 'HJ-001239', 'HJ-001247', 'HJ-001250', 'HJ-001292', 'HJ-001321', 'HJ-001348', 'HJ-000622', 'HJ-000684', 'HJ-000906']
# Print their full content and nearby jokes
id_map = {j['id']: j for j in jokes}
id_list = [j['id'] for j in jokes]

for fid in fragment_ids:
    idx = id_list.index(fid)
    print(f"\n=== {fid} ===")
    if idx > 0:
        prev = jokes[idx-1]
        print(f"PREV ({prev['id']}): {repr(prev['content'][:200])}")
    print(f"THIS: {repr(jokes[idx]['content'][:200])}")
    if idx < len(jokes)-1:
        nxt = jokes[idx+1]
        print(f"NEXT ({nxt['id']}): {repr(nxt['content'][:200])}")
