import json
from pathlib import Path
ROOT=Path(__file__).parent
sources={
'windows':{'title':'Microsoft · Windows shortcuts','url':'https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows'},
'magnifier':{'title':'Microsoft · Magnifier shortcuts','url':'https://support.microsoft.com/en-us/accessibility/windows/magnifier/keyboard-shortcuts-for-magnifier'},
'chrome':{'title':'Google · Chrome keyboard shortcuts','url':'https://support.google.com/chrome/answer/157179?hl=en'},
'gmail':{'title':'Google · Print Gmail messages','url':'https://support.google.com/mail/answer/8255?co=GENIE.Platform%3DDesktop&hl=en'},
'attachments':{'title':'Google · Gmail attachments','url':'https://support.google.com/mail/answer/30719?hl=en'},
'whatsapp':{'title':'WhatsApp · Windows video calls','url':'https://faq.whatsapp.com/1862285217468140/?cms_platform=windows-desktop'},
'share':{'title':'WhatsApp · Screen sharing','url':'https://faq.whatsapp.com/1339237313658883/?cms_platform=windows-desktop'},
'permissions':{'title':'Microsoft · Camera and microphone','url':'https://support.microsoft.com/en-us/windows/privacy/windows-camera-microphone-and-privacy'},
'phone':{'title':'Microsoft · Phone Link help','url':'https://support.microsoft.com/phone-link'},
'word':{'title':'Microsoft · Word help','url':'https://support.microsoft.com/word'},
}
# Each step has an explicit visual state and target, a keyboard route, mouse route and outcome.
def S(title,keys,instruction,mouse,expected,scene,target):
 return dict(title=title,keys=keys,instruction=instruction,mouse=mouse,expected=expected,scene=scene,target=target)
lessons=[]
def L(id,cat,title,desc,steps,help=[],source='windows',tags='',before='',note=''):
 lessons.append(dict(id=id,category=cat,title=title,description=desc,steps=steps,help=help,sources=source.split(),tags=tags,before=before,note=note))
L('magnifier','देखना आसान करें','स्क्रीन बड़ी करें','Magnifier चालू करें और ज़ूम बदलें।',[
 S('Magnifier खोलें',['Win','+'],'Windows बटन दबाकर रखें और प्लस (+) दबाएँ।','Start में Magnifier खोजकर खोलें।','स्क्रीन का हिस्सा बड़ा दिखेगा।','magnifier','Zoom in'),
 S('अपने हिसाब से बड़ा करें',['Win','+'],'हर बार यही बटन दबाने पर ज़ूम बढ़ेगा। कम करने के लिए Windows और माइनस दबाएँ।','Magnifier की पट्टी में + या − दबाएँ।','लिखाई आराम से पढ़ने लायक होगी।','magnifier','Zoom in'),
 S('ज़रूरत पर बंद करें',['Win','Esc'],'Windows और Esc साथ दबाएँ। इससे केवल Magnifier बंद होगा।','Magnifier की पट्टी का Close दबाएँ।','स्क्रीन सामान्य आकार पर लौटेगी।','magnifier','Close')],['magnifier-lost'],source='magnifier',tags='zoom बड़ा magnification plus minus')
L('magnifier-settings','देखना आसान करें','ज़ूम का तरीका बदलें','पूरी स्क्रीन, lens और docked view चुनें।',[
 S('Magnifier settings खोलें',['Win','Ctrl','M'],'ये तीनों बटन साथ दबाएँ।','Settings → Accessibility → Magnifier खोलें।','Magnifier की settings खुलेंगी।','settings','Magnifier'),
 S('View चुनें',['Tab','↑ / ↓'],'Tab दबाते हुए View तक जाएँ। उपलब्ध सूची में अपनी पसंद चुनें।','View में Full screen, Lens या Docked चुनें।','चुने हुए तरीके से ज़ूम दिखेगा।','magnifier','View'),
 S('चलते समय बदलना सीखें',['Ctrl','Alt','F'],'Magnifier चल रहा हो तो Ctrl + Alt + F से full screen; L से lens; D से docked view चुन सकते हैं।','Magnifier की view सूची से बदलें।','आपके लिए सुविधाजनक view दिखेगा।','magnifier','View')],['magnifier-lost'],source='magnifier')
L('text-size','देखना आसान करें','पूरे Windows की लिखाई बड़ी करें','Text size बढ़ाएँ, बिना हर बार ज़ूम किए।',[
 S('Settings खोलें',['Win','I'],'Windows और I साथ दबाएँ।','Start → Settings चुनें।','Settings खुलेगी।','settings','Accessibility'),
 S('Text size खोजें',['Ctrl','E'],'Settings के search box पर जाएँ। Text size लिखें और सही result खोलें। Ctrl + E काम न करे तो Tab से search box चुनें।','Accessibility → Text size खोलें।','Text size का slider दिखेगा।','settings','Text size'),
 S('बड़ा करके लागू करें',['Tab','→','Enter'],'Slider पर Tab से जाएँ। दाईं arrow से आकार बढ़ाएँ। फिर Apply चुनकर Enter दबाएँ।','Slider दाईं ओर खिसकाएँ और Apply दबाएँ।','Windows की समर्थित जगहों पर लिखाई बड़ी होगी।','settings','Apply')],['settings-different'])
L('pointer','देखना आसान करें','माउस का तीर बड़ा करें','बड़ा pointer और साफ़ रंग चुनें।',[
 S('Pointer settings खोलें',['Win'],'Windows दबाएँ, Mouse pointer size लिखें और संबंधित Settings result खोलें।','Settings → Accessibility → Mouse pointer and touch खोलें।','Pointer के आकार और रंग के विकल्प दिखेंगे।','settings','Mouse pointer'),
 S('आकार और रंग चुनें',['Tab','→'],'Size slider पर जाएँ और दाईं arrow दबाएँ। फिर pointer colour के विकल्प देखें।','Size बढ़ाएँ; सफ़ेद, काला, inverted या custom colour चुनें।','माउस का तीर आसानी से दिखाई देगा।','settings','Size')],['settings-different'])
L('contrast','देखना आसान करें','ज़्यादा contrast वाली स्क्रीन','Contrast themes के विकल्प देखें।',[
 S('Contrast settings खोजें',['Win'],'Windows दबाएँ। Contrast themes लिखें और Settings result खोलें।','Settings → Accessibility → Contrast themes खोलें।','Theme के विकल्प दिखेंगे।','settings','Contrast themes'),
 S('Preview देखकर लागू करें',['Tab','↑ / ↓'],'Theme सूची में arrow से चुनें। Preview देखें, फिर Apply दबाएँ। वापसी के लिए None चुन सकते हैं।','पसंद का theme चुनें और Apply दबाएँ।','लिखाई और पृष्ठभूमि का फर्क अधिक साफ़ होगा।','settings','Apply')],['settings-different'])
L('keyboard-basics','शुरुआत और Windows','बटन और keyboard समझें','Tab, Enter, Esc और साथ दबाने वाले बटन।',[
 S('अगले विकल्प पर जाएँ',['Tab'],'Tab से अगला button या field चुनता है। चारों ओर बनी outline देखें।','जिस विकल्प को चुनना हो, उस पर क्लिक करें।','Focus की outline अगले विकल्प पर पहुँचेगी।','keyboard','Tab'),
 S('वापस जाएँ और चुनें',['Shift','Tab'],'Shift दबाए रखकर Tab दबाने से पिछले विकल्प पर लौटते हैं। Enter चुना हुआ button खोलता है।','पिछले विकल्प या button पर क्लिक करें।','आप चुने हुए विकल्प को पहचान पाएँगे।','keyboard','Enter'),
 S('मेन्यू बंद करें',['Esc'],'Esc अक्सर खुले मेन्यू या dialog को रद्द करता है। कुछ dialogs में Cancel चुनना पड़ता है।','Cancel या Close दबाएँ।','वापस पिछली स्क्रीन मिलेगी; मूल app जरूरी नहीं बंद होगा।','keyboard','Esc')],['unknown'],tags='basic keyboard tab enter escape')
L('open-app','शुरुआत और Windows','कोई ऐप खोलें','Start search से ऐप जल्दी खोलें।',[
 S('ऐप खोजें',['Win'],'Windows बटन दबाएँ और ऐप का नाम लिखें, जैसे Chrome या WhatsApp।','Start खोलें और search box में ऐप का नाम लिखें।','ऐप का result दिखेगा।','start','Search'),
 S('सही result खोलें',['↑ / ↓','Enter'],'Arrow से सही ऐप चुनें और Enter दबाएँ।','ऐप के नाम पर क्लिक करें।','ऐप खुलेगा।','start','Open')],['app-missing','signin'],tags='start search app chrome whatsapp word')
