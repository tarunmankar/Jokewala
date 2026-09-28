# -*- coding: utf-8 -*-
"""
Ingests 32 authentic viral Indian Name Jokes & Funny Roasts
into the new 'joke-on-names' category.
"""

import json
from dataset_manager import DatasetManager

NAME_JOKES = [
    {
        "subcategory": "deepak",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Deepak naam sunke flower samjha hai kya? Fire hai apun! Lekin problem yeh hai ki tez hawa aate hi Deepak bujh bhi sabse pehle jata hai! 😂🔥",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "deepak", "flower", "fire", "pushpa", "attitude", "roast"],
        "notes": "Popular viral Deepak line"
    },
    {
        "subcategory": "rahul",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Shahrukh Khan ne kaha tha: 'Rahul, naam toh suna hi hoga!' Lekin tragedy yeh hai ki Rahul ne khud school me teacher ka lecture kabhi dhyan se nahi suna! 🤣",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "rahul", "shahrukh", "school", "teacher", "roast"],
        "notes": "Classic Rahul DDLJ punch"
    },
    {
        "subcategory": "rohit",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Rohit ka alag hi swag hai: Cricket match me 200 run maare ya pehli ball pe zero pe out ho, par dosto ki udhari me Rohit hamesha 99 pe not out rehta hai! 🏏💸",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "rohit", "cricket", "udhari", "rohit-sharma"],
        "notes": "Rohit cricket and udhari joke"
    },
    {
        "subcategory": "aman",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Aman ka naam sunke lagta hai shanti ka doot hoga... Lekin sachai yeh hai ki WhatsApp group me aag lagane aur dange karwane ka theka hamesha Aman ke paas hi hota hai! 🔥📱",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "aman", "shanti", "whatsapp", "group", "lafda"],
        "notes": "Aman irony joke"
    },
    {
        "subcategory": "pooja",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Pooja se jab bhi pucho: 'Kya kar rahi ho?', bolti hai 'Bas thoda busy hoon'... Baad me pata chalta hai 3 ghante se Instagram reels pe lipstick review dekh rahi thi! 💄💅",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "pooja", "instagram", "busy", "reels"],
        "notes": "Pooja busy excuse joke"
    },
    {
        "subcategory": "neha",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Neha har doosre ladke ki ex hoti hai, aur teesre ladke ki 'It's complicated' wali crush! Neha ke chakkar se bachna aasan nahi hai boss! 🙈💔",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "neha", "crush", "ex", "complicated"],
        "notes": "Neha universal ex joke"
    },
    {
        "subcategory": "priya",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Priya jab gusse me hoti hai toh NASA ke top scientist bhi decode nahi kar paate ki baat kya hai! Bas ek hi dialogue bolti hai: 'Leave it, tum nahi samjhoge!' 🤦‍♂️🛰️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "priya", "gussa", "nasa", "mood"],
        "notes": "Priya leave it joke"
    },
    {
        "subcategory": "ankit",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Ankit har trip ke plan me bolta hai: 'Main 5 minute me nikal raha hoon!' Aur tab wo ghar pe sofe pe letkar banyan me chai ki chuski le raha hota hai! ☕🛋️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "ankit", "late", "chai", "plan"],
        "notes": "Ankit 5-minute late joke"
    },
    {
        "subcategory": "amit",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Har mohalle me ek Amit zaroor hota hai jiska ek dost police me hota hai, ek neta ka bhatija hota hai... par khud apni Splendor me 50 ka petrol dalwata hai! 🛵⛽",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "amit", "police", "neta", "petrol", "splendor"],
        "notes": "Amit contacts joke"
    },
    {
        "subcategory": "vikas",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Desh me sab puchte hain: 'Vikas kab aayega?'... Bhai Vikas toh coaching ke bahar tapri pe sutte aur chai pe gyaan pel raha hai! ☕🚬",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "vikas", "coaching", "chai", "tapri"],
        "notes": "Vikas satirical name pun"
    },
    {
        "subcategory": "simran",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Bauji ne Simran ko bola tha: 'Jaa Simran jee le apni zindagi!' Aur Simran tab se Zomato aur Swiggy pe 60% discount coupon dhoondh rahi hai! 🍕🛵",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "simran", "ddlj", "bauji", "zomato", "swiggy"],
        "notes": "Simran ddlj modern spin"
    },
    {
        "subcategory": "kunal",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Kunal har party me entry maar ke bolta hai: 'Aaj gaadi tera bhai chalayega!' Aur party khatam hone ke baad bolta hai: 'Bhai koi 100 rupaye Paytm karo, Uber book karni hai!' 🚗💸",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "kunal", "party", "gaadi", "uber", "paytm"],
        "notes": "Kunal driving party boast"
    },
    {
        "subcategory": "sneha",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Sneha typing... Sneha typing... Sneha typing... 20 minute ke wait ke baad Sneha ka final reply aata hai: 'K'. Sneha ji ke is 'K' ke liye pura mohalla tension me rehta hai! 📱💔",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "sneha", "typing", "whatsapp", "k"],
        "notes": "Sneha one word reply"
    },
    {
        "subcategory": "rohan",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Rohan har exam hall ke bahar ro kar bolta hai: 'Bhai meri toh back pakki hai, kuch nahi padha!' Aur result wale din 95% lake class me top kar jata hai! Aise Rohan se dosti se darr lagta hai! 📚😭",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "rohan", "exam", "topper", "padhai"],
        "notes": "Rohan topper acting"
    },
    {
        "subcategory": "pankaj",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Pankaj ka swabhav: Agar do dosto me ladai ho jaye toh pehle aage aake 'Ruk ja, main sambhalta hoon' bolega, aur jab haatha-paayi shuru ho toh sabse pehle wahan se 9-2-gyarah ho jayega! 🏃‍♂️💨",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "pankaj", "dosti", "ladai", "bhaagna"],
        "notes": "Pankaj referee runner"
    },
    {
        "subcategory": "sonu",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Sonu ki ek hi universal problem hai: 'Sonu, tujhe meri yaad nahi aati kya?' Aur Sonu ka phone pichle 3 saal se hamesha silent mode pe rehta hai! 📵🤷‍♂️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "sonu", "silent", "phone", "yaad"],
        "notes": "Sonu silent phone"
    },
    {
        "subcategory": "monu",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Monu se pucho career plan kya hai: 'Bhai pehle graduation ho jaye, fir dosto ke sath Goa jayenge, fir aage ka dekhenge!' Monu ka Goa trip pichle 7 saal se pending chal raha hai! 🏖️✈️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "monu", "goa", "career", "plan"],
        "notes": "Monu goa plan"
    },
    {
        "subcategory": "ritu",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Ritu har Instagram photo pe pout bana kar caption likhti hai: 'Totally candid click yaar!', bhale hi bechare photographer ne 58 retakes liye ho! 📸💄",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "ritu", "instagram", "candid", "pout", "photo"],
        "notes": "Ritu candid photoshoot"
    },
    {
        "subcategory": "gaurav",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Gaurav ko gym join kiye huye 2 din nahi hote aur wo protein shake ke aise gun-gaan gaata hai jaise aane wale Olympics me Arnold Schwarzenegger ko yahi replace karega! 💪🥤",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "gaurav", "gym", "protein", "fitness"],
        "notes": "Gaurav gym enthusiast"
    },
    {
        "subcategory": "manish",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Manish se jab bhi dosti me udhari maango: 'Bhai kal hi company se bonus aane wala hai, parso subah Google Pay kar dunga!' Manish ka parso pichle 6 mahine se nahi aaya! 💸📱",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "manish", "udhari", "google-pay", "salary"],
        "notes": "Manish pending payment"
    },
    {
        "subcategory": "shweta",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Online meeting me mic on chhod kar saare secret leak karne wali Shweta ke charche poore desh me famous hain! Shweta ka mic band karwao pehle! 🎙️🔊🤣",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "shweta", "mic", "zoom", "viral"],
        "notes": "Shweta mic on viral meme"
    },
    {
        "subcategory": "sanjay",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Sanjay har match me TV ke saamne baithkar bolta hai: 'Dhoni ko meri jagah 6 number pe bhejna chahiye tha!' Sanjay bhai khud gully cricket me pehli ball pe clean bowled hote hain! 🏏📺",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "sanjay", "cricket", "dhoni", "match"],
        "notes": "Sanjay armchair captain"
    },
    {
        "subcategory": "kavita",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Kavita jab WhatsApp status pe shayariyaan lagati hai toh aisa lagta hai jaise Mirza Ghalib aur Gulzar dono ka ek sath dil toot gaya ho! ✍️🥀",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "kavita", "shayari", "status", "whatsapp"],
        "notes": "Kavita sad shayari status"
    },
    {
        "subcategory": "sunil",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Sunil ka wedding rule: Shaadi ke buffet counter pe Sunil aise टूट-ta hai jaise kal subah se poori dharti pe anaj aur paneer ki supply band hone wali ho! 🍲🍛",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "sunil", "shaadi", "buffet", "khana", "paneer"],
        "notes": "Sunil wedding food enthusiast"
    },
    {
        "subcategory": "rajesh",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Rajesh uncle jab subah 5 baje Good Morning message bhejte hain, toh usme 12 gulab ke phool, 6 jalte huye diye aur 4 cup chai hoti hai... Phone ka storage hi bhar jata hai! 🌺☕",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "rajesh", "good-morning", "whatsapp", "uncle"],
        "notes": "Rajesh uncle good morning forward"
    },
    {
        "subcategory": "divya",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Divya jab bolti hai: 'Bas 2 minute me ready ho kar neeche aa rahi hoon!', toh samajh jao calendar me agle mahine ki date dekhne ka time aa gaya hai! ⏳👗",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "divya", "ready", "makeup", "late"],
        "notes": "Divya getting ready delay"
    },
    {
        "subcategory": "mohit",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Mohit har Saturday night ko kasam khata hai: 'Aaj raat bhar jaag kar syllabus khatam karunga!' Aur 11:15 baje YouTube pe bhutiya kahani dekh kar kambal me so jata hai! 🛌👻",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "mohit", "padhai", "youtube", "neend"],
        "notes": "Mohit study night resolve"
    },
    {
        "subcategory": "ananya",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Ananya ko lagta hai duniya ka har nakhra aur 'OMG, so aesthetic!' bolne ka patent usi ke paas hai! Bina iced latte ke Ananya ka din start hi nahi hota! ☕💅",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "ananya", "aesthetic", "latte", "nakhra"],
        "notes": "Ananya aesthetic humor"
    },
    {
        "subcategory": "vijay",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Vijay ka favourite dialogue: 'Haar kar jeetne wale ko baazigar kehte hain!' Par jab khud gully cricket me haarne lagta hai, toh apna bat leke ghar bhaag jata hai! 🏏🏃‍♂️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "vijay", "cricket", "bat", "baazigar"],
        "notes": "Vijay bat cheater joke"
    },
    {
        "subcategory": "ramesh-suresh",
        "language": "hinglish",
        "format": "one-liner",
        "content": "5 Star chocolate ke Ramesh aur Suresh jab milte hain, toh pitaji ki patloon chhoti ho jati hai aur recharge khatam ho jata hai! Extra dimaag mat chalao! 🍫😂",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "ramesh", "suresh", "5star", "chocolate"],
        "notes": "Ramesh and Suresh 5 Star homage"
    },
    {
        "subcategory": "ajay",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Ajay jab bhi bike chalata hai toh lagta hai do bike pe pair rakh ke 'Phool Aur Kaante' ka stunt maarne wala hai, par pehle hi speed-breaker pe balance bigad jata hai! 🏍️🕺",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "ajay", "bike", "stunt", "phool-aur-kaante"],
        "notes": "Ajay Devgn bike stunt parody"
    },
    {
        "subcategory": "deepak-extra",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Dost: Deepak, bhai tu itna chamak kyu raha hai aaj? Deepak: Kyunki kal hi beauty parlour se facial karwaya hai! Dost: Wah Deepak bhai, deepak jalne ke bajaye ab glowing cream pe chal raha hai! ✨🤣",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "deepak", "facial", "glow", "chamak"],
        "notes": "Deepak glowing pun"
    }
]

def ingest_names():
    dm = DatasetManager()
    initial_count = len(dm.master_jokes)
    print(f"Starting Ingestion of 'joke-on-names'. Existing jokes: {initial_count}")

    acc, dup = dm.ingest_category_jokes(
        "joke-on-names",
        NAME_JOKES,
        {
            "source_name": "Indian Popular Names Humor & Viral Roasts",
            "source_url": "https://www.scoopwhoop.com/humour/desi-names-funny-roasts-and-dialogues/",
            "source_type": "digital_media",
            "notes": "Curated viral humor on popular Indian names (Deepak, Rahul, Rohit, Aman, Pooja, Neha, etc.)"
        }
    )

    dm.save_all()
    dm.update_progress_file()

    print(f"Ingested: {acc} accepted, {dup} duplicates. Total master jokes now: {len(dm.master_jokes)}")

if __name__ == "__main__":
    ingest_names()
