import json

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

for j in jokes:
    jid = j['id']
    if 'HJ-000605' <= jid <= 'HJ-000630':
        print(f"[{jid}] {repr(j['content'][:120])}")