L('switch-app','शुरुआत और Windows','खुली हुई ऐप बदलें','गाइड और असली ऐप के बीच जाएँ।',[
 S('दूसरी खिड़की चुनें',['Alt','Tab'],'Alt दबाकर रखें, Tab से इच्छित खिड़की चुनें, फिर Alt छोड़ें।','Taskbar में ऐप का चिह्न दबाएँ।','दूसरी ऐप सामने आएगी।','desktop','Task view'),
 S('वापस गाइड पर आएँ',['Alt','Tab'],'दो खिड़कियों के बीच लौटने के लिए Alt + Tab एक बार दबाएँ।','Browser की इस गाइड वाली खिड़की चुनें।','आप इस कदम से आगे जारी रख पाएँगे।','desktop','Task view')],[],tags='switch window guide')
L('shutdown','शुरुआत और Windows','लैपटॉप बंद करें','पहले काम सेव करें, फिर Shut down करें।',[
 S('खुली फाइलें सेव करें',['Ctrl','S'],'जिस document में काम किया है, वहाँ Ctrl + S दबाएँ। पहली बार Save dialog आए तो नाम और जगह चुनें।','हर ऐप में Save दबाएँ।','बदलाव सेव हो जाएँगे।','word','Save'),
 S('Desktop पर जाएँ',['Win','D'],'Windows और D दबाकर desktop सामने लाएँ।','Taskbar के दाएँ किनारे Show desktop, यदि उपलब्ध हो, दबाएँ।','खुली खिड़कियाँ पीछे चली जाएँगी।','desktop','Desktop'),
 S('Shut down चुनें',['Alt','F4'],'Desktop सामने हो तभी Alt + F4 दबाएँ। सूची में Shut down चुनें, फिर Enter दबाएँ।','Start → Power → Shut down चुनें।','Windows बंद होने लगेगा।','shutdown','Shut down')],['unsaved','update-shutdown'],before='चार्जिंग केबल निकालना shutdown का तरीका नहीं है।',tags='power off बंद')
L('restart','शुरुआत और Windows','लैपटॉप Restart करें','दोबारा चालू करके साधारण दिक्कतें ठीक करें।',[
 S('काम सेव करके Desktop खोलें',['Ctrl','S'],'खुला काम सेव करें। फिर Windows + D दबाएँ।','Save करके Desktop सामने लाएँ।','अब desktop दिखेगा।','desktop','Desktop'),
 S('Restart चुनें',['Alt','F4'],'Desktop पर Alt + F4 दबाएँ। Arrow से Restart चुनकर Enter दबाएँ।','Start → Power → Restart चुनें।','लैपटॉप बंद होकर फिर चालू होगा।','shutdown','Restart')],['unsaved','update-shutdown'])
L('lock','शुरुआत और Windows','लैपटॉप Lock करें','थोड़ी देर दूर जाना हो तो।',[
 S('स्क्रीन Lock करें',['Win','L'],'दोनों बटन साथ दबाएँ। काम खुला रहेगा।','Start के account menu में Lock, जहाँ उपलब्ध हो, चुनें।','Lock screen दिखेगी।','lock','Sign in'),
 S('वापस Sign in करें',['Enter'],'Enter दबाएँ। अपना PIN या password डालें और Enter दबाएँ।','Lock screen खोलकर अपने account में sign in करें।','पहले का काम वापस सामने होगा।','lock','PIN')],['signin'])
L('wifi','इंटरनेट और डिवाइस','Wi-Fi से जुड़ें','नेटवर्क चुनें और password डालें।',[
 S('Quick Settings खोलें',['Win','A'],'Windows और A साथ दबाएँ।','Taskbar में Wi-Fi, sound या battery वाला समूह दबाएँ।','Quick Settings panel खुलेगा।','quick','Wi-Fi'),
 S('नेटवर्क सूची खोलें',['Tab','Enter'],'Wi-Fi बंद हो तो चालू करें। फिर Wi-Fi के साथ वाले arrow पर Tab से जाएँ और Enter दबाएँ।','Wi-Fi tile के पास arrow दबाएँ।','पास के नेटवर्क दिखेंगे।','wifi','Show available networks'),
 S('अपना नेटवर्क चुनें',['Tab','↑ / ↓','Enter'],'अपने नेटवर्क तक जाएँ, Enter दबाएँ और Connect चुनें।','घर के Wi-Fi का नाम, फिर Connect दबाएँ।','Password माँगा जा सकता है।','wifi','Connect'),
 S('Password डालें',['Tab','Enter'],'Password field में सही password लिखें। Next पर जाएँ और Enter दबाएँ।','Password लिखें और Next दबाएँ।','नेटवर्क के नीचे Connected दिखेगा।','wifi','Next')],['wifi-password','wifi-none','wifi-no-internet'],tags='wifi wi-fi internet network connect')
L('bluetooth','इंटरनेट और डिवाइस','Bluetooth डिवाइस जोड़ें','हेडफोन, speaker या mouse pair करें।',[
 S('डिवाइस Pairing में रखें',[],'डिवाइस के निर्देश के अनुसार pairing mode चालू करें; केवल power on पर्याप्त नहीं होता।','डिवाइस का pairing button दबाएँ।','डिवाइस की बत्ती या आवाज़ pairing बताएगी।','bluetooth','Pairing mode'),
 S('Bluetooth settings खोलें',['Win'],'Windows दबाएँ। Bluetooth settings लिखें और संबंधित result खोलें।','Settings → Bluetooth & devices खोलें।','Bluetooth का switch और Add device दिखेगा।','bluetooth','Add device'),
 S('नया डिवाइस खोजें',['Tab','Enter'],'Bluetooth On करें। Add device चुनें, फिर Bluetooth चुनें।','Add device → Bluetooth दबाएँ।','डिवाइस की सूची खुलेगी।','bluetooth','Bluetooth'),
 S('सही नाम चुनें',['Tab','Enter'],'डिवाइस का नाम चुनें। Code दिखे तो दोनों ओर मिलाएँ, फिर Pair या Connect करें।','सही डिवाइस, फिर Pair / Connect / Done दबाएँ।','Paired या Connected दिखेगा।','bluetooth','Pair')],['bluetooth-none','pair-code'],source='windows',tags='headphone speaker pair')
L('sound','इंटरनेट और डिवाइस','आवाज़ और speaker चुनें','Volume, mute और output देखें।',[
 S('आवाज़ की settings खोलें',['Win','I'],'Settings में System → Sound खोलें। Search box में Sound लिखकर भी पहुँच सकते हैं।','Settings → System → Sound खोलें।','Volume और Output के विकल्प दिखेंगे।','settings','Sound'),
 S('सही Output चुनें',['Tab','↑ / ↓'],'Output में Speakers या जुड़े हुए headphones चुनें। Volume slider पर arrow से आवाज़ बदलें।','Output device चुनें और Volume बढ़ाएँ।','आवाज़ सही device से सुनाई देगी।','settings','Output')],['no-sound'],tags='volume speaker headphones mute')
L('battery','इंटरनेट और डिवाइस','बैटरी देखें','कितनी battery बची है और charging हो रही है या नहीं।',[
 S('Quick Settings खोलें',['Win','A'],'Windows और A दबाएँ। नीचे battery percentage देखें।','Taskbar के battery icon पर mouse रोकें, या उसे दबाएँ।','प्रतिशत दिखेगा।','quick','Battery'),
 S('पूरी जानकारी खोलें',['Win','I'],'System → Power & battery खोलें। Charging और battery level देखें।','Settings → System → Power & battery चुनें।','Battery की जानकारी मिलेगी।','settings','Power & battery')],[],tags='charging percentage')
