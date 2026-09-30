import json, sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'hinglish-jokes-dataset', 'scripts'))

with open('hinglish-jokes-dataset/jokes-master.json', 'r', encoding='utf-8') as f:
    jokes = json.load(f)

# These are the IDs we identified as fragments / incomplete jokes
# We'll either remove them or merge them with adjacent context

# Group 1: Fragment pieces of the same dialogue story - they're consecutive parts
# Best action: Remove the fragments that are just setup lines without punchline, 
# OR merge into one complete joke

fragment_ids_to_remove = set([
    'HJ-001195',  # "priye, main tumse bahut pyar karta hu." - just a setup, no punchline standalone
    'HJ-001197',  # "lekin tum toh din-raat mujhse hi ladati rahati ho." - fragment
    'HJ-001232',  # "Patni: adarak vali? Pati: Ok Patni: pudeena daloon ?" - fragment (of longer chai joke)
    'HJ-001239',  # "Patni Pati se: chalo utho chai aur nashta banane jao…" - fragment/setup
    'HJ-001247',  # "Patni: yeh bandook leke darwaje pe kyu khade ho..?" - fragment (answer is next joke)
    'HJ-001250',  # "Patni: bhaiya yeh lauki kya bhav...50 roopye kilo" - fragment
    'HJ-001292',  # "Teacher – ho sakta hai, lekin tumhe deri kyu hui?" - fragment
    'HJ-000622',  # "phir daayi tang mein hi takaliph kyu?" - orphan fragment, no context
    'HJ-000906',  # "police – phir theek hai maran de…" - orphan fragment
])

# Merge pairs into complete jokes
merge_map = {
    # Merge chai sequence: 1231 + 1232 + 1233
    'HJ-001231': "Patni: Chai banaoon?\nPati: Han theek hai.\nPatni: Adarak vali?\nPati: Ok.\nPatni: Pudeena daloon?\nPati: Han theek hai.\nPatni: Tulasi?\nPati: Han theek hai.\nPatni: Aur yeh kya daloo?\nPati (frustrate hokar): Oye! Chai banana hai ya poori aushadhi banaani hai? 😂",
    
    # Merge bandook sequence: HJ-001247 + HJ-001248
    'HJ-001248': "Patni: Yeh bandook leke darwaje pe kyu khade ho?\nPati: Sher ka shikar karne jaa raha hoon.\nPatni: Toh jaate kyu nahi?\nPati: Sher abhi aa raha hai. 😂😂",

    # Merge teacher sequence: HJ-001291 + HJ-001292
    'HJ-001291': "Teacher ne Pappu se late school aane ki wajah puchi.\nPappu ne kaha: Mummy aur Papa mein ladai ho rahi thi.\nTeacher: Toh tumhe deri kyu hui?\nPappu: Sir, mere joote bahar hi the. 😂",

    # Merge doctor sequence: 683 + 684 + 685 into one complete joke
    'HJ-000683': "Mareez: Doctor sahab, meri daayi taang mein bahut dard rehta hai.\nDoctor: Yeh toh umr ka taqaza hai.\nMareez: Lekin meri baayi taang ki bhi utni hi umr hai, us mein toh dard nahi! 😂😂",

    # Merge police WhatsApp joke: 905 + 906
    'HJ-000905': "Police: Tumhare samne chor us ladki ka purse chheen raha tha aur tumne koi madad nahi ki!\nLadka: Main us ladki ko jaanta hoon.\nPolice: Toh kya fark pada?\nLadka: Uska WhatsApp status hai - 'I can handle my own problems'.\nPolice: ...Theek hai, jaane do. 😂😂",

    # Merge bullet/eent sequence: HJ-001347 + HJ-001348 + HJ-001349
    'HJ-001347': "Patni: Sunoji, aapke sir par khoon kyu nikal raha hai, yeh kaise hua?\nPati: Kya bataoon, mere dost ne eet maar di.\nPatni: Apne kuch nahi kiya? Mar dete use, haath mein kuch nahi tha?\nPati: Haath mein toh eet thi, lekin woh mera dost hai na! 😂😂",

    # Lauki joke: 1250 + 1251 (complete)
    'HJ-001251': "Patni: Bhaiya, yeh lauki kya bhav hai?\nSabzivala: 50 rupaye kilo.\nPatni: Aur yeh bhindi tamatar?\nPati (peechhe se): Jaldi karo, mujhe office ke liye der ho rahi hai.\nPatni: Ek minute! Aur yeh palak?\nPati: Patni ke saath market aana matlab - poori zindagi yahan hi beet jayegi. 😂",

    # Aloo paratha: 1321 + 1322 complete
    'HJ-001321': "Pati: Suno! Aaj aloo parathe mein aloo nazar nahi aa raha.\nPatni: Chupchap khaa lo. Kabhi Agre ke pethe mein Agra nazar aata hai kya? 😂😂",
}

# IDs to fully remove (and also 1233 onwards that were merged)
ids_to_also_remove = set([
    'HJ-001196',  # Was merged into HJ-001195 story (but we removed that)  
    'HJ-001198',  # Was merged (orphan ending)
    'HJ-001233',  # Was merged into chai joke
    'HJ-001248',  # Now standalone complete (we merged the setup into this)
    'HJ-001349',  # Merged into HJ-001347
    'HJ-000684',  # Merged into HJ-000683
    'HJ-000685',  # Was merged into doctor joke
])

removed_count = 0
merged_count = 0
new_jokes = []

for j in jokes:
    jid = j['id']
    
    # Apply merges first
    if jid in merge_map:
        j['content'] = merge_map[jid]
        merged_count += 1
        new_jokes.append(j)
    
    # Skip fragments or merged parts
    elif jid in fragment_ids_to_remove or jid in ids_to_also_remove:
        removed_count += 1
        # Don't append - removes this joke
    
    else:
        new_jokes.append(j)

print(f"Removed: {removed_count} fragment/orphan jokes")
print(f"Merged/fixed: {merged_count} jokes")
print(f"Total remaining: {len(new_jokes)}")

# Verify no very short jokes remain (except naturally short one-liners that are complete)
still_short = [j for j in new_jokes if len(j['content'].strip()) < 50]
print(f"Still short (< 50 chars): {len(still_short)}")
for j in still_short:
    print(f"  {j['id']}: {repr(j['content'][:80])}")

# Save
with open('hinglish-jokes-dataset/jokes-master.json', 'w', encoding='utf-8') as f:
    json.dump(new_jokes, f, indent=2, ensure_ascii=False)

print("Saved!")
