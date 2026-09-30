import json

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

for j in jokes:
    if j['id'] in ['HJ-001238', 'HJ-001239', 'HJ-001240', 'HJ-001241', 'HJ-001246', 'HJ-001247', 'HJ-001248', 'HJ-001249', 'HJ-001250', 'HJ-001251', 'HJ-001252', 'HJ-001291', 'HJ-001292', 'HJ-001321', 'HJ-001322', 'HJ-001347', 'HJ-001348', 'HJ-001349', 'HJ-001350']:
        print(f"=== {j['id']} ===")
        print(j['content'])