L('hotspot','इंटरनेट और डिवाइस','फोन के Hotspot से जुड़ें','फोन का mobile data लैपटॉप पर इस्तेमाल करें।',[
 S('फोन में Hotspot चालू करें',[],'फोन में Mobile data और Personal hotspot / Mobile Hotspot चालू करें। नाम और password देख लें।','फोन की Settings में Hotspot खोजें; रास्ता फोन के अनुसार बदलता है।','फोन का नेटवर्क नाम तैयार होगा।','phone','Hotspot'),
 S('लैपटॉप में नेटवर्क चुनें',['Win','A'],'Wi-Fi के arrow से नेटवर्क सूची खोलें और अपने फोन का नाम चुनें।','Wi-Fi सूची में फोन का hotspot चुनें।','Connect का विकल्प दिखेगा।','wifi','Connect'),
 S('जुड़ें और काम के बाद बंद करें',['Tab','Enter'],'Connect चुनें, फोन का hotspot password डालें और Next दबाएँ। काम के बाद फोन में hotspot बंद करें।','Password डालकर जुड़ें। बाद में फोन पर hotspot बंद करें।','Connected दिखेगा। Mobile data खर्च होगा।','wifi','Next')],['wifi-password','wifi-no-internet'],tags='phone tether internet')
L('phone-link','इंटरनेट और डिवाइस','Phone Link से फोन जोड़ें','Android फोन और Windows का शुरुआती setup।',[
 S('Phone Link खोलें',['Win'],'Windows दबाएँ। Phone Link लिखें और ऐप खोलें।','Start → Phone Link खोलें।','फोन चुनने या sign in की स्क्रीन मिलेगी।','phone','Phone Link'),
 S('Android चुनें और निर्देश पढ़ें',['Tab','Enter'],'Android चुनें। माँगने पर अपना Microsoft account sign in करें।','Android दबाएँ और setup जारी रखें।','QR code या pairing के निर्देश मिलेंगे।','phone','Android'),
 S('फोन से Link करें',[],'फोन में Link to Windows खोलें। QR scan या स्क्रीन पर दिए pairing तरीके से जुड़ें।','फोन की Settings में Link to Windows भी खोज सकते हैं।','दोनों devices जुड़ने की पुष्टि करेंगे।','phone','Link to Windows'),
 S('अनुमतियाँ समझकर चुनें',[],'Notifications, photos, calls जैसे विकल्पों में केवल जिस feature की जरूरत है उसकी अनुमति दें।','हर अनुमति का विवरण पढ़कर अपना विकल्प चुनें।','चुनी हुई सुविधाएँ उपलब्ध होंगी।','phone','Permissions')],['app-missing','signin','pair-code'],source='phone',note='फोन और ऐप के version के अनुसार file transfer और दूसरे features बदलते हैं।',tags='android oneplus link windows')
L('phone-file','इंटरनेट और डिवाइस','Phone Link से फाइल भेजें','समर्थित devices पर Share का तरीका।',[
 S('पहले pairing जाँचें',['Win'],'Phone Link खोलें और फोन connected होने की पुष्टि करें।','Phone Link में अपने फोन की स्थिति देखें।','फोन connected होगा।','phone','Phone Link'),
 S('लैपटॉप से फोन भेजें',['Shift','F10'],'File Explorer में फाइल चुनें। Shift + F10 से menu खोलें। Share में Phone Link उपलब्ध हो तो चुनें।','फाइल पर right click → Share → Phone Link चुनें।','Transfer की स्थिति मिलेगी।','files','Share'),
 S('फोन से लैपटॉप भेजें',[],'फोन पर फाइल चुनकर Share खोलें। Link to Windows / Send to PC उपलब्ध हो तो अपना PC चुनें।','फोन के Share menu का प्रयोग करें।','फाइल मिलने की सूचना आएगी; ऐप बताए हुए folder में देखें।','phone','Send to PC')],['phone-transfer','wifi-no-internet'],source='phone',before='यह सुविधा हर Android फोन या पुराने app version में उपलब्ध नहीं होती।',tags='transfer android photo')
L('files-open','फाइल और फोल्डर','फाइल और Downloads खोजें','File Explorer में सही जगह पहुँचें।',[
 S('File Explorer खोलें',['Win','E'],'Windows और E दबाएँ।','Taskbar का पीला folder दबाएँ।','File Explorer खुलेगा।','files','Home'),
 S('Downloads पर जाएँ',['Alt','D'],'Address bar में %USERPROFILE%\\Downloads लिखें और Enter दबाएँ।','बाईं ओर Downloads चुनें।','डाउनलोड की हुई फाइलें दिखेंगी।','files','Downloads'),
 S('फाइल खोलें',['↑ / ↓','Enter'],'Arrow से फाइल चुनें। Enter से खोलें। जरूरत हो तो पहला अक्षर लिखकर नाम खोजें।','फाइल पर double click करें।','फाइल उससे जुड़े ऐप में खुलेगी।','files','Document.pdf')],['open-with','file-missing'],tags='download folder explorer')
L('new-folder','फाइल और फोल्डर','नया फोल्डर बनाएँ','अपनी फाइलें व्यवस्थित रखें।',[
 S('जगह खोलें',['Win','E'],'File Explorer में Documents या इच्छित जगह खोलें।','File Explorer में सही folder खोलें।','चुनी हुई जगह की फाइलें दिखेंगी।','files','Documents'),
 S('Folder बनाएँ',['Ctrl','Shift','N'],'तीनों बटन साथ दबाएँ। नया नाम लिखें और Enter दबाएँ।','खाली जगह पर right click → New → Folder चुनें।','आपके दिए नाम का folder बनेगा।','files','New folder')],['folder-exists'],tags='create directory')
L('rename','फाइल और फोल्डर','फाइल का नाम बदलें','Rename से पहचानने लायक नाम रखें।',[
 S('फाइल चुनें',['Win','E'],'सही folder खोलें। Arrow से फाइल चुनें।','फाइल पर एक बार क्लिक करें।','फाइल selected होगी।','files','Document.pdf'),
 S('नाम बदलें',['F2'],'F2 दबाएँ। नाम लिखें और Enter दबाएँ। .pdf या .docx जैसे extension को न बदलें।','Right click → Rename चुनें।','नया नाम दिखाई देगा।','files','Rename')],['extension','folder-exists'])
L('copy-move','फाइल और फोल्डर','फाइल Copy या Move करें','एक जगह से दूसरी जगह ले जाएँ।',[
 S('फाइल चुनें और Copy करें',['Ctrl','C'],'चुनी हुई फाइल पर Ctrl + C दबाएँ। Move करना हो तो Ctrl + X दबाएँ।','Right click में Copy या Cut चुनें।','फाइल clipboard में तैयार होगी।','files','Copy'),
 S('नई जगह खोलें',['Alt','D'],'Destination folder खोलें। उदाहरण: Documents।','चाही हुई जगह का folder खोलें।','नई जगह की सूची दिखेगी।','files','Documents'),
 S('Paste करें',['Ctrl','V'],'Ctrl + V दबाएँ और transfer पूरा होने दें।','Right click → Paste चुनें।','फाइल नई जगह दिखेगी। Copy में मूल फाइल वहीं रहेगी।','files','Paste')],['replace-file','permission','disk-full'],tags='cut paste transfer')
L('delete-restore','फाइल और फोल्डर','हटाएँ और वापस पाएँ','Delete, Undo और Recycle Bin।',[
 S('फाइल ध्यान से चुनें',['Delete'],'स्थानीय साधारण फाइल चुनकर Delete दबाएँ। Confirm आए तो नाम जाँचें। Shift + Delete का प्रयोग न करें।','Right click → Delete चुनें।','आमतौर पर फाइल Recycle Bin में जाएगी।','files','Delete'),
 S('गलती हो तो तुरंत Undo करें',['Ctrl','Z'],'उसी File Explorer खिड़की में तुरंत Ctrl + Z दबाएँ।','Right click → Undo Delete, यदि उपलब्ध हो, चुनें।','हटाई हुई फाइल वापस आ सकती है।','files','Undo'),
 S('बाद में Recycle Bin देखें',['Win'],'Start search में Recycle Bin खोजकर खोलें। फाइल चुनें, Shift + F10 दबाएँ और Restore चुनें।','Recycle Bin में फाइल पर right click → Restore चुनें।','फाइल पुरानी जगह वापस जाएगी।','files','Restore')],['permanent-delete','file-missing'],before='USB, network या बहुत बड़ी फाइलें सीधे स्थायी रूप से हट सकती हैं। Delete के संदेश को पढ़ें।')
