import json
import re
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_DIR = os.path.join(BASE_DIR, "hinglish-jokes-dataset")
APP_DIR = os.path.join(BASE_DIR, "chutkule-wala")
sys.path.insert(0, os.path.join(DATASET_DIR, "scripts"))

from dataset_manager import DatasetManager

# 1. Load jokes-master.json
master_path = os.path.join(DATASET_DIR, "jokes-master.json")
with open(master_path, "r", encoding="utf-8") as f:
    jokes = json.load(f)

print(f"Loaded {len(jokes)} jokes from master.")

# 2. Complete jokes replacements (merge fragments into complete, funny jokes)
merge_replacements = {
    # 605 + 606 + 686 -> Santa baby joke
    "HJ-000605": "Santa (apni Mummy se): Mummy khushkhabri hai, hum do se teen ho gaye hain!\nMummy: Badhai ho beta! Kya hua hai, beta ya beti?\nSanta: Na beta, na beti... maine doosri shaadi kar li hai! 😂😂😂",
    
    # 683 + 684 + 685 -> Doctor leg pain joke
    "HJ-000683": "Mareez: Doctor sahab, meri daayi taang mein bahut dard rehta hai... 😥\nDoctor: Yeh toh umr ka taqaza hai... 🙂\nMareez: Lekin doctor sahab, meri baayi taang ki bhi toh umr utni hi hai, usme dard kyu nahi?! 😂😂😂",
    
    # 905 + 906 -> WhatsApp status purse theft
    "HJ-000905": "Police: Tumhare samne chor us ladki ka purse chheen raha tha aur tumne uski koi madad nahi ki?\nLadka: Main us ladki ko jaanta hoon... uska WhatsApp status hai – 'I can handle my own problems. Mind your own business!'\nPolice: Phir theek hai, maran de! 😂😂😂",
    
    # 1195 + 1196 + 1197 + 1198 -> Pati Patni duniya ladai joke
    "HJ-001195": "Pati (patni se): Priye, main tumse bahut pyar karta hoon.\nPatni: Toh kya main aapko nahi karti? Main toh aapke liye saari duniya se lad sakti hoon!\nPati: Lekin tum toh din-raat mujhse hi ladti rehti ho?\nPatni: Janu, aap hi toh meri duniya ho! 😜😂😂",
    
    # 1201 -> Chunav chinh joke
    "HJ-001201": "Pati: Agar main ghar aane mein late hua toh?\nBiwi: Agar time se aaye toh BJP ke chunav chinh (kamal ke phool) se swagat karungi. Thoda late huye toh Congress ke chunav chinh (panje/thappad) se... aur agar zyada late huye toh Kejriwal ka chunav chinh (jhaadu) darwaze ke peeche rakha hai, yaad rakhna! 😂😂😂",
    
    # 1204 + 1205 -> Bhole pati joke
    "HJ-001204": "Patni: Aap bahut bhole hain ji... aapko koi bhi aakar bewakoof bana deta hai!\nPati: Shuruaat toh tere baap ne ki thi! 😂😂😂",
    
    # 1207 -> 4-5 din na dikhoon joke
    "HJ-001207": "Patni: Agar main aapko 4-5 din na dikhoon toh aapko kaisa lagega?\nPati: Bahut achha lagega!\n(Phir kya... Somwar ko nahi dikhi, Mangalwar ko nahi dikhi, Budhwar ko thoda-thoda dikhna shuru hua jab aankh ki sujan kam hui!) 😂😂😂",
    
    # 1208 + 1209 -> Mandir joke
    "HJ-001208": "Patni: Shaadi ke pehle tum roz mandir jaate the, ab kya ho gaya?\nPati: Phir tumse shaadi ho gayi... aur mera bhagwan par se bharosa hi uth gaya! 😂😂😂",
    
    # 1211 -> Khwab mein ladki aayi joke
    "HJ-001211": "Pati: Kal mere khwab mein ek bahut khoobsurat ladki aayi thi... wah kya ladki thi!\nPatni: Akele aayi thi ya pati ke saath?\nPati: Akele aayi thi.\nPatni: Toh aaj se raat ko darwaza band karke sona, warna main bhi khwab mein aa jaungi belan leke! 😂😂😂",
    
    # 1212 + 1213 -> Shawl joke
    "HJ-001212": "Patni: Darling dekho na, maine ise pichhle 5 saal se nahi pehna, phir bhi iski fitting vaisi ki vaisi hi hai!\nPati: Kuch toh bhagwan se darr pagli, yeh shawl hai! 😂😂😂",
    
    # 1215 + 1216 -> Izzat karta hoon joke
    "HJ-001215": "Patni: Main aapse baat nahi karungi!\nPati: Theek hai.\nPatni: Kya tum wajah nahi jaanna chahte?\nPati: Nahi, main tumhare faisle ki poori izzat karta hoon! 😜😂😂",
    
    # 1217 + 1218 -> Leakage check joke
    "HJ-001217": "Pati: Zara paani pila do...\nPatni: Kya hua ji, pyaas lagi hai?\nPati (gusse se): Nahi, gala check karna hai ki kahin se leak toh nahi ho raha! 😂😂😂",
    
    # 1219 + 1220 -> Zubaan se try kar joke
    "HJ-001219": "Patni: Aji sunte ho? Upar se woh bag utaar dena, mera haath thoda chhota pad raha hai.\nPati: Toh apni zubaan se try karke dekh le!\n(Pati abhi hospital ke ICU ward mein admit hai!) 😂😂😂",
    
    # 1221 + 1222 -> Machhar permanent khoon joke
    "HJ-001221": "Patni: Jab main shaadi karke yahan aayi thi toh ghar mein bahut machhar the.\nPati: Haan, hamari shaadi ke baad machharon ne yeh kehkar ghar chhod diya - ab toh permanent khoon peene wali aa gayi hai! 😂😂😂",
    
    # 1224 + 1225 -> Mall shopping 40 selfie joke
    "HJ-001224": "Pati: Kahan gayab thi 4 ghante se?\nPatni: Mall mein gayi thi shopping karne!\nPati: Phir kya-kya khareeda?\nPatni: Ek hair band aur saath mein 40 selfie! 😂😂😂",
    
    # 1227 + 1228 -> Sapne mein haar joke
    "HJ-001227": "Patni: Aji sunte ho ji, mujhe sapna aaya ki aap mere liye heeron ka haar lekar aaye ho!\nPati: Theek hai pagli, toh wapis so jaa aur pehan le! 😂😂😂",
    
    # 1229 -> Facebook panchi joke
    "HJ-001229": "Pati ne office mein baithkar Facebook par post kiya: 'Panchhi banu udta phiroon mast gagan mein...'\nTabhi patni ka comment aaya: 'Dharti par aate hi 2 kilo tamatar aur 1 kilo pyaaz le aana, warna saare par kaat doongi!' 😂😂😂",
    
    # 1231 + 1232 + 1233 + 1234 -> Chai aushadhi joke
    "HJ-001231": "Patni: Chai banaoon?\nPati: Haan theek hai.\nPatni: Adrak wali?\nPati: Ok.\nPatni: Pudeena daloon?\nPati: Theek hai.\nPatni: Tulsi daal doon, sehat ke liye achhi hoti hai?\nPati: Oye bhagwan! Ek kaam kar, pyaaz aur lehsun daal ke tadka bhi laga de! Chai banani hai ya Kadha?! 😂😂😂",
    
    # 1236 + 1237 + 1238 -> Aadha maatha dukhna joke
    "HJ-001236": "Patni: Hamesha mera aadha maatha dukhta hai... lagta hai doctor ko dikhana padega.\nPati: Are usme kya batana, jitna dimaag hai utna hi toh dukhega! 😂\n(Bas tab se hi pati ka poora badan dukh raha hai!) 😜😂😂",
    
    # 1239 + 1240 + 1241 + 1242 -> Vakeel pocha joke
    "HJ-001239": "Patni: Chalo utho, chai aur nashta banane jao!\nPati uthkar seedha bahar ki taraf jaane laga.\nPatni: Kahan jaa rahe ho?\nPati: Vakeel ke paas, tumse talaq lene!\n(Thodi der baad pati wapis aakar chupchap chai banane laga)\nPatni: Kya hua ji?\nPati: Kuch nahi... dekha vakeel sahab khud pocha laga rahe the! 😂😂😂",
    
    # 1243 + 1244 -> Roti paani mein dubo kar joke
    "HJ-001243": "Pati: Kitni baar kaha hai ki khana banate waqt mobile mat chalaya kar! Dekh sabzi ka swad ekdum paani jaisa lag raha hai!\nPatni: Zyada dimaag ka dahi na karo ji! Aapko kitni baar bola hai ki khate waqt mobile mat chalaya karo... sabzi ki jagah paani mein roti dubo-dubokar khaa rahe ho! 😂😂😂",
    
    # 1245 + 1246 -> Golgappe baari joke
    "HJ-001245": "Pati-patni ek hi plate mein golgappe khaa rahe the. Ek doosre ki aankh mein aankhein daal kar patni ne romantic hokar poochha: Aise kya dekh rahe ho ji?\nPati: Thoda aaram se khaa bhagwan ke liye, meri baari hi nahi aa rahi! 😂😂😂",
    
    # 1247 + 1248 + 1249 -> Bandook sher kuta joke
    "HJ-001247": "Patni: Yeh bandook leke darwaze pe kyu khade ho?\nPati: Sher ka shikar karne jaa raha hoon!\nPatni: Toh jaate kyu nahi?\nPati: Bahar kutta khada hai! 😂😂😂",
    
    # 1250 + 1251 + 1252 + 1253 -> Lauki jaldbaazi joke
    "HJ-001250": "Patni: Bhaiya, yeh lauki kya bhav hai?\nSabziwala: 50 rupaye kilo madam.\nPatni: Aur yeh bhindi, tamatar?\nPati (piche se): Jaldi karo ji, mujhe office ke liye der ho rahi hai!\nPatni: Tum bakwas na karo! Jaldi-jaldi mein tumhare jaisa pati mila... ab sabzi khareedne mein jaldbaazi bilkul nahi karungi! 😂😂😂",
    
    # 1254 + 1255 -> Naagin gale mein joke
    "HJ-001254": "Patni ne pati ke gale mein baahein daali aur poochha: Kaisi lag rahi hoon ji?\nPati: Jaise bhagwan Shiv ke gale mein naagin lipti ho! 😂😂😂",
    
    # 1256 + 1257 -> Bedroom chaar taang shak joke
    "HJ-001256": "Patni office se aakar bedroom ka darwaza kholi toh dekha kambal mein 2 ki jagah 4 taangein nazar aa rahi thin. Usne aao dekha na taav, dande se jamkar sutai kar di!\nPeechhe se pati bola: Tere bhai-bhabhi aaye hain, maine unhe bedroom mein sulaya hai, jaa ke mil le... Moral: Aur karo bina soche shak! 😂😂😂",
    
    # 1258 + 1259 + 1260 -> Gayi bhains paani mein
    "HJ-001258": "Pati: Tum meri film mein kaam karogi?\nPatni: Haan, par scene kya hai?\nPati: Tumhe dheere-dheere paani mein jaana hoga.\nPatni: Theek hai, par film ka naam kya hai?\nPati: Gayi Bhains Paani Mein! 😂😂😂",
    
    # 1260 + 1261 -> Talaq aadhi salary joke
    "HJ-001261": "Talaq ke case mein judge sahab ne pati ko aadesh diya: Aadhi salary har mahine patni ko deni padegi.\nPati (khushi-khushi): Judge sahab, main toh taiyar hoon... kam se kam aadhi salary toh mere paas bachegi! 😂😂😂",
    
    # 1264 + 1265 -> Takli kaun hai joke
    "HJ-001264": "Patni (pati ki shirt check karte huye): Aapki shirt par toh kisi ladki ka ek bhi baal nahi mila!\nPati: Haan toh kya hua?\nPatni: Main poochhti hoon, kaun hai woh takli jiske saath ghoom rahe the?! 😂😂😂",
    
    # 1272 + 1273 -> Propose gaana joke
    "HJ-001272": "Patni: Agar tum mujhe dobara propose karoge toh kaun se gaane par karoge?\nPati: Itni shakti hamein dena daata, mann ka vishwas kamzor ho na! 😂😂😂",
    
    # 1276 + 1277 -> Daaru celebrate joke
    "HJ-001276": "Patni (pati se): Suniye ji, woh jo aadmi daru pee kar naach raha hai na, maine use 10 saal pehle reject kar diya tha!\nPati: Dekh lo bhagwan... sala abhi tak celebrate kar raha hai! 😂😂😂",
    
    # 1278 + 1279 -> Sharma ji neend ki goli joke
    "HJ-001278": "Doctor: Sharma ji, is samay aapko aaram ki sakht zaroorat hai. Main neend ki goliyaan de raha hoon, inhe roz raat ko apni patni ko khila dena! 😂😂😂",
    
    # 1283 + 1284 -> Chhota grah pittal di joke
    "HJ-001283": "Teacher: Batao agar ek chhota grah prithvi se takra jaaye toh kya hoga?\nPappu: Tann-tann ki aawaz aayegi sir!\nTeacher: Kyun be?\nPappu: Kyunki Sunny Leone ne gaaya hai - Yeh duniya pittal di! 😂😂😂",
    
    # 1286 + 1287 + 1288 -> Zinda rehne ke liye joke
    "HJ-001286": "Teacher ne Pappu se kaha: Zinda rehne ke liye kya-kya cheezein zaroori hain?\nPappu: Zinda rehne ke liye teri kasam, ek mulakat zaroori hai sanam!\n(Phir kya... de thappad de thappad!) 😂😂😂",
    
    # 1289 + 1290 -> Birbal beti dhyan do joke
    "HJ-001289": "Teacher: Birbal kaun tha?\nPappu: Pata nahi madam.\nTeacher: Padhai par dhyan do toh pata chale!\nPappu: Achha madam, yeh batao Rajesh, Vicky aur Saurav kaun hain?\nTeacher: Mujhe kya pata!\nPappu: Apni beti par dhyan do toh pata chale! 😂😂😂",
    
    # 1291 + 1292 + 1303 -> Joota mummy papa joke
    "HJ-001291": "Teacher ne Pappu se late school aane ki wajah poochhi:\nPappu: Mummy aur Papa mein ladai ho rahi thi sir.\nTeacher: Ho sakta hai, lekin usme tumhe aane mein deri kyu hui?\nPappu: Sir, mera ek joota mummy ke haath mein tha aur doosra papa ke haath mein! 😂😂😂",
    
    # 1294 + 1295 -> Customer care papa joke
    "HJ-001294": "Teacher: Pappu, tumhare papa kya kaam karte hain?\nPappu: Sir, woh roz gaaliyan khate hain!\nTeacher: Kya matlab?\nPappu: Sir, woh Customer Care Executive hain! 😂😂😂",
    
    # 1297 + 1298 -> Kiss liye joke
    "HJ-001297": "Master: Kal school kyu nahi aaye the?\nPappu: Girlfriend se milne gaya tha sir.\nMaster: Kiss liye?\nPappu: Yes sir, li thi! 😂😂😂",
    
    # 1319 + 1320 -> Chatayi bichhana joke
    "HJ-001319": "Pati: Aaj khana hum bahar khayenge!\nPatni: (Khush hokar) Theek hai ji, main 2 minute mein ready hokar aati hoon.\nPati: Theek hai pagli, main bahar aangan mein chatayi bichhata hoon! 😂😂😂",
    
    # 1321 + 1322 -> Agra petha aalu paratha joke
    "HJ-001321": "Pati: Suno! Aaj aloo ke parathe mein aloo nazar nahi aa raha!\nPatni: Chupchap khaa lo. Kabhi Agra ke pethe mein Agra nazar aata hai kya?! 😂😂😂",
    
    # 1323 + 1324 -> Mafi samjhauta joke
    "HJ-001323": "Ek baar pati-patni mein ladai ho gayi aur teen din tak baat nahi hui. Chauthe din patni aayi aur boli: Aise kab tak chalega? Chalo aapas mein samjhauta kar lete hain.\nPati: Par karna kya hoga?\nPatni: Bas tum mujhse maafi maang lo, aur main tumhe maaf kar deti hoon! 😂😂😂",
    
    # 1326 + 1327 -> Saasuma baal joke
    "HJ-001326": "Pati: Aaj khana saasuma ne banaya hai kya?\nPatni: Wah! Aapne toh bilkul sahi anuman lagaya... khana bahut tasty bana hai kya?\nPati: Nahi, hamesha khane se kaale baal nikalte the, aaj safed nikle hain! 😂😂😂",
    
    # 1328 + 1329 -> Insta pooja ID joke
    "HJ-001328": "Patni: Suno ji! Aaj shaam ko Insta ki pooja rakhi hai, aas-pados ki sabhi saheliyon ko bulaya hai. Prasad mein kya baantoon?\nPati: Meri ID baant dena, bada punya lagega! 😂😂😂",
    
    # 1330 + 1331 -> Sprite seedhi baat joke
    "HJ-001330": "Patni: Jab aap vodka peete ho toh mujhe Janu kehte ho, jab tequila peete ho toh Darling kehte ho, par aaj kameeni kyu kaha?\nPati: Aaj maine Sprite peeya hai... seedhi baat, no bakwas! 😂😂😂",
    
    # 1334 + 1335 -> Tau ji perfume joke
    "HJ-001334": "Doctor ne checkup kiya aur kaha: Tau ji, ek lambi saans leejiye.\nTau ji ne ek lambi aur gehri saans li.\nDoctor: Kaisa lag raha hai?\nTau ji: Wah doctor sahiba! Aaj kaunsa perfume laga kar aayi ho?! 😂😂😂",
    
    # 1338 + 1339 -> Girdhari lal result joke
    "HJ-001338": "Papa: Dekho beta, agar tum is baar bhi fail ho gaye toh mujhe Papa mat bolna!\nExam result ke baad...\nPapa: Beta, tumhare result ka kya hua?\nPappu: Dimaag kharab mat karo Girdhari Lal! Aapne Papa kehne ka haq kho diya hai! 😂😂😂",
    
    # 1343 + 1344 -> Zindagi laanat joke
    "HJ-001343": "Patni: Janu, tum mujhe do aisi baatein bolo, jisme se ek ko sunkar main khush ho jaoon aur doosri sunkar naraz ho jaoon!\nPati: Pehli baat – tum meri zindagi ho... aur doosri baat – laanat hai aisi zindagi par! 😂😂😂",
    
    # 1345 + 1346 -> Fresh joke
    "HJ-001345": "Shaam ko pati ke ghar aate hi patni ne kich-kich shuru kar di.\nPareshan pati: Are yaar, dinbhar ka thaka-hara aaya hoon, pehle fresh toh ho lene do!\nPatni: Main bhi dinbhar akeli thi, toh main bhi fresh hi ho rahi hoon! 😂😂😂",
    
    # 1347 + 1348 + 1349 + 1350 -> Dost eent biwi haath joke
    "HJ-001347": "Patni: Suno ji, aapke sar par khoon kyu nikal raha hai, yeh sab kaise hua?\nPati: Kya bataoon, mere dost ne eent maar di!\nPatni: Hain! Aapne kuch nahi kiya? Aap bhi maar dete us saale ko, haath mein kuch nahi tha kya?\nPati: Tha na... mere haath mein uski Biwi ka haath tha!\n(Phir kya, patni ne 2 eent uthakar aur maar di!) 😂😂😂",
}

