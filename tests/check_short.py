import json

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

short_jokes = [j for j in jokes if len(j['content'].strip()) < 90]
print(f'Jokes < 90 chars: {len(short_jokes)}')
for j in short_jokes:
    print(f"{j['id']} [{j['category']}]: {repr(j['content'])}")