L('find-file','फाइल और फोल्डर','नाम से फाइल ढूँढें','सही folder में search करें।',[
 S('जिस जगह खोजना है वह खोलें',['Win','E'],'Downloads, Documents या This PC चुनें। This PC की search में अधिक समय लग सकता है।','File Explorer में खोजने वाली जगह खोलें।','सही folder सामने होगा।','files','Documents'),
 S('Search में नाम लिखें',['Ctrl','E'],'Ctrl + E दबाएँ, फाइल के नाम का कुछ हिस्सा लिखें और Enter दबाएँ।','ऊपर दाईं ओर search field में नाम लिखें।','मिलते-जुलते results दिखेंगे।','files','Search'),
 S('सही फाइल पहचानें',['↑ / ↓','Enter'],'नाम, तारीख और जगह देखकर सही फाइल खोलें।','सही result पर double click करें।','चुनी हुई फाइल खुलेगी।','files','Document.pdf')],['file-missing'])
L('usb','फाइल और फोल्डर','USB से फाइल कॉपी करें','Drive पहचानें और सुरक्षित निकालें।',[
 S('USB लगाकर पहचानें',['Win','E'],'USB लगाएँ। File Explorer में This PC खोलें और सही drive का नाम देखें।','USB drive को double click करें।','USB की फाइलें दिखेंगी।','files','USB drive'),
 S('Copy और Paste करें',['Ctrl','C'],'फाइल चुनकर Ctrl + C दबाएँ। PC का destination folder खोलकर Ctrl + V दबाएँ।','Copy → destination → Paste करें।','Copy पूरा होने पर फाइल PC में दिखेगी।','files','Paste'),
 S('सुरक्षित निकालें',['Shift','F10'],'Copy पूरा हो जाए और फाइलें बंद हों। This PC में USB चुनें; context menu में Eject चुनें।','USB drive पर right click → Eject चुनें।','Safe to remove का संदेश मिले तो USB निकालें।','files','Eject')],['usb-format','usb-busy','replace-file'])
L('chrome-open','Chrome और वेब','वेबसाइट खोलें या Search करें','Address bar से सीधे शुरू करें।',[
 S('Chrome खोलें',['Win'],'Windows दबाएँ, Chrome लिखें, सही ऐप चुनें और Enter दबाएँ।','Chrome का चिह्न खोलें।','Chrome खुलेगा।','chrome','Address bar'),
 S('पता या सवाल लिखें',['Ctrl','L'],'Ctrl + L दबाएँ। वेबसाइट का पता या अपना सवाल लिखें और Enter दबाएँ।','ऊपर address bar पर क्लिक करके लिखें।','वेबसाइट या search results खुलेंगे।','chrome','Address bar'),
 S('लिंक खोलें',['Tab','Enter'],'Tab से इच्छित link पर जाएँ और Enter दबाएँ। Shift + Tab से पीछे जाएँ।','इच्छित result पर क्लिक करें।','चुना हुआ पन्ना खुलेगा।','chrome','Search result')],['chrome-default','cookie','ssl','offline'],source='chrome',tags='browser google search address url')
L('chrome-zoom','Chrome और वेब','वेब पन्ने की लिखाई बड़ी करें','Chrome zoom, Windows zoom से अलग है।',[
 S('पन्ना बड़ा करें',['Ctrl','+'],'Chrome में Ctrl और plus दबाएँ। जितनी जरूरत हो दोहराएँ।','Chrome menu → Zoom में + दबाएँ।','इस वेबसाइट की सामग्री बड़ी होगी।','chrome','Zoom'),
 S('कम या सामान्य करें',['Ctrl','−'],'कम करने के लिए Ctrl और minus दबाएँ। सामान्य आकार के लिए Ctrl + 0 दबाएँ।','Zoom में − दबाएँ; 100% सामान्य आकार है।','आपके लिए सही आकार दिखेगा।','chrome','Zoom')],[],source='chrome',tags='zoom text size')
L('chrome-tabs','Chrome और वेब','Tabs खोलें और बदलें','कई पन्नों के बीच काम करें।',[
 S('नई Tab खोलें',['Ctrl','T'],'Ctrl + T दबाएँ। नया पता लिखकर Enter दबाएँ।','ऊपर tabs के पास + दबाएँ।','नई tab खुलेगी।','chrome','New tab'),
 S('Tab बदलें',['Ctrl','Tab'],'Ctrl + Tab से अगली tab; Ctrl + Shift + Tab से पिछली tab चुनें।','ऊपर tab के नाम पर क्लिक करें।','दूसरा पन्ना सामने आएगा।','chrome','New tab'),
 S('बंद करें या वापस लाएँ',['Ctrl','W'],'Ctrl + W वर्तमान tab बंद करता है। गलती से बंद हो तो Ctrl + Shift + T दबाएँ।','Tab का close दबाएँ।','पिछली tab सामने होगी या बंद tab वापस खुलेगी।','chrome','Close tab')],['unsaved'],source='chrome')
L('chrome-back','Chrome और वेब','पिछले पन्ने पर लौटें','Back, Forward और Reload सीखें।',[
 S('पिछला पन्ना खोलें',['Alt','←'],'Alt और बाईं arrow दबाएँ।','ऊपर Back arrow दबाएँ।','पहले देखा हुआ पन्ना खुलेगा।','chrome','Back'),
 S('वापस आगे जाएँ',['Alt','→'],'Alt और दाईं arrow दबाएँ।','Forward arrow दबाएँ।','अगला पन्ना लौटेगा।','chrome','Forward'),
 S('पन्ना फिर लोड करें',['Ctrl','R'],'लोड अटक गया हो तो Ctrl + R दबाएँ। भरे हुए form में पहले लिखी जानकारी का ध्यान रखें।','Reload button दबाएँ।','पन्ना फिर से लोड होगा।','chrome','Reload')],['resubmit','offline'],source='chrome')
L('chrome-find','Chrome और वेब','पन्ने में शब्द ढूँढें','लंबे पन्ने में जल्दी सही जगह पहुँचें।',[
 S('Find खोलें',['Ctrl','F'],'Ctrl + F दबाकर खोजने वाला शब्द लिखें।','Chrome menu → Find and edit → Find चुनें, यदि दिखे।','मिलते हुए शब्द highlight होंगे।','chrome','Find'),
 S('अगला मिलान चुनें',['Enter'],'Enter से अगला; Shift + Enter से पिछला मिलान चुनें। Esc से Find बंद करें।','Find box के arrows दबाएँ।','पन्ना संबंधित शब्द तक जाएगा।','chrome','Find')],[],source='chrome')
L('chrome-downloads','Chrome और वेब','डाउनलोड की हुई फाइल पाएँ','Download history और folder खोलें।',[
 S('Downloads खोलें',['Ctrl','J'],'Chrome में Ctrl + J दबाएँ।','Chrome menu → Downloads चुनें।','Downloads की सूची खुलेगी।','downloads','Downloads'),
 S('फाइल या folder खोलें',['Tab','Enter'],'पूरी हुई download चुनें। Show in folder से Windows वाला folder खुलेगा।','फाइल या Show in folder दबाएँ।','फाइल या उसकी जगह खुलेगी।','downloads','Show in folder')],['download-blocked','download-failed','file-missing'],source='chrome',tags='pdf downloaded')
L('chrome-bookmark','Chrome और वेब','पसंदीदा वेबसाइट सेव करें','Bookmark से बार-बार पता न लिखना पड़े।',[
 S('वेबसाइट Bookmark करें',['Ctrl','D'],'सही पन्ने पर Ctrl + D दबाएँ। नाम पढ़ें और Done चुनें।','Address bar के star पर क्लिक करें, फिर Done दबाएँ।','Bookmark सेव होगा।','chrome','Bookmark'),
 S('Bookmarks दिखाएँ',['Ctrl','Shift','B'],'इससे bookmarks bar दिखाई या छिपाई जाती है।','Chrome menu में Bookmarks and lists देखें।','सेव किए हुए पन्ने चुन सकेंगे।','chrome','Bookmarks bar')],[],source='chrome')
L('gmail-open','Gmail और PDF','Gmail खोलें और मेल खोजें','Inbox में सही संदेश तक पहुँचें।',[
 S('Gmail खोलें',['Ctrl','L'],'Chrome में mail.google.com लिखें और Enter दबाएँ। जरूरत हो तो सही Google account में sign in करें।','Gmail वेबसाइट खोलें।','आपका Inbox दिखेगा।','gmail','Inbox'),
 S('मेल Search करें',['Tab','Enter'],'Search mail field पर Tab से जाएँ। भेजने वाले का नाम या विषय लिखकर Enter दबाएँ।','ऊपर Search mail में लिखें।','संबंधित ईमेल दिखेंगे।','gmail','Search mail'),
 S('सही संदेश खोलें',['Tab','Enter'],'सही subject तक जाएँ और Enter दबाएँ।','ईमेल के subject पर क्लिक करें।','संदेश की सामग्री दिखेगी।','gmail','Message')],['signin','offline'],source='gmail',note='इस गाइड में Gmail के वैकल्पिक single-letter shortcuts पर निर्भर नहीं किया गया है।')