# IDs to completely drop because they were merged into primary IDs or are website garbage/scraped filler
ids_to_drop = set([
    # Non-jokes / website filler / scraper comments
    "HJ-000593",  # "padhiye in hindi joks ko aur dil kholakar hansiye..." (website filler)
    "HJ-000622",  # Duplicate orphan line ("phir daayi tang mein hi takaliph kyu ??”")
    "HJ-000626",  # "aapki vebasait par sheyar aaikan..." (website instructions)
    "HJ-001223",  # Cut-off fragment ("Chaar cheejen insan ko...")
    "HJ-001226",  # Cut-off fragment ("pation mein khauph bana rahe...")
    "HJ-001263",  # Incomplete setup line ("Patni se pareshan Pati Ek din Pandit ji...")
    "HJ-001266",  # Cut-off fragment ("Patni – apane Pati ke saath mayake jaate hue...")
    "HJ-001267",  # Orphan ending ("Patni behosh….!")
    "HJ-001280",  # Duplicate thermometer fragment
    "HJ-001306",  # Redundant broken fragment of metro seat joke
    "HJ-001307",  # Redundant broken fragment of metro seat joke
    "HJ-001310",  # Redundant broken fragment of metro seat joke
    "HJ-001311",  # Redundant broken fragment of budhiya cow joke
    "HJ-001312",  # Redundant broken fragment of budhiya cow joke
    "HJ-001313",  # Website comment form garbage ("Thank you Jagat yadav ji...")
    "HJ-001316",  # Website SEO intro paragraph ("Chutkule in hindi: jaise kee aap sab...")
    "HJ-001317",  # Scraped fragment out of context
    "HJ-001318",  # Website comment form ("Loading… 2 thoughts on...")

    # Secondary pieces of merged jokes
    "HJ-000807",              # Website header ("Funny Quotes Hindi")
    "HJ-001194",              # Orphan punchline
    "HJ-001199",              # Orphan incomplete phone line
    "HJ-001274",              # Redundant setup line of 1275
    "HJ-001281", "HJ-001282",  # Meaningless fragment
    "HJ-000606", "HJ-000686",  # Merged into 605
    "HJ-000684", "HJ-000685",  # Merged into 683
    "HJ-000906",              # Merged into 905
    "HJ-001196", "HJ-001197", "HJ-001198",  # Merged into 1195
    "HJ-001205",              # Merged into 1204
    "HJ-001209",              # Merged into 1208
    "HJ-001213",              # Merged into 1212
    "HJ-001216",              # Merged into 1215
    "HJ-001218",              # Merged into 1217
    "HJ-001220",              # Merged into 1219
    "HJ-001222",              # Merged into 1221
    "HJ-001225",              # Merged into 1224
    "HJ-001228",              # Merged into 1227
    "HJ-001232", "HJ-001233", "HJ-001234",  # Merged into 1231
    "HJ-001237", "HJ-001238",  # Merged into 1236
    "HJ-001240", "HJ-001241", "HJ-001242",  # Merged into 1239
    "HJ-001244",              # Merged into 1243
    "HJ-001246",              # Merged into 1245
    "HJ-001248", "HJ-001249",  # Merged into 1247
    "HJ-001251", "HJ-001252", "HJ-001253",  # Merged into 1250
    "HJ-001255",              # Merged into 1254
    "HJ-001257",              # Merged into 1256
    "HJ-001259", "HJ-001260",  # Merged into 1258
    "HJ-001265",              # Merged into 1264
    "HJ-001273",              # Merged into 1272
    "HJ-001277",              # Merged into 1276
    "HJ-001279",              # Merged into 1278
    "HJ-001284",              # Merged into 1283
    "HJ-001287", "HJ-001288",  # Merged into 1286
    "HJ-001290",              # Merged into 1289
    "HJ-001292", "HJ-001303",  # Merged into 1291
    "HJ-001295",              # Merged into 1294
    "HJ-001298",              # Merged into 1297
    "HJ-001320",              # Merged into 1319
    "HJ-001322",              # Merged into 1321
    "HJ-001324",              # Merged into 1323
    "HJ-001327",              # Merged into 1326
    "HJ-001329",              # Merged into 1328
    "HJ-001331",              # Merged into 1330
    "HJ-001335",              # Merged into 1334
    "HJ-001339",              # Merged into 1338
    "HJ-001344",              # Merged into 1343
    "HJ-001346",              # Merged into 1345
    "HJ-001348", "HJ-001349", "HJ-001350",  # Merged into 1347
])

