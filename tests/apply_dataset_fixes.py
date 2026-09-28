import os
import sys
import json
import shutil

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_DIR = os.path.join(BASE_DIR, "hinglish-jokes-dataset")
APP_DIR = os.path.join(BASE_DIR, "chutkule-wala")
sys.path.insert(0, os.path.join(DATASET_DIR, "scripts"))

from dataset_manager import DatasetManager

clean_replacements = {
    "HJ-001200": "Patni: TV pe Zee TV nahi aa raha hai!\nPati: Are pagli Zee nahi lagta toh Star aur Sony laga kar dekh liya kar, woh bhi acche channel hain!",
    
    "HJ-001228": "Patni (raat ko): Suniye ji, maine ek sapna dekha ki aapne mere liye sone ka haar khareed liya hai!\nPati: Theek hai pagli, toh wapis so jaa aur pehan le!",
    
    "HJ-001275": "Pati (subah subah): Aaj naashte mein kya banaya hai ji?\nPatni: Kyun, kis liye poochh rahe ho?\nPati: Are bhagwan, mujhse bhi toh upar swarg mein poochha jayega ki aakhir kya kha kar mare the! 😂😂😂",
    
    "HJ-001285": "Teacher: Pappu, class mein baar baar sar neeche kyu gira rahe ho, neend aa rahi hai kya?\nPappu: Nahi teacher, gurutvakarshan (gravity) se sar neeche gir raha hai, mera koi dosh nahi hai!",
    
    "HJ-001288": "Teacher: Pappu, tum roz late kyu aate ho? Kuch bolo!\nPappu: Zinda rehne ke liye teri kasam, ek mulakat zaroori hai sanam!\n(Phir kya... de thappad de thappad!) 😂",
    
    "HJ-001293": "Adhyapak: Agar tumhara best friend aur girlfriend dono nadi mein doob rahe ho, toh tum kise bachaoge?\nStudent: Doob jaane do saalon ko, aakhir woh dono ek saath nadi kinare kar kya rahe the!",
    
    "HJ-001302": "Teacher: Pappu, tumhara padhai mein bilkul dhyan nahi rehta!\nPappu: Sir, aap apni beti par dhyan do, tab pata chalega mera dhyan kahan rehta hai!",
    
    "HJ-001304": "Teacher: Pappu, kabhi zindagi mein kisi se koi seekh li hai tumne?\nPappu: Li hai sir, bahut seekh li hai... tabhi toh fail hoke bhi khush rehta hoon!",
    
    "HJ-001305": "Dost aur Biwi ko kabhi vishwas dilane ki zaroorat nahi hoti... kyunki sachha dost kabhi shak nahi karta, aur biwi kabhi yaqeen nahi karti!",
    
    "HJ-001308": "Boy (khush hoke): Aaj pehli baar metro mein ek sundar ladki ne mujhse baat ki!\nDost: Wah bhai! Kya baat ki?\nBoy: Boli- Oye hero, khade ho jao, yeh ladies seat hai!",
    
    "HJ-001314": "Boy (romantic hoke): Darling, mujhe tumhari dono aankhon mein poori duniya dikhti hai!\nPeechhe se ek budhiya boli: Beta, subah se hamari bhains nahi mil rahi, zara dekh ke bata de kahan char rahi hai!",
    
    "HJ-001333": "Pintu: Papa, main jeevan mein aage badhne ke liye sabse pehle kya karoon?\nPapa: Ek patthar utha aur pehle apna smartphone phod, tab aage badhega!",
    
    "HJ-001340": "Husband: Aisi kadak chai banao ki peete hi tan-badan jhoomne lage aur mann naachne lage!\nWife: Hamare yahan bhains ka doodh aata hai ji, naagin ka nahi! 😆😆",
    
    "HJ-001341": "Husband: Aaj toh bohot garmi si lag rahi hai.\nWife: Haan ji, garmi toh bohot badh gayi hai.\nHusband: Chalo chhat par chalte hain, thandi hawa kha ke aate hain.\nWife: Aap chalo, main plate aur chammach lekar aati hoon!"
}

# 1. Update jokes-master.json
master_path = os.path.join(DATASET_DIR, "jokes-master.json")
with open(master_path, "r", encoding="utf-8") as f:
    jokes = json.load(f)

for j in jokes:
    # Fix the scraped bloated jokes
    if j["id"] in clean_replacements:
        j["content"] = clean_replacements[j["id"]]
    # Fix Devanagari character in HJ-001396
    if j["id"] == "HJ-001396":
        j["content"] = j["content"].replace("टूट-ta", "toot-ta")

with open(master_path, "w", encoding="utf-8") as f:
    json.dump(jokes, f, indent=2, ensure_ascii=False)

print("Updated jokes-master.json successfully.")

# 2. Export all cleanly via DatasetManager
dm = DatasetManager()
dm.master_jokes = jokes
dm.save_all()
print("Exported dataset successfully.")

# 3. Synchronize with chutkule-wala assets
clean_export_path = os.path.join(DATASET_DIR, "exports", "clean-jokes.json")
app_jokes_path = os.path.join(APP_DIR, "assets", "jokes.json")
shutil.copyfile(clean_export_path, app_jokes_path)
print("Synchronized chutkule-wala/assets/jokes.json successfully.")