L('gmail-pdf','Gmail और PDF','ईमेल को PDF में सेव करें','सिर्फ संदेश या पूरी बातचीत चुनें।',[
 S('सही ईमेल खोलें',['Tab','Enter'],'Gmail में सेव करने वाला ईमेल खोलें। एक ही conversation में कई messages हों तो इच्छित message खोलें।','ईमेल का subject खोलें।','संदेश दिखेगा।','gmail','Message'),
 S('ईमेल का Print विकल्प खोलें',['Tab','Enter'],'उस message के More menu तक Tab से जाएँ। Print चुनें। पूरी conversation के लिए Print all चुनें।','Message के तीन dots → Print; पूरी बातचीत के लिए Print all दबाएँ।','Message की print view खुलेगी।','gmail','Print'),
 S('Print dialog न खुले तो खोलें',['Ctrl','P'],'केवल message की print view सामने हो और dialog न खुला हो तभी Ctrl + P दबाएँ।','Print view का Print button दबाएँ।','Chrome का print preview दिखेगा।','print','Destination'),
 S('Save as PDF चुनें',['Tab','↑ / ↓'],'Destination सूची खोलकर Save as PDF चुनें। Preview में सही message जाँचें।','Destination → Save as PDF चुनें।','नीचे Save button दिखेगा।','print','Save as PDF'),
 S('नाम और जगह चुनें',['Tab','Enter'],'Save दबाएँ। Windows dialog में File name लिखें, सही folder चुनें, फिर Save दबाएँ।','File name और folder चुनकर Save दबाएँ।','PDF चुनी हुई जगह पर सेव होगी।','save','Save')],['confidential','print-blocked','replace-file','file-missing','save-permission'],source='gmail chrome',tags='email mail download pdf print',note='Download message से .eml मिलती है; PDF के लिए Print → Save as PDF का प्रयोग करें।')
L('gmail-attachment','Gmail और PDF','ईमेल का Attachment डाउनलोड करें','PDF या दूसरी संलग्न फाइल सेव करें।',[
 S('Attachment तक जाएँ',['Tab'],'Gmail में संदेश खोलें और नीचे attached file तक जाएँ।','Message के नीचे attachment देखें।','Attachment का नाम दिखेगा।','gmail','Attachment'),
 S('Download चुनें',['Tab','Enter'],'Attachment का Download button चुनें और Enter दबाएँ।','Attachment पर Download arrow दबाएँ।','Download शुरू होगी।','gmail','Download'),
 S('फाइल ढूँढें',['Ctrl','J'],'Chrome downloads में पूरी हुई फाइल देखें। Show in folder से जगह खोलें।','Downloads list में फाइल देखें।','आप फाइल खोल सकेंगे।','downloads','Show in folder')],['confidential','download-blocked','download-failed'],source='attachments chrome')
L('gmail-compose','Gmail और PDF','नया ईमेल और Attachment भेजें','पता, विषय, संदेश और फाइल जाँचकर भेजें।',[
 S('Compose खोलें',['Tab','Enter'],'Gmail में Compose button चुनें।','बाईं ओर Compose दबाएँ।','New Message खुलेगा।','gmail-compose','Compose'),
 S('पता और संदेश लिखें',['Tab'],'To में पूरा email address लिखें। Subject और message field में Tab से जाएँ और लिखें।','To, Subject और message में जानकारी भरें।','ईमेल तैयार दिखेगा।','gmail-compose','To'),
 S('फाइल जोड़ें',['Tab','Enter'],'Attach files button चुनें। Windows file picker में फाइल चुनकर Open दबाएँ।','Paperclip → फाइल चुनें → Open दबाएँ।','Upload पूरी होने पर फाइल का नाम दिखेगा।','open-file','Open'),
 S('जाँचकर भेजें',['Tab','Enter'],'Recipient, subject, message और attachment जाँचें। सही हो तभी Send चुनें।','Send button दबाएँ।','Message sent की पुष्टि मिलेगी।','gmail-compose','Send')],['attachment-large','missing-attachment','signin','offline'],source='attachments',before='यह अभ्यास ऐप कोई असली ईमेल नहीं भेजती। असली Gmail में भेजने से पहले recipient ज़रूर जाँचें।')
L('pdf-read','Gmail और PDF','PDF पढ़ें और बड़ा करें','Chrome PDF viewer में page और zoom।',[
 S('PDF खोलें',['Enter'],'File Explorer में PDF चुनकर Enter दबाएँ। दूसरे ऐप में खुले तो उसके zoom controls देखें।','PDF पर double click करें।','PDF viewer खुलेगा।','pdf','Document.pdf'),
 S('Zoom और page चुनें',['Tab'],'Viewer की toolbar में zoom या page number चुनें। बहुत छोटा हो तो Windows Magnifier भी उपयोग कर सकते हैं।','ऊपर zoom + और page field इस्तेमाल करें।','पन्ना बड़े आकार में दिखेगा।','pdf','Zoom'),
 S('शब्द खोजें',['Ctrl','F'],'Ctrl + F दबाकर शब्द लिखें। Scanned image वाली PDF में text search उपलब्ध न भी हो।','Find विकल्प चुनें।','Text PDF में मिले शब्द दिखेंगे।','pdf','Find')],['pdf-password','pdf-scanned','open-with'],source='chrome')
L('print-file','Gmail और PDF','Document Print करें','सही printer और pages चुनें।',[
 S('Print dialog खोलें',['Ctrl','P'],'Document सामने हो तो Ctrl + P दबाएँ।','ऐप में File → Print चुनें।','Print settings खुलेंगी।','print','Destination'),
 S('Printer और pages चुनें',['Tab'],'अपने printer का नाम चुनें। Copies, pages और preview जाँचें।','Destination / Printer सूची में अपना printer चुनें।','सही print settings दिखेंगी।','print','Printer'),
 S('Print भेजें',['Tab','Enter'],'Print button चुनें। Printer में कागज़ और connection होना चाहिए।','Print दबाएँ।','Printer काम शुरू करेगा या queue में job दिखेगी।','print','Print')],['printer-offline','print-blocked'],source='windows chrome')
L('whatsapp-link','WhatsApp','WhatsApp में फोन Link करें','Windows app का शुरुआती setup।',[
 S('WhatsApp खोलें',['Win'],'Windows दबाएँ, WhatsApp लिखें और ऐप खोलें।','WhatsApp ऐप खोलें।','Setup या QR screen दिखेगी।','whatsapp-link','Get started'),
 S('फोन में Linked devices खोलें',[],'अपने फोन पर WhatsApp खोलें। Android में menu, या iPhone में Settings से Linked devices खोलें।','Linked devices → Link a device चुनें।','फोन QR scan करने के लिए तैयार होगा।','phone','Linked devices'),
 S('PC का QR scan करें',[],'फोन से अपने PC पर WhatsApp वाला QR scan करें। Chats sync होने दें।','फोन का camera PC के QR की ओर रखें।','Windows app में chats दिखेंगी।','whatsapp-link','QR code')],['qr-expired','offline'],source='whatsapp',tags='qr login setup')
L('whatsapp-message','WhatsApp','किसी को Message भेजें','सही contact चुनें और संदेश लिखें।',[
 S('सही chat खोलें',['Tab'],'Search या chat list से व्यक्ति का नाम ढूँढें। ऊपर नाम जाँचकर chat खोलें।','Search field में नाम लिखें और सही chat चुनें।','व्यक्ति का नाम ऊपर दिखेगा।','whatsapp','Search'),
 S('संदेश लिखें',['Tab'],'Message field पर जाएँ और अपना संदेश लिखें।','Type a message वाले field में लिखें।','लिखा हुआ संदेश दिखेगा।','whatsapp','Type a message'),
 S('भेजें',['Enter'],'व्यक्ति और संदेश जाँचें। Enter से भेजें; नई लाइन के लिए आमतौर पर Shift + Enter होता है।','Send button दबाएँ।','संदेश chat में दिखेगा।','whatsapp','Send')],['whatsapp-offline'],source='whatsapp',note='ऐप versions में button का स्थान बदल सकता है; यहाँ कोई निश्चित Tab-count नहीं माना गया है।')