# 3. Clean general scraper junk & website boilerplate
def clean_joke_text(text):
    # Remove HTML / JS snippets
    text = re.sub(r'Δ document\.getElementById\(.*?\);?', '', text)
    text = re.sub(r'Loading…\s*Leave a Comment.*', '', text, flags=re.DOTALL)
    text = re.sub(r'Save my name, email.*', '', text, flags=re.DOTALL)
    text = re.sub(r'Notify me of.*', '', text, flags=re.DOTALL)
    
    # Remove asterisks dividers
    text = re.sub(r'\*{3,}', '', text)
    
    # Remove website header garbage like "Whatsapp Jokes in Hindi", "See Also: ...", "phani WhatsApp joks in hindi"
    header_patterns = [
        r'^(?:Whatsapp Jokes (?:Chutkule )?in Hindi\s*)+',
        r'^(?:Hindi Jokes >>\s*(?:See Also:\s*)?(?:hindi chutakule\s*)?(?:Teacher Student Jokes in Hindi\s*)?(?:WhatsApp Jokes in Hindi\s*)?)+',
        r'^(?:veri\s+)?phani WhatsApp (?:stetas\s+)?joks?(?:\s+in\s+hindi)?\s*',
        r'^(?:hasy chutakule hindi mein\s*)+',
        r'^(?:WhatsApp Jokes Status\s*)+',
        r'^(?:WhatsApp ke chutakule\s*)+',
        r'^(?:Pati par jokes\s*)+',
        r'^(?:Pati Patni (?:ke )?jokes(?:\s+in\s+hindi(?:\s+latest)?)?\s*)+',
        r'^(?:shaharee Ladka Dehaati Mahila Funny Jokes In Hindi\s*)+',
        r'^(?:Long WhatsApp Jokes in Hindi\s*)+',
        r'^(?:Ladka Ladki Funny Jokes In Hindi\s*)+',
        r'^(?:Teacher Student Funny Jokes In Hindi\s*)+',
        r'^(?:Funny Hindi Jokes\s*)+',
        r'^(?:Comedy Jokes in Hindi\s*)+',
        r'^(?:Hindi Jokes Images\s*)+',
    ]
    for hp in header_patterns:
        text = re.sub(hp, '', text, flags=re.IGNORECASE | re.MULTILINE)
    
    # Remove trailing blog links like "Read: Best jokes in hindi..."
    text = re.sub(r'Read:\s*Best jokes.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'New \d+ Funny.*', '', text, flags=re.IGNORECASE)
    
    # Normalize excessive newlines
    lines = [l.strip() for l in text.split('\n')]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    
    cleaned = '\n'.join(lines)
    return cleaned.strip()

# 4. Process dataset
final_jokes = []
dropped_count = 0
merged_count = 0
cleaned_count = 0

for j in jokes:
    jid = j['id']
    if jid in ids_to_drop:
        dropped_count += 1
        continue
    
    if jid in merge_replacements:
        j['content'] = merge_replacements[jid]
        merged_count += 1
    else:
        new_text = clean_joke_text(j['content'])
        if new_text != j['content']:
            cleaned_count += 1
        j['content'] = new_text

    final_jokes.append(j)

print(f"Dropped {dropped_count} junk/fragment jokes.")
print(f"Merged & repaired {merged_count} jokes into full jokes.")
print(f"Cleaned headers/boilerplate in {cleaned_count} jokes.")
print(f"Final joke count: {len(final_jokes)}")

# Save to jokes-master.json
with open(master_path, "w", encoding="utf-8") as f:
    json.dump(final_jokes, f, indent=2, ensure_ascii=False)
print("Updated jokes-master.json successfully.")

# Re-export clean dataset via DatasetManager
dm = DatasetManager()
dm.master_jokes = final_jokes
dm.save_all()
print("Exported dataset successfully via DatasetManager.")

# Copy clean-jokes.json to chutkule-wala/assets/jokes.json
clean_export_path = os.path.join(DATASET_DIR, "exports", "clean-jokes.json")
app_jokes_path = os.path.join(APP_DIR, "assets", "jokes.json")

import shutil
shutil.copyfile(clean_export_path, app_jokes_path)
print("Synchronized chutkule-wala/assets/jokes.json successfully.")
