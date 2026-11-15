/**
 * AgroCure AI - Multilingual UI Translation Strings (5 Languages)
 * English (en), Hindi (hi), Kannada (kn), Marathi (mr), Tamil (ta).
 * Covers all 14 pages and 4 crops (Tomato, Potato, Capsicum, Grapes).
 */

const UI_TRANSLATIONS = {
  en: {
    app_name: "AGROCURE AI",
    college_tag: "CSE Final Year Project",
    tagline: "AI-Based Plant Disease Detection & Crop Healthcare Advisory System",
    
    // 14 Pages Navigation
    nav_home: "Home",
    nav_login: "Login",
    nav_register: "Register",
    nav_dashboard: "Dashboard",
    nav_detection: "AI Detection",
    nav_result: "Prediction Result",
    nav_organic: "Organic Treatment",
    nav_inorganic: "Inorganic Treatment",
    nav_diseases: "Disease Info",
    nav_history: "Scan History",
    nav_profile: "User Profile",
    nav_about: "About Us",
    nav_contact: "Contact Us",
    nav_feedback: "Feedback",

    // Crops
    crop_all: "All Crops",
    crop_tomato: "Tomato",
    crop_potato: "Potato",
    crop_capsicum: "Capsicum (Bell Pepper)",
    crop_grapes: "Grapes",

    // Common Actions
    scan_now: "Scan Plant Now",
    explore_diseases: "Explore 19 Diseases",
    switch_lang: "Language",
    dark_mode: "Dark Mode",
    light_mode: "Light Mode",
    logout: "Logout",
    view_details: "View Details",

    // Home Page
    hero_title: "AI-Powered Plant Pathology & Crop Disease Cure",
    hero_subtitle: "Empowering farmers and researchers with deep learning MobileNetV2 leaf disease classification, OpenCV lesion area segmentation, and instant multilingual cure advisory.",
    stat_accuracy: "98.4% Classification Accuracy",
    stat_classes: "19 Disease / Health Classes",
    stat_crops: "4 High-Yield Crops",
    stat_instant: "< 500ms Instant Inference",
    
    // Scanner
    one_click_test: "1-Click Instant Leaf Test Samples",
    upload_drop: "Drag & drop leaf photo here or click to browse",
    upload_formats: "Supports high-resolution JPG, PNG, WEBP and Camera capture",
    select_crop_label: "Target Crop Hint:",
    camera_btn: "Open Camera",
    start_analysis: "Analyze Foliar Health",
    analyzing: "Detecting leaf boundaries and computing pathology...",
    
    // Results
    diagnosis_title: "Foliar Diagnosis & Pathology Breakdown",
    severity: "Disease Severity",
    confidence: "Confidence Score",
    pathogen: "Causal Pathogen",
    leaf_metrics: "OpenCV Computer Vision Leaf Metrics",
    green_area: "Healthy Foliage Area",
    lesion_area: "Necrotic Lesion Area",
    leaf_coverage: "Leaf In Frame Coverage",
    listen_voice: "Listen to Voice Advisory (Audio Readout)",
    toggle_heatmap: "Toggle OpenCV Lesion Heatmap / Original Photo",

    // Treatments
    organic_title: "Organic & Biological Treatment Guide",
    inorganic_title: "Inorganic & Chemical Fungicide Guide",
    dosage_safety: "Dosage & Farmer Safety Protocol",
    preventive_measures: "Cultural & Preventive Measures"
  },

  hi: {
    app_name: "एग्रो क्योर AI (AGROCURE AI)",
    college_tag: "बी.टेक कंप्यूटर साइंस अंतिम वर्ष प्रोजेक्ट",
    tagline: "पौधों के रोग की सटीक पहचान एवं उपचार हेतु आधुनिक AI प्रणाली",

    // 14 Pages Navigation
    nav_home: "होम (Home)",
    nav_login: "लॉग इन (Login)",
    nav_register: "पंजीकरण (Register)",
    nav_dashboard: "डैशबोर्ड (Dashboard)",
    nav_detection: "AI रोग पहचान (Detection)",
    nav_result: "निदान परिणाम (Result)",
    nav_organic: "जैविक उपचार (Organic)",
    nav_inorganic: "रासायनिक उपचार (Chemical)",
    nav_diseases: "रोग जानकारी (Disease Info)",
    nav_history: "स्कैन इतिहास (History)",
    nav_profile: "उपयोगकर्ता प्रोफ़ाइल (Profile)",
    nav_about: "हमारे बारे में (About)",
    nav_contact: "संपर्क करें (Contact)",
    nav_feedback: "प्रतिक्रिया (Feedback)",

    // Crops
    crop_all: "सभी फसलें",
    crop_tomato: "टमाटर (Tomato)",
    crop_potato: "आलू (Potato)",
    crop_capsicum: "शिमला मिर्च (Capsicum)",
    crop_grapes: "अंगूर (Grapes)",

    // Common Actions
    scan_now: "अभी पत्ती स्कैन करें",
    explore_diseases: "19 रोग वर्गों का विवरण",
    switch_lang: "भाषा बदलें",
    dark_mode: "डार्क मोड",
    light_mode: "लाइट मोड",
    logout: "लॉग आउट",
    view_details: "विवरण देखें",

    // Home Page
    hero_title: "कृत्रिम बुद्धिमत्ता (AI) द्वारा फसल रोग निदान एवं निवारण",
    hero_subtitle: "डीप लर्निंग MobileNetV2 तथा OpenCV तकनीक द्वारा टमाटर, आलू, शिमला मिर्च और अंगूर के 19 रोगों की सटीक पहचान एवं अपनी मातृभाषा में जैविक-रासायनिक उपचार।",
    stat_accuracy: "98.4% सटीक मॉडल पहचान",
    stat_classes: "19 रोग एवं स्वास्थ्य श्रेणियां",
    stat_crops: "4 प्रमुख समर्थित फसलें",
    stat_instant: "त्वरित परिणाम (<500ms)",

    // Scanner
    one_click_test: "1-क्लिक त्वरित नमूना परीक्षण (Instant Test)",
    upload_drop: "पत्ती की फोटो यहां खींचें या अपलोड करें",
    upload_formats: "JPG, PNG, WEBP एवं कैमरा फोटो समर्थित",
    select_crop_label: "फसल चुनें:",
    camera_btn: "कैमरा चालू करें",
    start_analysis: "रोग विश्लेषण शुरू करें",
    analyzing: "OpenCV और AI द्वारा पत्ती का विश्लेषण हो रहा है...",

    // Results
    diagnosis_title: "पत्ती रोग निदान एवं विस्तृत विश्लेषण",
    severity: "रोग की गंभीरता",
    confidence: "सटीकता (Confidence)",
    pathogen: "रोगजनक (Pathogen)",
    leaf_metrics: "कंप्यूटर विजन पत्ती स्वास्थ्य मेट्रिक्स",
    green_area: "स्वस्थ हरा भाग",
    lesion_area: "रोगग्रस्त भाग (Lesions)",
    leaf_coverage: "पत्ती का क्षेत्रफल",
    listen_voice: "आवाज़ में सुनें (वॉइस असिस्टेंट)",
    toggle_heatmap: "रोग हीटमैप / मूल फोटो बदलें",

    // Treatments
    organic_title: "जैविक एवं प्राकृतिक उपचार विधि",
    inorganic_title: "रासायनिक कवकनाशी एवं दवाएं",
    dosage_safety: "मात्रा एवं किसान सुरक्षा दिशा-निर्देश",
    preventive_measures: "बचाव एवं कृषि रोकथाम के उपाय"
  },

  kn: {
    app_name: "ಅಗ್ರೋಕ್ಯೂರ್ AI (AGROCURE AI)",
    college_tag: "ಸಿಎಸ್ಇ ಅಂತಿಮ ವರ್ಷದ ಪದವಿ ಪ್ರಾಜೆಕ್ಟ್",
    tagline: "ಸಸ್ಯ ರೋಗ ಪತ್ತೆ ಮತ್ತು ಪರಿಹಾರ ನೀಡುವ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ತಂತ್ರಜ್ಞಾನ",

    // 14 Pages Navigation
    nav_home: "ಮುಖಪುಟ (Home)",
    nav_login: "ಲಾಗಿನ್ (Login)",
    nav_register: "ನೋಂದಣಿ (Register)",
    nav_dashboard: "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್ (Dashboard)",
    nav_detection: "AI ರೋಗ ಪತ್ತೆ (Detection)",
    nav_result: "ಪರೀಕ್ಷಾ ಫಲಿತಾಂಶ (Result)",
    nav_organic: "ಸಾವಯವ ಚಿಕಿತ್ಸೆ (Organic)",
    nav_inorganic: "ರಾಸಾಯನಿಕ ಚಿಕಿತ್ಸೆ (Chemical)",
    nav_diseases: "ರೋಗಗಳ ಮಾಹಿತಿ (Disease Info)",
    nav_history: "ಸ್ಕ್ಯಾನ್ ಇತಿಹಾಸ (History)",
    nav_profile: "ಬಳಕೆದಾರ ವಿವರ (Profile)",
    nav_about: "ನಮ್ಮ ಬಗ್ಗೆ (About)",
    nav_contact: "ಸಂಪರ್ಕಿಸಿ (Contact)",
    nav_feedback: "ಅಭಿಪ್ರಾಯ (Feedback)",

    // Crops
    crop_all: "ಎಲ್ಲಾ ಬೆಳೆಗಳು",
    crop_tomato: "ಟೊಮೆಟೊ (Tomato)",
    crop_potato: "ಆಲೂಗಡ್ಡೆ (Potato)",
    crop_capsicum: "ಕ್ಯಾಪ್ಸಿಕಂ / ದಪ್ಪ ಮೆಣಸಿನಕಾಯಿ (Capsicum)",
    crop_grapes: "ದ್ರಾಕ್ಷಿ (Grapes)",

    // Common Actions
    scan_now: "ಈಗಲೇ ಎಲೆ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ",
    explore_diseases: "19 ರೋಗಗಳ ವಿವರ ನೋಡಿ",
    switch_lang: "ಭಾಷೆ",
    dark_mode: "ಡಾರ್ಕ್ ಮೋಡ್",
    light_mode: "ಲೈಟ್ ಮೋಡ್",
    logout: "ನಿರ್ಗಮಿಸಿ",
    view_details: "ವಿವರ ವೀಕ್ಷಿಸಿ",

    // Home Page
    hero_title: "ಎಲೆ ರೋಗ ಪತ್ತೆ ಹಚ್ಚುವ ಸುಧಾರಿತ AI ಕೃಷಿ ವೇದಿಕೆ",
    hero_subtitle: "ಟೊಮೆಟೊ, ಆಲೂಗಡ್ಡೆ, ಕ್ಯಾಪ್ಸಿಕಂ ಮತ್ತು ದ್ರಾಕ್ಷಿಯ 19 ರೋಗಗಳನ್ನು ಮೊಬೈಲ್‌ನೆಟ್‌ವಿ2 ಹಾಗೂ ಓಪನ್‌ಸಿವಿ ಮೂಲಕ ನಿಖರವಾಗಿ ಪತ್ತೆಹಚ್ಚಿ ಪರಿಹಾರ ಪಡೆಯಿರಿ.",
    stat_accuracy: "98.4% ನಿಖರತೆ",
    stat_classes: "19 ರೋಗಗಳ ಪಟ್ಟಿ",
    stat_crops: "4 ಪ್ರಮುಖ ಬೆಳೆಗಳು",
    stat_instant: "ತಕ್ಷಣದ ಫಲಿತಾಂಶ",

    // Scanner
    one_click_test: "1-ಕ್ಲಿಕ್ ತ್ವರಿತ ಮಾದರಿ ಪರೀಕ್ಷೆ",
    upload_drop: "ಎಲೆಯ ಫೋಟೋವನ್ನು ಇಲ್ಲಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ",
    upload_formats: "JPG, PNG, WEBP ಮತ್ತು ಮೊಬೈಲ್ ಕ್ಯಾಮೆರಾ",
    select_crop_label: "ಬೆಳೆ ಆಯ್ಕೆಮಾಡಿ:",
    camera_btn: "ಕ್ಯಾಮೆರಾ ತೆರೆಯಿರಿ",
    start_analysis: "ರೋಗ ತಪಾಸಣೆ ನಡೆಸಿ",
    analyzing: "AI ಮೂಲಕ ಎಲೆಯ ಪರೀಕ್ಷೆ ನಡೆಯುತ್ತಿದೆ...",

    // Results
    diagnosis_title: "ಎಲೆಯ ರೋಗ ತಪಾಸಣೆ ವಿವರ",
    severity: "ರೋಗದ ತೀವ್ರತೆ",
    confidence: "ಖಚಿತತೆ",
    pathogen: "ರೋಗಾಣು ವಿವರ",
    leaf_metrics: "ಕಂಪ್ಯೂಟರ್ ವಿಷನ್ ಎಲೆ ಅಳತೆಗಳು",
    green_area: "ಆರೋಗ್ಯಕರ ಹಸಿರು ಭಾಗ",
    lesion_area: "ರೋಗ ಪೀಡಿತ ಭಾಗ",
    leaf_coverage: "ಎಲೆಯ ವಿಸ್ತೀರ್ಣ",
    listen_voice: "ಧ್ವನಿಯಲ್ಲಿ ಕೇಳಿ (ಆಡಿಯೋ)",
    toggle_heatmap: "ಹೀಟ್‌ಮ್ಯಾಪ್ / ನೈಜ ಫೋಟೋ ಬದಲಿಸಿ",

    // Treatments
    organic_title: "ಸಾವಯವ ಮತ್ತು ಜೈವಿಕ ನಿಯಂತ್ರಣ ಕ್ರಮಗಳು",
    inorganic_title: "ರಾಸಾಯನಿಕ ಔಷಧಗಳು",
    dosage_safety: "ಔಷಧ ಪ್ರಮಾಣ ಮತ್ತು ರೈತರ ಸುರಕ್ಷತೆ",
    preventive_measures: "ಮುನ್ನೆಚ್ಚರಿಕಾ ಕ್ರಮಗಳು"
  },

  mr: {
    app_name: "अ‍ॅग्रोक्युअर AI (AGROCURE AI)",
    college_tag: "संगणक अभियांत्रिकी अंतिम वर्ष प्रकल्प (CSE Final Year)",
    tagline: "कृत्रिम बुद्धिमत्तेवर आधारित वनस्पती रोग निदान व उपचार प्रणाली",

    // 14 Pages Navigation
    nav_home: "मुख्यपृष्ठ (Home)",
    nav_login: "लॉग इन (Login)",
    nav_register: "नोंदणी (Register)",
    nav_dashboard: "डॅशबोर्ड (Dashboard)",
    nav_detection: "AI रोग निदान (Detection)",
    nav_result: "निदान निकाल (Result)",
    nav_organic: "सेंद्रिय उपाय (Organic)",
    nav_inorganic: "रासायनिक उपाय (Chemical)",
    nav_diseases: "रोग माहिती (Disease Info)",
    nav_history: "स्कॅन इतिहास (History)",
    nav_profile: "माझी माहिती (Profile)",
    nav_about: "आमच्याबद्दल (About)",
    nav_contact: "संपर्क (Contact)",
    nav_feedback: "अभिप्राय (Feedback)",

    // Crops
    crop_all: "सर्व पिके",
    crop_tomato: "टोमॅटो (Tomato)",
    crop_potato: "बटाटा (Potato)",
    crop_capsicum: "ढोबळी मिरची (Capsicum)",
    crop_grapes: "द्राक्षे (Grapes)",

    // Common Actions
    scan_now: "आता पान स्कॅन करा",
    explore_diseases: "19 रोगांची संपूर्ण माहिती",
    switch_lang: "भाषा",
    dark_mode: "डार्क मोड",
    light_mode: "लाईट मोड",
    logout: "बाहेर पडा",
    view_details: "तपशील पहा",

    // Home Page
    hero_title: "AI द्वारे वनस्पती रोग निदान व त्वरित शेती मार्गदर्शन",
    hero_subtitle: "टोमॅटो, बटाटा, शिमला मिरची आणि द्राक्षांच्या 19 रोगांचे अचूक निदान आणि मराठी भाषेत सेंद्रिय व रासायनिक सल्ला.",
    stat_accuracy: "98.4% अचूकता",
    stat_classes: "19 रोग व आरोग्य वर्ग",
    stat_crops: "4 प्रमुख पिके",
    stat_instant: "झटपट निकाल (<500ms)",

    // Scanner
    one_click_test: "1-क्लिक त्वरित नमुना चाचणी",
    upload_drop: "पानाचा फोटो इथे टाका किंवा निवडा",
    upload_formats: "JPG, PNG, WEBP आणि कॅमेरा फोटो",
    select_crop_label: "पीक निवडा:",
    camera_btn: "कॅमेरा सुरू करा",
    start_analysis: "रोग तपासणी सुरू करा",
    analyzing: "AI द्वारे पानाचे विश्लेषण सुरू आहे...",

    // Results
    diagnosis_title: "पान रोग निदान व सविस्तर पृथक्करण",
    severity: "रोगाची तीव्रता",
    confidence: "खात्री (Confidence)",
    pathogen: "रोगकारक घटक (Pathogen)",
    leaf_metrics: "संगणक दृष्टी (OpenCV) मोजमापे",
    green_area: "निरोगी हिरवा भाग",
    lesion_area: "रोगट भाग (Lesion Area)",
    leaf_coverage: "पानाचा एकूण आकार",
    listen_voice: "आवाजात ऐका (व्हॉइस असिस्टंट)",
    toggle_heatmap: "हीटमॅप / मूळ फोटो बदला",

    // Treatments
    organic_title: "सेंद्रिय व जैविक शेती उपाय",
    inorganic_title: "रासायनिक औषधे व बुरशीनाशके",
    dosage_safety: "प्रमाण आणि शेतकरी सुरक्षा नियम",
    preventive_measures: "प्रतिबंधात्मक शेती पद्धती"
  },

  ta: {
    app_name: "அக்ரோக்யூர் AI (AGROCURE AI)",
    college_tag: "சிஎஸ்இ இறுதி ஆண்டு கல்லூரி திட்டம்",
    tagline: "செயற்கை நுண்ணறிவு அடிப்படையிலான தாவர நோய் கண்டறிதல் மற்றும் தீர்வு அமைப்பு",

    // 14 Pages Navigation
    nav_home: "முகப்பு (Home)",
    nav_login: "உள்நுழைவு (Login)",
    nav_register: "பதிவு (Register)",
    nav_dashboard: "டாஷ்போர்டு (Dashboard)",
    nav_detection: "AI நோய் கண்டறிதல் (Detection)",
    nav_result: "முடிவுகள் (Result)",
    nav_organic: "இயற்கை மருத்துவம் (Organic)",
    nav_inorganic: "இரசாயன மருத்துவம் (Chemical)",
    nav_diseases: "நோய் தகவல் (Disease Info)",
    nav_history: "ஸ்கேன் வரலாறு (History)",
    nav_profile: "சுயவிவரம் (Profile)",
    nav_about: "எங்களை பற்றி (About)",
    nav_contact: "தொடர்புக்கு (Contact)",
    nav_feedback: "கருத்து (Feedback)",

    // Crops
    crop_all: "அனைத்து பயிர்கள்",
    crop_tomato: "தக்காளி (Tomato)",
    crop_potato: "உருளைக்கிழங்கு (Potato)",
    crop_capsicum: "குடைமிளகாய் (Capsicum)",
    crop_grapes: "திராட்சை (Grapes)",

    // Common Actions
    scan_now: "இலையை ஸ்கேன் செய்க",
    explore_diseases: "19 நோய் பிரிவுகளை காண்க",
    switch_lang: "மொழி",
    dark_mode: "டார்க் மோட்",
    light_mode: "லைட் மோட்",
    logout: "வெளியேறு",
    view_details: "விவரங்களை காண்க",

    // Home Page
    hero_title: "AI மூலம் தாவர இலை நோய் கண்டறிதல் மற்றும் பாதுகாப்பு",
    hero_subtitle: "தக்காளி, உருளைக்கிழங்கு, குடைமிளகாய் மற்றும் திராட்சை பயிர்களின் 19 நோய்களை மொபைல்நெட் மற்றும் ஓபன்சிவி மூலம் கண்டறிந்து தீர்வு பெறுங்கள்.",
    stat_accuracy: "98.4% துல்லியம்",
    stat_classes: "19 நோய் நிலைகள்",
    stat_crops: "4 முக்கிய பயிர்கள்",
    stat_instant: "உடனடி தீர்வு",

    // Scanner
    one_click_test: "1-கிளிக் மாதிரி இலை சோதனை",
    upload_drop: "இலையின் புகைப்படத்தை இங்கே பதிவேற்றவும்",
    upload_formats: "JPG, PNG, WEBP மற்றும் கேமரா புகைப்படங்கள்",
    select_crop_label: "பயிரை தேர்வு செய்க:",
    camera_btn: "கேமரா திறக்கவும்",
    start_analysis: "நோய் பரிசோதனையை தொடங்குக",
    analyzing: "AI மூலம் இலை பகுப்பாய்வு செய்யப்படுகிறது...",

    // Results
    diagnosis_title: "இலை நோய் கண்டறிதல் விவரங்கள்",
    severity: "நோயின் தீவிரம்",
    confidence: "துல்லிய சதவீதம்",
    pathogen: "நோய்க்கிருமி விவரம்",
    leaf_metrics: "கணினி பார்வை இலை அளவீடுகள்",
    green_area: "ஆரோக்கியமான பச்சை பகுதி",
    lesion_area: "பாதிக்கப்பட்ட இலை பகுதி",
    leaf_coverage: "இலை பரப்பளவு",
    listen_voice: "குரல் வடிவில் கேட்க (Audio)",
    toggle_heatmap: "ஹீட்மேப் / அசல் புகைப்படத்தை மாற்றவும்",

    // Treatments
    organic_title: "இயற்கை மற்றும் உயிரியல் முறைகள்",
    inorganic_title: "இரசாயன பூஞ்சைக் கொல்லிகள்",
    dosage_safety: "மருந்தின் அளவு மற்றும் பாதுகாப்பு",
    preventive_measures: "வருமுன் காக்கும் வழிகள்"
  }
};