L('whatsapp-file','WhatsApp','WhatsApp पर फाइल भेजें','Document या photo attach करें।',[
 S('सही chat चुनें',['Tab'],'जिसे फाइल भेजनी है उसकी chat खोलें। ऊपर नाम जाँचें।','सही contact चुनें।','सही व्यक्ति की chat दिखेगी।','whatsapp','Contact'),
 S('Attach खोलें',['Tab','Enter'],'Attach / plus button तक जाएँ। Document या Photos and videos चुनें।','Attach / + → Document चुनें।','File picker खुलेगा।','whatsapp','Attach'),
 S('फाइल चुनें',['Tab','Enter'],'File picker में इच्छित फाइल चुनें और Open दबाएँ।','सही फाइल → Open दबाएँ।','Attachment preview दिखेगा।','open-file','Open'),
 S('Preview देखकर Send करें',['Tab','Enter'],'फाइल का नाम और recipient जाँचें, फिर Send दबाएँ।','Preview में Send दबाएँ।','Upload के बाद फाइल chat में दिखेगी।','whatsapp','Send')],['whatsapp-offline','file-missing','attachment-large'],source='whatsapp')
L('whatsapp-call','WhatsApp','Voice या Video call करें','Contact, microphone और camera के साथ।',[
 S('Contact खोलें',['Tab'],'WhatsApp में सही व्यक्ति की chat खोलें।','सही chat चुनें।','Contact का नाम ऊपर दिखेगा।','whatsapp','Contact'),
 S('Call शुरू करें',['Tab','Enter'],'Voice call या Video call button तक जाएँ और Enter दबाएँ।','ऊपर phone या video camera button दबाएँ।','Call window या permission prompt खुलेगा।','whatsapp','Video call'),
 S('Permission आए तो पढ़ें',[],'Microphone और video के लिए camera की अनुमति केवल इस अपेक्षित WhatsApp call के लिए दें। Windows settings की जरूरत हो तो नीचे मदद देखें।','WhatsApp के अपेक्षित permission prompt में विकल्प चुनें।','Ringing या connected call दिखेगी।','call','Microphone'),
 S('Mute या End call चुनें',['Tab','Enter'],'Call controls में Microphone, Camera और End call के labels देखें। संबंधित button चुनें।','Microphone से mute; लाल phone से call समाप्त करें।','चुने हुए action की स्थिति बदलेगी।','call','End call')],['mic-camera','no-sound','call-unavailable','whatsapp-offline'],source='whatsapp permissions')
L('whatsapp-share','WhatsApp','Video call में Screen share करें','सही window चुनें और फिर sharing बंद करें।',[
 S('पहले video call जोड़ें',['Tab','Enter'],'WhatsApp में व्यक्ति की chat खोलें और video call शुरू करें। Call connect होने दें।','Video call button दबाएँ।','जुड़ी हुई video call दिखेगी।','call','Video call'),
 S('Share screen खोजें',['Tab','Enter'],'Call controls में Share screen देखें। न दिखे तो More / तीन dots menu खोलें और Share screen चुनें।','Share screen या More → Share screen दबाएँ।','Share करने के विकल्प दिखेंगे।','call','Share screen'),
 S('कौन-सी चीज़ दिखानी है चुनें',['Tab','↑ / ↓'],'एक window या पूरी screen के विकल्प आएँ तो इच्छित चीज़ चुनें। निजी messages या documents सामने न रखें।','Window / screen preview चुनें।','चुना हुआ preview दिखेगा।','share','Window'),
 S('Prompt पढ़कर शुरू करें',['Tab','Enter'],'जो content सामने वाले को दिखेगा उसे जाँचें। फिर Share / Start screen sharing चुनें।','Share या Start screen sharing दबाएँ।','Sharing चलने का indicator दिखेगा।','share','Share'),
 S('काम पूरा हो तो Stop करें',['Tab','Enter'],'WhatsApp call में लौटें। Stop sharing चुनें और sharing समाप्त होने की पुष्टि करें।','Stop sharing दबाएँ।','Screen sharing बंद होगी; call जारी रह सकती है।','call','Stop sharing')],['mic-camera','share-missing','share-warning','share-black','whatsapp-offline'],source='share whatsapp',before='आपकी साझा की गई screen सामने वाला देख सकता है। पहले तय करें कि कौन-सी window दिखानी है।',note='यह Windows ऐप की सामान्य प्रक्रिया है। Picker और buttons ऐप version के अनुसार अलग हो सकते हैं। इस web app से असली screen share शुरू नहीं होता।',tags='screen sharing video call')
L('whatsapp-download','WhatsApp','मिली हुई फाइल सेव करें','Download और Save as का उपयोग करें।',[
 S('फाइल वाली chat खोलें',['Tab'],'सही chat में attachment ढूँढें। नाम और भेजने वाला देखें।','Attachment वाली chat खोलें।','फाइल का नाम या preview दिखेगा।','whatsapp','Attachment'),
 S('Download / Save as चुनें',['Tab','Enter'],'फाइल पर Download या उसके menu में Save as देखें। उपलब्ध विकल्प ऐप version पर निर्भर करेगा।','Download arrow या attachment menu → Save as चुनें।','Download शुरू होगी या save dialog खुलेगा।','whatsapp','Download'),
 S('जगह देखें',['Win','E'],'चुने हुए folder या Downloads में फाइल देखें।','File Explorer में Downloads खोलें।','फाइल उपलब्ध होगी।','files','Downloads')],['download-failed','file-missing'],source='whatsapp')
L('word-new','Word और टाइपिंग','Word में नया Document बनाएँ','लिखें और पहली बार सेव करें।',[
 S('Word खोलें',['Win'],'Windows दबाएँ, Word लिखें और ऐप खोलें।','Word ऐप खोलें।','Word की शुरुआत वाली स्क्रीन मिलेगी।','word-home','Blank document'),
 S('Blank document चुनें',['Tab','Enter'],'Blank document चुनें। खुले document में Ctrl + N से भी नया document बनता है।','Blank document दबाएँ।','खाली पन्ना खुलेगा।','word','Document'),
 S('लिखकर Save करें',['Ctrl','S'],'अपना text लिखें। Ctrl + S दबाएँ। पहली बार नाम और जगह चुनें।','File → Save as में जगह और नाम चुनें।','Document सेव होगा।','save','Save')],['office-signin','save-permission','replace-file'],source='word',before='Desktop Word install और उसकी उपयुक्त license की जरूरत हो सकती है।')
L('word-save','Word और टाइपिंग','Document सेव या PDF बनाएँ','Save और Save as में फर्क समझें।',[
 S('वर्तमान बदलाव सेव करें',['Ctrl','S'],'Ctrl + S उसी फाइल में बदलाव सेव करता है। पहली बार file location माँगी जा सकती है।','Save button दबाएँ।','नए बदलाव सेव होंगे।','word','Save'),
 S('अलग नाम की कॉपी बनाएँ',['F12'],'Desktop Word में F12 से Save As खुल सकता है। Laptop पर Fn + F12 की जरूरत हो सकती है।','File → Save As / Save a Copy चुनें।','नाम, जगह और type के विकल्प मिलेंगे।','save','File name'),
 S('PDF चाहिए तो type बदलें',['Tab'],'Save as type में PDF चुनें। नाम और folder जाँचकर Save / Publish चुनें।','File type में PDF चुनकर Save दबाएँ।','अलग PDF बनेगी; editable Word file भी रखें।','save','Save as type')],['save-permission','replace-file'],source='word',tags='pdf export docx')
L('copy-text','Word और टाइपिंग','लिखाई Copy और Paste करें','चुनी हुई लिखाई दूसरी जगह रखें।',[
 S('लिखाई चुनें',['Shift','← / →'],'Text cursor रखें। Shift के साथ arrows से text चुनें। पूरे document के लिए Ctrl + A होता है।','Mouse से text select करें।','चुनी हुई लिखाई highlight होगी।','word','Selected text'),
 S('Copy करें',['Ctrl','C'],'Ctrl + C दबाएँ। Move करना हो तो Ctrl + X दबाएँ।','Right click → Copy चुनें।','चुनी हुई लिखाई clipboard में होगी।','word','Copy'),
 S('नई जगह Paste करें',['Ctrl','V'],'जहाँ लिखाई चाहिए वहाँ cursor रखें। Ctrl + V दबाएँ।','नई जगह click → Paste करें।','लिखाई नई जगह दिखेगी।','word','Paste')],[],source='windows',tags='clipboard cut copy paste')
