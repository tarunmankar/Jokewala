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
    },
    {
        "subcategory": "deepak-roshni",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Naam me kya rakha hai: Deepak naam tha uska, par usne 8-10 ladkiyo ko andhere me rakha! Udhar Roshni bhi aisi hi thi, usne bhi 4 ladko ko andhere me rakha! 😂💡",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "deepak", "roshni", "andhera", "naam-me-kya-rakha-hai"],
        "notes": "Classic Webdunia viral Deepak and Roshni joke"
    },
    {
        "subcategory": "disha",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Naam me kya rakha hai... Rasta toh wo bhi theek se nahi bata paati jiska naam Disha hai! 'Bhaiya seedhe jaake right mud jaana, shayad wahi hoga!' 🗺️🤦‍♂️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "disha", "rasta", "gps", "naam-me-kya-rakha-hai"],
        "notes": "Amar Ujala viral Disha joke"
    },
    {
        "subcategory": "varsha",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Naam me kya rakha hai: Varsha naam ki ladki bhi zindagi me aag laga deti hai, aur barish hone ke bajaye taano ki barsaat hoti hai! 🌧️🔥",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "varsha", "aag", "barish", "naam-me-kya-rakha-hai"],
        "notes": "QuotesDiary viral Varsha pun"
    },
    {
        "subcategory": "komal",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Naam Komal hai, par dil se aisi pathar-dil nikli ki kal sham ko breakup hua aur aaj subah Instagram story pe dosto ke sath pizza party daal rahi hai! 🍕💔",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "komal", "pathar-dil", "breakup", "pizza"],
        "notes": "Komal irony roast"
    },
    {
        "subcategory": "karan-arjun",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Maa kehti thi: 'Mere Karan Arjun aayenge!'... Lekin yahan Karan credit card ki EMI bharne me phasa hai aur Arjun IT company me night shift me bugs fix kar raha hai! 💻💸",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "karan", "arjun", "karan-arjun", "emi", "it-job"],
        "notes": "Karan Arjun modern corporate spin"
    },
    {
        "subcategory": "kabir",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Kabir Singh banne ke chakkar me Kabir ne bina helmet Bullet daudayi... Traffic police ne jab 5000 ka chalan kaata, toh Kabir ko direct Kabir Das ke dohe yaad aa gaye! 🏍️📝",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "kabir", "kabir-singh", "bullet", "chalan"],
        "notes": "Kabir Singh vs Kabir Das chalan"
    },
    {
        "subcategory": "bunty",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Bunty ka sabun hamesha slow hota hai: Dosto ne Monday ko joke maara tha, Bunty ko Thursday ko hassi aayi jab teacher class me viva le rahi thi! 🧼⏱️🤣",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "bunty", "sabun-slow", "lifebuoy", "late-joke"],
        "notes": "Bunty slow sabun viral ad joke"
    },
    {
        "subcategory": "guddu",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Mirzapur dekh ke Guddu apne aap ko bahubali samajhne laga tha... Sham ko mummy ne jhaadu utha li toh chupchap 10 rupaye leke dukan se dhaniya lene bhaag gaya! 🧹🌿😂",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "guddu", "mirzapur", "mummy", "dhaniya", "jhaadu"],
        "notes": "Guddu bhaiya reality check"
    },
    {
        "subcategory": "munna",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Munna Bhai banne ke chakkar me Munna pados wali gussa aunty ko 'Jadoo ki jhappi' dene gaya tha... Aunty ne pehle jhappi li, fir chappal nikal li! 🫂🩴🤣",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "munna", "munna-bhai", "jadoo-ki-jhappi", "aunty"],
        "notes": "Munna Bhai jadoo ki jhappi twist"
    },
    {
        "subcategory": "suraj",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Gharwalo ne ladke ka naam Suraj rakha taaki ghar me roshni laaye... Aur Suraj roz dopahar 12 baje se pehle kambal se nikalne ka naam nahi leta! ☀️🛏️",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "suraj", "dopahar", "soona", "kambal"],
        "notes": "Suraj late rising joke"
    },
    {
        "subcategory": "aakash",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Naam Aakash hai par jab dhabe pe dosto ke sath chai-samosa ka hisab hota hai, toh zameen pe baith kar 2 rupaye ki extra chutney ka hisab mangne lagta hai! ☁️🪙",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "aakash", "hisab", "dhaba", "chutney"],
        "notes": "Aakash ground reality"
    },
    {
        "subcategory": "baburao",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Baburao ka alag hi level hai: 'Utha le re baba, utha le... Mereko nahi re, in sab WhatsApp group walo ko ek sath utha le!' 👓😂",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "baburao", "hera-pheri", "utha-le", "whatsapp"],
        "notes": "Baburao Hera Pheri classic line"
    },
    {
        "subcategory": "sweety",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Naam Sweety hai, par jab subah muh kholti hai toh uske taane sunkar karela aur neem bhi aapas me bolte hain: 'Bhai hum toh iske aage mehenge amrit hain!' 🥒🐝",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "sweety", "taane", "karela", "kadwi"],
        "notes": "Sweety bitter talk pun"
    },
    {
        "subcategory": "shanti",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Naam Shanti aunty hai, par jaise hi mohalle me entry leti hain, pados ki 4 biwiyo aur saas ke beech teesra vishwa yuddh chhidwa deti hain! 📢🕊️🔥",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "shanti", "aunty", "mohalla", "kalesh"],
        "notes": "Shanti aunty kalesh joke"
    },
    {
        "subcategory": "sharma-ji",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Papa: Dekh Sharma ji ka beta Google me 50 lakh ka package le gaya! Beta: Papa, par Sharma ji ka beta ghar aake khana toh Swiggy se hi mangwata hai, aur main toh mummy ke haath ki roti khata hoon! 👨‍💼🍕",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "sharma-ji", "sharma-ji-ka-beta", "google", "swiggy", "papa"],
        "notes": "Sharma ji ka beta legendary comparison"
    },
    {
        "subcategory": "anil",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Anil har wedding me dulha-dulhan ke camera man ke theek peeche khada rehta hai, taaki album ki har doosri photo me Anil ka aadha chehra zaroor chamke! 📸🤵",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "anil", "shaadi", "cameraman", "photo"],
        "notes": "Anil wedding photo bomber"
    },
    {
        "subcategory": "kavya",
        "language": "hinglish",
        "format": "one-liner",
        "content": "Kavya Instagram bio me likhti hai: 'Simple girl with big dreams 🌸', par sham ko dosto ke sath momos khate waqt 12 baar extra mayonnaise aur tissue paper mangwati hai! 🥟💅",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "kavya", "instagram", "momos", "mayonnaise"],
        "notes": "Kavya simple girl momos joke"
    },
    {
        "subcategory": "hardik",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Hardik jab bolta hai: 'Aaj match main akele jitaunga!', toh padosi pehle TV band kar dete hain aur inverter ka switch on kar lete hain! 🏏⚡",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "hardik", "cricket", "match", "inverter"],
        "notes": "Hardik cricket match joke"
    },
    {
        "subcategory": "poonam",
        "language": "hinglish",
        "format": "dialogue",
        "content": "Poonam se pucha: 'Poonam ki raat ko chaand kitna sundar lagta hai na?' Poonam: 'Haan, par wo sab chhod, Zomato pe 50% flat off ka coupon mil raha hai kya?' 🌕🍕",
        "clean": True,
        "safety_tags": ["safe", "clean", "name-roast"],
        "tags": ["joke-on-names", "names", "poonam", "chaand", "zomato", "coupon"],
        "notes": "Poonam chaand vs food joke"
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
            "source_url": "https://www.webdunia.com/hindi-jokes/naam-me-kya-rakha-hai-jokes.html",
            "source_type": "digital_media",
            "notes": "Curated viral humor on popular Indian names (Deepak, Rahul, Rohit, Disha, Varsha, Bunty, etc.)"
        }
    )

    dm.save_all()
    dm.update_progress_file()

    print(f"Ingested: {acc} accepted, {dup} duplicates. Total master jokes now: {len(dm.master_jokes)}")

if __name__ == "__main__":
    ingest_names()
