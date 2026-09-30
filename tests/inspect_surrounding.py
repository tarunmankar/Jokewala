import json

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

short_ids = [
    'HJ-000622', 'HJ-000684', 'HJ-000906', 'HJ-001195', 'HJ-001197', 
    'HJ-001215', 'HJ-001232', 'HJ-001239', 'HJ-001247', 'HJ-001250', 
    'HJ-001292', 'HJ-001321', 'HJ-001348'
]

joke_map = {j['id']: (i, j) for i, j in enumerate(jokes)}

for sid in short_ids:
    if sid not in joke_map:
        continue
    idx, j = joke_map[sid]
    start = max(0, idx - 1)
    end = min(len(jokes), idx + 2)
    print(f"\n=================== Surrounding {sid} ===================")
    for k in range(start, end):
        jk = jokes[k]
        print(f"--- {jk['id']} ---")
        print(jk['content'])