L('typing-language','Word और टाइपिंग','हिंदी / English बदलें','Installed keyboard language चुनें।',[
 S('Input language बदलें',['Win','Space'],'Windows दबाकर रखें और Space से भाषा चुनें। Windows छोड़ दें।','Taskbar में ENG / HIN चुनें।','उपलब्ध भाषा चुन जाएगी।','language','Hindi'),
 S('छोटा शब्द लिखकर जाँचें',[],'किसी text field में छोटा शब्द लिखें। Phonetic और InScript layouts अलग तरह से काम करते हैं।','Text field में लिखकर परिणाम देखें।','सही भाषा में लिखाई दिखेगी।','language','Hindi')],['hindi-missing'],source='windows',tags='hindi english input keyboard')
L('undo','Word और टाइपिंग','गलती वापस करें','Undo और Redo का उपयोग करें।',[
 S('पिछला बदलाव वापस करें',['Ctrl','Z'],'जिस ऐप में बदलाव हुआ है, वहीं Ctrl + Z दबाएँ। कुछ actions वापस नहीं होते।','ऐप का Undo button दबाएँ।','समर्थित आखिरी बदलाव वापस होगा।','word','Undo'),
 S('जरूरत हो तो Redo करें',['Ctrl','Y'],'Word जैसे समर्थित apps में Ctrl + Y से वापस लाया बदलाव दोहरा सकते हैं।','Redo button दबाएँ।','बदलाव फिर लागू होगा।','word','Redo')],[],source='windows')
L('windows-update','मदद और रखरखाव','Windows Update देखें','चार्जर लगाकर update करें।',[
 S('Update settings खोलें',['Win','I'],'Settings में Windows Update चुनें। Charger और internet जुड़े हों।','Settings → Windows Update खोलें।','Update status दिखेगा।','settings','Windows Update'),
 S('Updates जाँचें',['Tab','Enter'],'Check for updates चुनें। Download & install दिखे तो विवरण पढ़ें।','Check for updates दबाएँ।','नई updates या up to date का संदेश मिलेगा।','update','Check for updates'),
 S('जरूरत पर Restart करें',['Tab','Enter'],'पहले अपना काम सेव करें। Restart required आए तो उपयुक्त समय पर Restart now चुनें।','Restart now या Schedule restart चुनें।','Update लगकर PC दोबारा चालू होगा।','update','Restart now')],['update-shutdown','unsaved'],source='windows')
L('narrator','मदद और रखरखाव','Narrator चालू / बंद करें','ज़रूरत होने पर screen reader का विकल्प।',[
 S('Narrator toggle करें',['Ctrl','Win','Enter'],'तीनों बटन साथ दबाएँ। Shortcut enabled हो तो Narrator चालू या बंद होगा।','Settings → Accessibility → Narrator का switch चुनें।','आवाज़ शुरू होगी या बंद होगी।','settings','Narrator'),
 S('Shortcut काम न करे तो Settings देखें',['Win','I'],'Settings में Accessibility → Narrator खोलें। यहाँ On / Off और shortcut setting मिलती है।','Narrator settings में अपनी पसंद चुनें।','Narrator की स्थिति स्पष्ट होगी।','settings','Narrator')],['settings-different'],source='windows',note='यह वैकल्पिक सहायक तरीका है। ऐप की मुख्य सुविधा बड़ा text और magnification है।')
L('frozen','मदद और रखरखाव','ऐप अटक गई है','पहले इंतज़ार, फिर जरूरत हो तो Task Manager।',[
 S('थोड़ा रुकें और ऐप बदलें',['Alt','Tab'],'Download या save चल रहा हो तो पहले पूरा होने दें। Alt + Tab से जाँचें कि दूसरी ऐप चलती है या नहीं।','Taskbar से दूसरी ऐप खोलकर देखें।','पता चलेगा केवल एक ऐप अटकी है या पूरा PC।','desktop','Task view'),
 S('Task Manager खोलें',['Ctrl','Shift','Esc'],'ऐप लगातार जवाब न दे तो Task Manager खोलें।','Start पर right click → Task Manager चुनें।','Processes की सूची दिखेगी।','taskmanager','Processes'),
 S('केवल अटकी हुई ऐप बंद करें',['Tab','Enter'],'सही ऐप चुनें। बिना सेव किया काम खो सकता है। जरूरत हो तभी End task दबाएँ; अनजान system processes बंद न करें।','अटकी ऐप → End task चुनें।','ऐप बंद होगी; फिर खोल सकते हैं।','taskmanager','End task')],['unsaved','unknown'],source='windows')
help_items={
'unknown':('यह संदेश सूची में नहीं है','रुकें और पूरा संदेश पढ़ें। शीर्षक और buttons का नाम लिख लें या निजी जानकारी हटाकर screenshot लें। अनजाना विकल्प न चुनें। Cancel / Close हो तो उससे लौटें; हर dialog में Esc काम नहीं करता।'),
'settings-different':('मेरी Settings अलग दिख रही है','Settings के search box में feature का English नाम लिखें। Sidebar का स्थान Windows update या window के आकार से बदल सकता है।'),
'magnifier-lost':('ज़ूम में रास्ता खो गया','Windows + minus से थोड़ा छोटा करें। जरूरत हो तो Windows + Esc से Magnifier बंद करें। Windows + plus से फिर चालू कर सकते हैं।'),
'signin':('Sign in / Verify it is you','पहचानें कि यह उसी ऐप का अपेक्षित sign-in है। सही account चुनें। Password या OTP केवल असली sign-in screen पर डालें; इस गाइड में कभी नहीं। Account recovery के लिए संबंधित service का आधिकारिक तरीका अपनाएँ।'),
'app-missing':('ऐप खोजने पर नहीं मिलती','नाम फिर जाँचें। Installed apps में देखें। Install जरूरी हो तो Microsoft Store या ऐप की आधिकारिक वेबसाइट इस्तेमाल करें। अनजान download विज्ञापन न चुनें।'),
'unsaved':('Save changes? / Unsaved changes','काम रखना हो तो Save चुनें। हटाना हो तभी Don’t save / Discard चुनें। अभी तय न हो तो Cancel चुनकर वापस document देखें।'),
'update-shutdown':('Update and shut down / Restart required','काम सेव करें और charger लगा रहने दें। Update शुरू हो जाए तो बीच में power न काटें। उपलब्ध हो तो schedule का विकल्प चुन सकते हैं।'),
'wifi-password':('Can’t connect / Incorrect password','सही network name और password जाँचें। Caps Lock और ENG / HIN देखें। अगली बार सही password डालें। साझा नेटवर्क हो तो मालिक से जानकारी लें।'),
'wifi-none':('Wi-Fi या network नहीं दिखता','Airplane mode और Wi-Fi की स्थिति देखें। Router / hotspot पास और चालू हो। Settings में Network & internet देखें। Wi-Fi विकल्प बिल्कुल न हो तो device-specific मदद चाहिए।'),
'wifi-no-internet':('Connected, no internet','Wi-Fi connection और internet अलग बातें हैं। फोन के hotspot में mobile data देखें। Public Wi-Fi हो तो browser में sign-in page अपेक्षित हो सकता है। दूसरे device में भी internet जाँचें।'),
'bluetooth-none':('डिवाइस सूची में नहीं है','डिवाइस pairing mode में और पास रखें। वह किसी दूसरे फोन से जुड़ा हो तो पहले वहाँ disconnect करें। Battery जाँचें और फिर Add device दोबारा खोलें।'),
'pair-code':('Pairing code / Confirm PIN','दोनों devices पर code एक जैसा है तभी Pair / Confirm करें। किसी और device का request हो तो Cancel करें।'),
'no-sound':('आवाज़ नहीं आ रही','Volume, mute और चुना हुआ speaker / headphones जाँचें। Bluetooth headphones से आवाज़ जा रही हो सकती है। Call में WhatsApp की device settings भी देखें।'),
'phone-transfer':('Share में Phone Link नहीं है','Phone Link और Link to Windows update करें; फोन pairing जाँचें। Feature device और version पर निर्भर है। विकल्प न हो तो USB या दूसरी समर्थित file-transfer विधि इस्तेमाल करें।'),
'open-with':('How do you want to open this file?','फाइल के type से मेल खाता परिचित ऐप चुनें। PDF के लिए उपलब्ध PDF reader या browser चुन सकते हैं। हमेशा के लिए default तभी बनाएँ जब वही पसंद हो।'),
'file-missing':('सेव की हुई फाइल नहीं मिल रही','पहले चुना हुआ folder देखें। Browser में Ctrl + J → Show in folder देखें। Downloads और Documents में नाम खोजें। अलग user account / OneDrive में भी जगह चुनी गई हो सकती है।'),
'folder-exists':('नाम पहले से मौजूद है','अलग नाम दें। बदलना जरूरी न हो तो Cancel करें। बिना जाँच किसी मौजूदा फाइल या folder को replace न करें।'),
'extension':('Changing file extension warning','Rename में .pdf / .docx जैसे extension बदल गए हों तो No / Cancel करें। केवल नाम बदलें, extension रहने दें।'),
'replace-file':('Replace this file? / File already exists','दोनों फाइलों को बचाना हो तो Cancel / Skip चुनें और नए नाम से सेव करें। Replace चुनने से पुरानी फाइल बदल सकती है; पहले जाँचें।'),
'permission':('Access denied / Administrator permission','पहले Cancel करें। Documents जैसे अपने folder में काम करके देखें। Protected system folders की permissions बिना समझे न बदलें।'),
'save-permission':('You don’t have permission to save here','Save As में अपने Documents या Desktop की जगह चुनें। Managed computer हो तो administrator की मदद लें।'),
'disk-full':('Not enough space','Transfer रोकें। Settings → System → Storage में जगह देखें। अपनी जरूरी फाइलें जाँचकर सुरक्षित backup बनाएँ; अनजान system files न हटाएँ।'),
'permanent-delete':('Permanently delete? / Too large for Recycle Bin','यह वापस न आने वाली deletion हो सकती है। Cancel चुनें और पहले backup या सही फाइल की पुष्टि करें।'),
'usb-format':('You need to format the disk','डेटा रखना हो तो Format दबाने से बचें। Cancel करें। दूसरे port या PC में जाँचें; drive में जरूरी डेटा हो तो विशेषज्ञ मदद लें।'),
'usb-busy':('Device is currently in use','USB की खुली फाइलें और उससे जुड़ी apps बंद करें। Copy पूरा होने दें, फिर Eject दोबारा करें। चलते transfer में USB न निकालें।'),
'chrome-default':('Make Chrome default / Sign in to Chrome','Browsing के लिए default या sync जरूरी नहीं। अभी जरूरत न हो तो Skip / Not now / Close से आगे बढ़ें।'),
'cookie':('Cookies / Notifications का संदेश','जरूरी cookies या अपनी पसंद चुनें। Website notifications की जरूरत न हो तो Block / Don’t allow चुन सकते हैं।'),
'ssl':('Your connection is not private / सुरक्षा चेतावनी','संदेश को bypass न करें। Address spelling और PC की तारीख जाँचें। इस page पर password या payment जानकारी न डालें; आधिकारिक सुरक्षित रास्ते से वापस जाएँ।'),
'offline':('No internet / You’re offline','Wi-Fi / hotspot और mobile data देखें। Connection लौटने पर page फिर खोलें। यह गाइड पहली सफल cache के बाद कुछ हिस्सों में offline काम कर सकती है, लेकिन Gmail / calls को internet चाहिए।'),
'resubmit':('Confirm form resubmission','पहले तय करें कि form दोबारा भेजना है या नहीं। Payment या application हो तो Cancel करके उसकी स्थिति अलग से देखें ताकि duplicate submission न हो।'),
'download-blocked':('Dangerous / Suspicious download blocked','Warning को सीधे bypass न करें। स्रोत, sender और file की जरूरत जाँचें। आधिकारिक सुरक्षित स्रोत से फाइल लें।'),
'download-failed':('Download failed / Network error','Internet और खाली storage देखें। उसी trusted source से download फिर शुरू करें। खत्म होने तक फाइल पूरी उपलब्ध नहीं होगी।'),
'confidential':('Confidential mode / Print नहीं मिलता','Gmail confidential messages में printing और downloading बंद हो सकती है। Sender से आवश्यक अनुमति वाला अलग document माँगें; restriction को bypass न करें।'),
'print-blocked':('Print view नहीं खुली / Pop-up blocked','Gmail में उस message का More → Print फिर जाँचें। अगर Chrome इसी expected print action का pop-up रोक रहा है, तभी Gmail के लिए उस prompt में अनुमति चुनें। अनजान websites के लिए blanket अनुमति न दें।'),
'attachment-large':('File too large / Upload failed','ऐप की बताई सीमा देखें। छोटी फाइल चुनें या supported sharing तरीका अपनाएँ। Upload पूरा होने से पहले Send न दबाएँ।'),
'missing-attachment':('Did you mean to attach files?','फाइल भेजनी थी तो Cancel / Add attachment चुनें। सही attachment लगाकर दोबारा जाँचें।'),
'pdf-password':('PDF password माँग रही है','Document के sender से सही password लें। इस गाइड में password न लिखें। Password बिना सही document नहीं खुल सकता।'),
'pdf-scanned':('Ctrl + F से शब्द नहीं मिलते','यह scanned image वाली PDF हो सकती है। Zoom से पढ़ें; text search के लिए OCR वाली accessible copy चाहिए हो सकती है।'),
'printer-offline':('Printer offline / Paper jam / Out of paper','Printer चालू, connected और paper भरा है या नहीं देखें। Jam हो तो printer की अपनी instructions अपनाएँ। बार-बार Print दबाने से duplicate jobs बन सकती हैं।'),
'qr-expired':('QR code expired / Link failed','PC में QR refresh करें और अपने फोन से नया code scan करें। दोनों devices में internet जाँचें। केवल अपने PC के QR को link करें।'),
'whatsapp-offline':('Connecting / Phone or computer offline','Computer का internet जाँचें। WhatsApp को sync होने दें। बार-बार message भेजने से duplicate हो सकते हैं; भेजे हुए message की स्थिति पहले देखें।'),
'mic-camera':('Microphone / Camera access denied','Windows Settings → Privacy & security → Microphone या Camera देखें। Device access और संबंधित app permissions जाँचें। Webcam shutter हो तो खोलें। दूसरी ऐप camera इस्तेमाल कर रही हो तो उसे बंद करें।'),
'call-unavailable':('Call button नहीं है / Call failed','सही Windows WhatsApp app और उसकी update जाँचें। Internet, camera और microphone उपलब्ध हों। Work restrictions या unsupported version हो तो उस device की सहायता चाहिए।'),
'share-missing':('Share screen का button नहीं है','पहले connected video call होना जाँचें। More / तीन dots में देखें। WhatsApp update करें। Audio-only call या अलग version में विकल्प उपलब्ध न हो सकता है।'),
'share-warning':('Screen sharing warning / Start sharing?','कौन-सी window / screen दिखेगी पढ़ें। अपेक्षित व्यक्ति को वही content दिखाना हो तभी शुरू करें। निजी documents और notifications का ध्यान रखें।'),
'share-black':('सामने वाले को काली / गलत screen दिखती है','Sharing रोकें। सही window चुनकर फिर शुरू करें; चुना हुआ app खुला रखें। Protected video या content साझा न हो सकता है।'),
'office-signin':('Activate Office / Sign in / Subscription','Desktop Word के लिए license जरूरी हो सकता है। अपने उपलब्ध account की जाँच करें। बिना जरूरत खरीदारी न करें। उपयुक्त हो तो Word for the web अलग विकल्प है, उसकी screen अलग होगी।'),
'hindi-missing':('सूची में Hindi नहीं है','Settings → Time & language → Language & region में Hindi और उपयुक्त keyboard जोड़ें। Phonetic या InScript का चुनाव आपकी typing के तरीके पर निर्भर है।')
}
for x in lessons:
 for h in x['help']:
  assert h in help_items,h
content=dict(version=1,reviewed='2026-11-11',categories=['देखना आसान करें','शुरुआत और Windows','इंटरनेट और डिवाइस','फाइल और फोल्डर','Chrome और वेब','Gmail और PDF','WhatsApp','Word और टाइपिंग','मदद और रखरखाव'],sources=sources,help={k:dict(title=v[0],body=v[1]) for k,v in help_items.items()},lessons=lessons)
(ROOT/'lessons.json').write_text(json.dumps(content,ensure_ascii=False,indent=2))
print(len(lessons),'lessons;',sum(len(x['steps']) for x in lessons),'steps;',len(help_items),'help paths')
