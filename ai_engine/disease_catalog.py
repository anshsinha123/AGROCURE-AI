"""
AgroCure AI - Comprehensive 19-Class Disease Knowledge Base.
Specifically covers the 4 Target Crops:
1. Tomato (10 classes)
2. Potato (3 classes)
3. Capsicum / Bell Pepper (2 classes)
4. Grapes (4 classes)

Supports 5 Languages: English (en), Hindi (hi), Kannada (kn), Marathi (mr), Tamil (ta).
"""

CROPS = ["Tomato", "Potato", "Capsicum", "Grapes"]

DISEASE_CATALOG = {
    # ==================== TOMATO (10 CLASSES) ====================
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "pathogen": "Bacterium (Xanthomonas vesicatoria)",
        "severity": "High",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Bacterial Spot",
                "pathogen": "Bacterium (Xanthomonas vesicatoria)",
                "symptoms": "Small, dark, water-soaked circular lesions (<3mm) with yellow chlorotic halos, turning black and causing severe defoliation and sunken fruit spots.",
                "organic_treatment": [
                    "Spray copper soap (copper octanoate) or fixed copper bactericide in early morning.",
                    "Apply bio-fungicide Bacillus subtilis (Serenade) every 7-10 days.",
                    "Prune lower foliage and mulch bed to prevent rain-splash infection from soil."
                ],
                "chemical_treatment": [
                    "Copper hydroxide tank-mixed with Mancozeb (acts synergistically).",
                    "Streptomycin sulfate sprays in registered agricultural areas during transplant stage."
                ],
                "prevention": [
                    "Use certified disease-free seeds and resistant tomato varieties.",
                    "Practice 2-3 year crop rotation away from solanaceous crops.",
                    "Use drip irrigation to keep tomato foliage dry."
                ]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "जीवाणु पत्ती धब्बा (Bacterial Spot)",
                "pathogen": "जीवाणु (Xanthomonas vesicatoria)",
                "symptoms": "पत्तियों पर छोटे (3 मिमी से कम) जल-सोखे हुए काले-भूरे गोल धब्बे, जिनके चारों ओर पीला घेरा होता है। पत्तियां समय से पहले झड़ जाती हैं।",
                "organic_treatment": [
                    "कॉपर सोप या नीम के तेल (0.5%) का सुबह छिड़काव करें।",
                    "बैसिलस सबटिलिस जैविक कवकनाशी का हर 7-10 दिन में छिड़काव करें।",
                    "निचली पत्तियों की छंटाई करें और पुआल की मल्चिंग करें।"
                ],
                "chemical_treatment": [
                    "कॉपर हाइड्रोक्साइड को मैन्कोजेब के साथ मिलाकर स्प्रे करें।",
                    "स्ट्रेप्टोमाइसिन सल्फेट का अनुशंसित मात्रा में छिड़काव करें।"
                ],
                "prevention": [
                    "प्रमाणित रोगमुक्त बीज लगाएं और 3 वर्ष का फसल चक्र अपनाएं।",
                    "टपक सिंचाई (ड्रिप) अपनाएं ताकि पत्तियों पर पानी न पड़े।"
                ]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಎಲೆ ಚುಕ್ಕೆ (Bacterial Spot)",
                "pathogen": "ಬ್ಯಾಕ್ಟೀರಿಯಾ (Xanthomonas vesicatoria)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ನೀರಿನಿಂದ ಕೂಡಿದ ಸಣ್ಣ ಕಪ್ಪು-ಕಂದು ಚುಕ್ಕೆಗಳು ಹಳದಿ ಅಂಚಿನೊಂದಿಗೆ ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತವೆ.",
                "organic_treatment": ["ತಾಮ್ರದ ಸಾಬೂನು ಅಥವಾ ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ.", "ಬ್ಯಾಸಿಲಸ್ ಸಬ್ಟಿಲಿಸ್ ಜೈವಿಕ ನಿಯಂತ್ರಕ ಬಳಸಿ."],
                "chemical_treatment": ["ಕಾಪರ್ ಹೈಡ್ರಾಕ್ಸೈಡ್ ಮತ್ತು ಮ್ಯಾಂಕೋಜೆಬ್ ಮಿಶ್ರಣ ಸಿಂಪಡಿಸಿ."],
                "prevention": ["ರೋಗಮುಕ್ತ ಬೀಜಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಹನಿ ನೀರಾವರಿ ಪದ್ಧತಿ ಅಳವಡಿಸಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "जिवाणूजन्य ठिपके (Bacterial Spot)",
                "pathogen": "जिवाणू (Xanthomonas vesicatoria)",
                "symptoms": "पानांवर लहान, काळे-तपकिरी रंगाचे जलमय ठिपके पडतात व पिवळे वलय दिसते. पाने अकाली गळतात.",
                "organic_treatment": ["कॉपर सोप किंवा जैविक बॅसिलस सबटिलिसची फवारणी करा."],
                "chemical_treatment": ["कॉपर हायड्रॉक्साईड अधिक मॅन्कोझेब एकत्र मिसळून फवारा."],
                "prevention": ["रोगमुक्त बियाणे वापरा आणि ठिबक सिंचनाचा वापर करा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "பாக்டீரியா இலைப்புள்ளி (Bacterial Spot)",
                "pathogen": "பாக்டீரியா (Xanthomonas vesicatoria)",
                "symptoms": "இலைகளில் சிறிய நீர் ஊறிய கரும் புள்ளிகள் மஞ்சள் வளையத்துடன் தோன்றும்.",
                "organic_treatment": ["காப்பர் சோப் அல்லது வேப்பெண்ணெய் தெளிக்கவும்."],
                "chemical_treatment": ["காப்பர் ஹைட்ராக்சைடு மற்றும் மேன்கோசெப் தெளிக்கவும்."],
                "prevention": ["சான்றளிக்கப்பட்ட விதைகளைப் பயன்படுத்தவும்."]
            }
        }
    },

    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "pathogen": "Fungus (Alternaria solani)",
        "severity": "Moderate to High",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Early Blight",
                "pathogen": "Fungus (Alternaria solani)",
                "symptoms": "Dark brown to black spots with distinct concentric rings creating a 'target-board' pattern, surrounded by chlorotic yellow halos on older leaves.",
                "organic_treatment": [
                    "Spray bio-fungicides with Trichoderma harzianum or Bacillus subtilis.",
                    "Apply copper octanoate or potassium bicarbonate sprays.",
                    "Mulch heavily around the plant base to prevent fungal spores from splashing up from soil."
                ],
                "chemical_treatment": [
                    "Apply Chlorothalonil (Daconil) or Mancozeb as protective contact fungicides.",
                    "Spray Azoxystrobin (Amistar) or Difenoconazole for active systemic control."
                ],
                "prevention": [
                    "Maintain 24-36 inch spacing between tomato plants for optimal air circulation.",
                    "Prune lower 12 inches of foliage after flowering.",
                    "Rotate crops annually with non-solanaceous crops."
                ]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "अगेती झुलसा (Early Blight)",
                "pathogen": "कवक (Alternaria solani)",
                "symptoms": "पुरानी पत्तियों पर गोल भूरे-काले धब्बे जिनके अंदर छल्ले (लक्ष्य बोर्ड / Target-board) बनते हैं और चारों तरफ पीलापन होता है।",
                "organic_treatment": [
                    "ट्राइकोडर्मा या कॉपर कवकनाशी का छिड़काव करें।",
                    "पौधों के तने के पास पुआल की मल्चिंग करें।"
                ],
                "chemical_treatment": [
                    "मैन्कोजेब (Mancozeb) या क्लोरोथैलोनिल का छिड़काव करें।",
                    "डाइफेनोकोनाज़ोल (Score) या एज़ोक्सीस्ट्रोबिन का प्रयोग करें।"
                ],
                "prevention": [
                    "पौधों के बीच उचित दूरी रखें और निचली पत्तियों की छंटाई करें।"
                ]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಮುಂಚಿನ ಕರಗು ರೋಗ (Early Blight)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Alternaria solani)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ಚಕ್ರಾಕಾರದ ಉಂಗುರಗಳಂತಹ ಕಂದು ಬಣ್ಣದ ಚುಕ್ಕೆಗಳು ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತವೆ.",
                "organic_treatment": ["ಟ್ರೈಕೋಡರ್ಮಾ ಅಥವಾ ತಾಮ್ರದ ದ್ರಾವಣ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಮ್ಯಾಂಕೋಜೆಬ್ ಅಥವಾ ಕ್ಲೋರೋಥಲೋನಿಲ್ ಸಿಂಪಡಿಸಿ."],
                "prevention": ["ಗಿಡಗಳ ನಡುವೆ ಸೂಕ್ತ ಅಂತರ ಕಾಪಾಡಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "लवकर येणारा करपा (Early Blight)",
                "pathogen": "बुरशी (Alternaria solani)",
                "symptoms": "पानांवर गोलाकार काळे-तपकिरी ठिपके ज्यामध्ये वर्तुळाकार वलये (Target Board) दिसतात.",
                "organic_treatment": ["ट्रायकोडर्मा किंवा कॉपर बुरशीनाशकाची फवारणी करा."],
                "chemical_treatment": ["मॅन्कोझेब किंवा डायफेनोकोनाझोल (Score) फवारा."],
                "prevention": ["पिकात योग्य अंतर ठेवा आणि खालील पाने छाटा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "முன் கருகல் நோய் (Early Blight)",
                "pathogen": "பூஞ்சை (Alternaria solani)",
                "symptoms": "இலைகளில் வட்ட வளையங்கள் போன்ற பழுப்பு நிற புள்ளிகள் தோன்றும்.",
                "organic_treatment": ["டிரைக்கோடெர்மா அல்லது காப்பர் மருந்து தெளிக்கவும்."],
                "chemical_treatment": ["மேன்கோசெப் அல்லது குளோரோதலோனில் தெளிக்கவும்."],
                "prevention": ["செடிகளுக்கு இடையே போதுமான இடைவெளி விடவும்."]
            }
        }
    },

    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "pathogen": "Oomycete (Phytophthora infestans)",
        "severity": "Severe / Critical",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Late Blight",
                "pathogen": "Oomycete (Phytophthora infestans)",
                "symptoms": "Large, irregular, water-soaked dark brown to black greasy lesions expanding rapidly across foliage. White downy mold appears on undersides during high humidity.",
                "organic_treatment": [
                    "Apply liquid copper hydroxide or Bordeaux mixture immediately upon outbreak.",
                    "Bag and destroy heavily infected vines; do not compost."
                ],
                "chemical_treatment": [
                    "Metalaxyl + Mancozeb (Ridomil Gold) or Cymoxanil applied preventively.",
                    "Dimethomorph or Fluopicolide during wet cool conditions."
                ],
                "prevention": [
                    "Plant late blight-resistant varieties (e.g., Mountain Magic, Defiant).",
                    "Eliminate volunteer tomato and potato plants nearby."
                ]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "पछेती झुलसा (Late Blight)",
                "pathogen": "ओओमीसीट (Phytophthora infestans)",
                "symptoms": "पत्तियों पर बड़े, पानी से भीगे हुए अनियमित काले-भूरे धब्बे जो तेजी से फैलते हैं। नमी में पत्ती के नीचे सफेद फफूंद दिखती है।",
                "organic_treatment": ["बोर्डो मिश्रण या कॉपर हाइड्रोक्साइड का तुरंत छिड़काव करें। संक्रमित पौधों को नष्ट करें।"],
                "chemical_treatment": ["मेटालेक्सिल + मैन्कोजेब (रिडोमिल गोल्ड) का स्प्रे करें।"],
                "prevention": ["प्रतिरोधी किस्में लगाएं और खेतों में जलभराव न होने दें।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ತಡವಾದ ಕರಗು ರೋಗ (Late Blight)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Phytophthora infestans)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ವೇಗವಾಗಿ ಹರಡುವ ಕಪ್ಪು ನೀರಿನ ಕಲೆಗಳು ಮತ್ತು ಕೆಳಭಾಗದಲ್ಲಿ ಬಿಳಿ ಶಿಲೀಂಧ್ರ.",
                "organic_treatment": ["ಬೋರ್ಡೋ ಮಿಶ್ರಣ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಮೆಟಾಲಾಕ್ಸಿಲ್ + ಮ್ಯಾಂಕೋಜೆಬ್ (Ridomil Gold) ಬಳಸಿ."],
                "prevention": ["ರೋಗ ನಿರೋಧಕ ತಳಿಗಳನ್ನು ಬೆಳೆಯಿರಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "उशिरा येणारा करपा (Late Blight)",
                "pathogen": "बुरशी (Phytophthora infestans)",
                "symptoms": "पानांवर जलमय काळे-तपकिरी मोठे चट्टे पडतात व दमट हवेत पांढरी बुरशी दिसते.",
                "organic_treatment": ["बोर्डो मिश्रण किंवा कॉपर बुरशीनाशक फवारा."],
                "chemical_treatment": ["मेटॅलॅक्सिल अधिक मॅन्कोझेब (रिडोमिल गोल्ड) फवारा."],
                "prevention": ["पाण्याचा चांगला निचरा ठेवा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "பின் கருகல் நோய் (Late Blight)",
                "pathogen": "பூஞ்சை (Phytophthora infestans)",
                "symptoms": "இலைகளில் வேகமாகப் பரவும் பெரிய கருப்பு அழுகல் புள்ளிகள்.",
                "organic_treatment": ["போர்டோ கலவை தெளிக்கவும்."],
                "chemical_treatment": ["மெட்டலாக்சில் + மேன்கோசெப் தெளிக்கவும்."],
                "prevention": ["நீர் தேங்குவதைத் தவிர்க்கவும்."]
            }
        }
    },

    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "pathogen": "Fungus (Passalora fulva)",
        "severity": "Moderate",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Leaf Mold",
                "pathogen": "Fungus (Passalora fulva)",
                "symptoms": "Pale green to yellow chlorotic spots on upper leaf surfaces; olive-green to brownish velvety mold patches on leaf undersides.",
                "organic_treatment": ["Copper octanoate sprays under leaves.", "Potassium bicarbonate spray."],
                "chemical_treatment": ["Chlorothalonil, Boscalid, or Pyraclostrobin."],
                "prevention": ["Improve greenhouse ventilation; keep humidity below 85%."]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "पत्ती फफूंद (Leaf Mold)",
                "pathogen": "कवक (Passalora fulva)",
                "symptoms": "पत्ती के ऊपरी भाग पर पीले धब्बे और निचली सतह पर जैतून जैसे भूरे-हरे रंग की मखमली फफूंद।",
                "organic_treatment": ["पत्तियों के नीचे कॉपर फफूंदनाशक का छिड़काव करें।"],
                "chemical_treatment": ["क्लोरोथैलोनिल का छिड़काव करें।"],
                "prevention": ["पॉलीहाउस में वेंटिलेशन सुधारें और नमी घटाएं।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಎಲೆ ಶಿಲೀಂಧ್ರ ರೋಗ (Leaf Mold)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Passalora fulva)",
                "symptoms": "ಎಲೆಯ ಮೇಲ್ಭಾಗದಲ್ಲಿ ಹಳದಿ ಕಲೆಗಳು, ಕೆಳಭಾಗದಲ್ಲಿ ಹಸಿರು-ಕಂದು ಬೂದಿ ಪದರ.",
                "organic_treatment": ["ತಾಮ್ರದ ದ್ರಾವಣ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಕ್ಲೋರೋಥಲೋನಿಲ್ ಬಳಸಿ."],
                "prevention": ["ಗಾಳಿ ಸಂಚಾರವನ್ನು ಹೆಚ್ಚಿಸಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "पानावरील बुरशी (Leaf Mold)",
                "pathogen": "बुरशी (Passalora fulva)",
                "symptoms": "पानाच्या वरच्या बाजूवर पिवळे डाग आणि खालच्या बाजूवर मखमली तपकिरी बुरशी.",
                "organic_treatment": ["कॉपर बुरशीनाशक पानांच्या खाली फवारा."],
                "chemical_treatment": ["क्लोरोथॅलोनिल फवारा."],
                "prevention": ["हवेतील आर्द्रता कमी ठेवा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "இலை பூஞ்சை நோய் (Leaf Mold)",
                "pathogen": "பூஞ்சை (Passalora fulva)",
                "symptoms": "இலையின் மேல் மஞ்சள் புள்ளிகளும், அடியில் வெல்வெட் போன்ற பூஞ்சையும் தோன்றும்.",
                "organic_treatment": ["காப்பர் மருந்து தெளிக்கவும்."],
                "chemical_treatment": ["குளோரோதலோனில் தெளிக்கவும்."],
                "prevention": ["காற்றோட்டத்தை அதிகரிக்கவும்."]
            }
        }
    },

    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "pathogen": "Fungus (Septoria lycopersici)",
        "severity": "Moderate to High",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Septoria Leaf Spot",
                "pathogen": "Fungus (Septoria lycopersici)",
                "symptoms": "Numerous circular small spots (1.5-3mm) with grayish-white centers and dark brown margins. Tiny black pycnidia specks visible inside lesions.",
                "organic_treatment": ["Copper octanoate sprays every 7-10 days.", "Remove infected lower leaves promptly."],
                "chemical_treatment": ["Chlorothalonil, Mancozeb, or Azoxystrobin."],
                "prevention": ["Straw mulching to stop soil splash.", "Deep plowing of crop residues."]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "सेप्टोरिया पत्ती धब्बा (Septoria Leaf Spot)",
                "pathogen": "कवक (Septoria lycopersici)",
                "symptoms": "पत्तियों पर छोटे-छोटे गोल धब्बे जिनका केंद्र सफेद-धूसर और किनारे गहरे भूरे होते हैं। केंद्र में काले बिंदु दिखते हैं।",
                "organic_treatment": ["कॉपर कवकनाशी का हर 7-10 दिन में छिड़काव करें।"],
                "chemical_treatment": ["मैन्कोजेब या क्लोरोथैलोनिल का स्प्रे करें।"],
                "prevention": ["संक्रमित निचली पत्तियों को तोड़कर नष्ट करें और मल्चिंग करें।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಸೆಪ್ಟೋರಿಯಾ ಎಲೆ ಚುಕ್ಕೆ (Septoria Leaf Spot)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Septoria lycopersici)",
                "symptoms": "ಬಿಳಿ-ಬೂದು ಮಧ್ಯಭಾಗ ಮತ್ತು ಕಂದು ಅಂಚುಳ್ಳ ಸಣ್ಣ ದುಂಡನೆಯ ಚುಕ್ಕೆಗಳು.",
                "organic_treatment": ["ತಾಮ್ರದ ಔಷಧ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಮ್ಯಾಂಕೋಜೆಬ್ ಬಳಸಿ."],
                "prevention": ["ಕೆಳಗಿನ ಸೋಂಕಿತ ಎಲೆಗಳನ್ನು ತೆಗೆಯಿರಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "सेप्टोरिया ठिपके (Septoria Leaf Spot)",
                "pathogen": "बुरशी (Septoria lycopersici)",
                "symptoms": "पानांवर लहान गोल ठिपके ज्यांचे केंद्र पांढरे-राखाडी आणि कडा गडद तपकिरी असतात.",
                "organic_treatment": ["कॉपर बुरशीनाशक फवारा."],
                "chemical_treatment": ["मॅन्कोझेबची फवारणी करा."],
                "prevention": ["खालची रोगट पाने काढून टाका."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "செப்டோரியா இலைப்புள்ளி (Septoria Leaf Spot)",
                "pathogen": "பூஞ்சை (Septoria lycopersici)",
                "symptoms": "இலைகளில் சாம்பல் நிற மையமும் பழுப்பு ஓரமும் கொண்ட சிறிய புள்ளிகள்.",
                "organic_treatment": ["காப்பர் மருந்து தெளிக்கவும்."],
                "chemical_treatment": ["மேன்கோசெப் தெளிக்கவும்."],
                "prevention": ["பாதிக்கப்பட்ட கீழ் இலைகளை அகற்றவும்."]
            }
        }
    },

    "Tomato___Spider_mites_Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Two-Spotted Spider Mites",
        "pathogen": "Pest / Arachnid (Tetranychus urticae)",
        "severity": "Moderate to High",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Spider Mites",
                "pathogen": "Pest (Tetranychus urticae)",
                "symptoms": "Fine yellow or white stippling speckles across leaf surface. Silken webs visible on leaf undersides; severe infestation turns leaves bronze and crispy.",
                "organic_treatment": ["Insecticidal soap or 1-2% neem oil targeting leaf undersides.", "Release predatory mites (Phytoseiulus persimilis)."],
                "chemical_treatment": ["Abamectin, Bifenazate, or Spiromesifen miticides."],
                "prevention": ["Avoid water stress; keep plants adequately irrigated in hot weather."]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "मकड़ी कीट / स्पाइडर माइट (Spider Mites)",
                "pathogen": "कीट (Tetranychus urticae)",
                "symptoms": "पत्तियों पर पीले या सफेद बारीक बिंदु (धब्बे) और पत्ती के नीचे महीन जाले। पत्तियां सूखकर भूरी हो जाती हैं।",
                "organic_treatment": ["पत्ती के नीचे 1% नीम तेल या कीटनाशक साबुन का स्प्रे करें।"],
                "chemical_treatment": ["एबामेक्टिन (Abamectin) या स्पाइरोमेसिफेन का छिड़काव करें।"],
                "prevention": ["गर्मियों में खेत में नमी बनाए रखें।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಜೇಡರ ಹುಳು ರೋಗ (Spider Mites)",
                "pathogen": "ಕೀಟ (Tetranychus urticae)",
                "symptoms": "ಎಲೆಯ ಮೇಲೆ ಸಣ್ಣ ಹಳದಿ ಚುಕ್ಕೆಗಳು ಮತ್ತು ಎಲೆಯ ಕೆಳಗೆ ಜೇಡರ ಬಲೆ.",
                "organic_treatment": ["ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಅಬಾಮೆಕ್ಟಿನ್ ಸಿಂಪಡಿಸಿ."],
                "prevention": ["ತೇವಾಂಶ ಕಾಪಾಡಿಕೊಳ್ಳಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "लाल कोळी / स्पायडर माईट (Spider Mites)",
                "pathogen": "कीटक (Tetranychus urticae)",
                "symptoms": "पानांवर बारीक पिवळे ठिपके आणि पाठीमागे बारीक जाळे दिसतात. पाने तांबूस होतात.",
                "organic_treatment": ["१% निंबोळी अर्क किंवा कीटकनाशक साबण फवारा."],
                "chemical_treatment": ["अ‍ॅबामेक्टींन किंवा स्पायरोमेसीफेन फवारा."],
                "prevention": ["उष्ण हवामानात पाण्याचा ताण पडू देऊ नका."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "செம்பேன் / சிலந்திப் பூச்சி (Spider Mites)",
                "pathogen": "பூச்சி (Tetranychus urticae)",
                "symptoms": "இலைகளில் மஞ்சள் நிற புள்ளிகள் மற்றும் அடியில் சிலந்தி வலைகள்.",
                "organic_treatment": ["வேப்பெண்ணெய் தெளிக்கவும்."],
                "chemical_treatment": ["அபாமெக்டின் தெளிக்கவும்."],
                "prevention": ["முறையான பாசனம் செய்யவும்."]
            }
        }
    },

    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "pathogen": "Fungus (Corynespora cassiicola)",
        "severity": "Moderate",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Target Spot",
                "pathogen": "Fungus (Corynespora cassiicola)",
                "symptoms": "Brown circular lesions with light brown centers and dark brown margins, often with faint concentric rings coalescing to cause extensive foliar blighting.",
                "organic_treatment": ["Liquid copper fungicides combined with bio-fungicide Bacillus amyloliquefaciens."],
                "chemical_treatment": ["Azoxystrobin + Difenoconazole (Quadris Top) or Boscalid."],
                "prevention": ["3-year crop rotation with non-host crops.", "Avoid overhead irrigation."]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "टारगेट स्पॉट (Target Spot)",
                "pathogen": "कवक (Corynespora cassiicola)",
                "symptoms": "हल्के भूरे केंद्र और गहरे भूरे किनारों वाले गोल धब्बे, जो आपस में मिलकर पूरी पत्ती को झुलसा देते हैं।",
                "organic_treatment": ["कॉपर कवकनाशी या जैविक बैसिलस का छिड़काव करें।"],
                "chemical_treatment": ["एज़ोक्सीस्ट्रोबिन या डाइफेनोकोनाज़ोल का छिड़काव करें।"],
                "prevention": ["3 वर्ष का फसल चक्र अपनाएं।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಟಾರ್ಗೆಟ್ ಸ್ಪಾಟ್ (Target Spot)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Corynespora cassiicola)",
                "symptoms": "ಕಂದು ಬಣ್ಣದ ದುಂಡನೆಯ ಚುಕ್ಕೆಗಳು ಒಟ್ಟಾಗಿ ಎಲೆಯನ್ನು ಒಣಗಿಸುತ್ತವೆ.",
                "organic_treatment": ["ತಾಮ್ರದ ಕವಕನಾಶಕ ಬಳಸಿ."],
                "chemical_treatment": ["ಅಜೋಕ್ಸಿಸ್ಟ್ರೋಬಿನ್ ಸಿಂಪಡಿಸಿ."],
                "prevention": ["ಬೆಳೆ ಪರಿವರ್ತನೆ ಮಾಡಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "टारगेट स्पॉट (Target Spot)",
                "pathogen": "बुरशी (Corynespora cassiicola)",
                "symptoms": "तपकिरी गोलाकार डाग ज्यांचे केंद्र फिकट आणि कडा गडद असतात.",
                "organic_treatment": ["कॉपर बुरशीनाशक वापरा."],
                "chemical_treatment": ["अझोक्सीस्ट्रोबिन फवारा."],
                "prevention": ["पीक फेरपालट करा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "டார்கெட் ஸ்பாட் (Target Spot)",
                "pathogen": "பூஞ்சை (Corynespora cassiicola)",
                "symptoms": "பழுப்பு நிற வட்ட புள்ளிகள் ஒன்றிணைந்து இலையைக் கருக வைக்கும்.",
                "organic_treatment": ["காப்பர் மருந்து தெளிக்கவும்."],
                "chemical_treatment": ["அசாசிஸ்ட்ரோபின் தெளிக்கவும்."],
                "prevention": ["பயிர் சுழற்சி செய்யவும்."]
            }
        }
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Yellow Leaf Curl Virus",
        "pathogen": "Virus (Begomovirus / Whitefly vector)",
        "severity": "Severe / Critical",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Yellow Leaf Curl Virus (TYLCV)",
                "pathogen": "Virus (transmitted by Whiteflies)",
                "symptoms": "Upward curling and cupping of leaf margins, severe chlorosis (yellowing) between veins, stunted bushy plant growth, and extensive flower drop.",
                "organic_treatment": [
                    "Control whitefly vectors using yellow sticky traps and reflective silver mulches.",
                    "Spray neem oil (1%) or insecticidal soap to reduce whitefly vectors.",
                    "Rogue and destroy infected plants immediately (no chemical cure for viruses)."
                ],
                "chemical_treatment": [
                    "Control whitefly vectors with Imidacloprid, Dinotefuran, or Spirotetramat systemic insecticides."
                ],
                "prevention": [
                    "Plant TYLCV-resistant tomato hybrids (e.g., Tycoon, Charger).",
                    "Install 50-mesh insect screening in nurseries."
                ]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "पत्ती मरोड़ / पीला पर्ण कुंचन वायरस (TYLCV)",
                "pathogen": "विषाणु (सफेद मक्खी द्वारा प्रसारित)",
                "symptoms": "पत्तियां ऊपर की ओर मुड़कर कटोरी जैसी हो जाती हैं, नसों के बीच पीलापन, पौधा बौना व झाड़ीनुमा हो जाता है और फूल गिर जाते हैं।",
                "organic_treatment": [
                    "पीले चिपचिपे कार्ड (Yellow sticky traps) लगाएं।",
                    "नीम तेल का छिड़काव कर सफेद मक्खी (Whitefly) को नियंत्रित करें।",
                    "संक्रमित पौधों को उखाड़कर नष्ट करें।"
                ],
                "chemical_treatment": [
                    "सफेद मक्खी के नियंत्रण के लिए इमिडाक्लोप्रिड (Imidacloprid) का छिड़काव करें।"
                ],
                "prevention": [
                    "प्रतिरोधी संकर किस्में लगाएं और 50-मेश जाली का उपयोग करें।"
                ]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಎಲೆ ಸುರುಟು ರೋಗ (TYLCV)",
                "pathogen": "ವೈರಸ್ (ಬಿಳಿ ನೊಣದಿಂದ ಹರಡುತ್ತದೆ)",
                "symptoms": "ಎಲೆಗಳು ಮೇಲ್ಮುಖವಾಗಿ ಸುರುಟಿಕೊಳ್ಳುತ್ತವೆ, ಹಳದಿಯಾಗುತ್ತವೆ ಮತ್ತು ಗಿಡ ಕುಬ್ಜವಾಗುತ್ತದೆ.",
                "organic_treatment": ["ಹಳದಿ ಜಿಗುಟು ಬಲೆಗಳನ್ನು ಬಳಸಿ ಮತ್ತು ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಇಮಿಡಾಕ್ಲೋಪ್ರಿಡ್ ಬಳಸಿ ಬಿಳಿ ನೊಣಗಳನ್ನು ನಿಯಂತ್ರಿಸಿ."],
                "prevention": ["ರೋಗ ನಿರೋಧಕ ತಳಿಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "पिवळा पानांचा चुरडा-मुरडा (TYLCV)",
                "pathogen": "विषाणू (पांढऱ्या माशीद्वारे प्रसार)",
                "symptoms": "पाने वरच्या बाजूला वाटीसारखी वळतात, शिरांमधील भाग पिवळा पडतो आणि झाड खुजे होते.",
                "organic_treatment": ["पिवळे चिकट सापळे लावा आणि निंबोळी तेल फवारा."],
                "chemical_treatment": ["पांढऱ्या माशीच्या नियंत्रणासाठी इमिडाक्लोप्रिड फवारा."],
                "prevention": ["रोगप्रतिकारक संकरित बियाणे वापरा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "இலை சுருட்டு வைரஸ் (TYLCV)",
                "pathogen": "வைரஸ் (வெள்ளை ஈக்களால் பரவுகிறது)",
                "symptoms": "இலைகள் மேல்நோக்கி கிண்ணம் போல சுருண்டு மஞ்சள் நிறமாக மாறும்.",
                "organic_treatment": ["மஞ்சள் ஒட்டும் பொறிகளைப் பயன்படுத்தவும்."],
                "chemical_treatment": ["இமிடாக்ளோபிரிட் தெளித்து வெள்ளை ஈக்களைக் கட்டுப்படுத்தவும்."],
                "prevention": ["நோய் எதிர்ப்பு ரகங்களைப் பயிரிடவும்."]
            }
        }
    },

    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Mosaic Virus",
        "pathogen": "Virus (Tobamovirus / Contact transmitted)",
        "severity": "Moderate to High",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Tomato Mosaic Virus (ToMV)",
                "pathogen": "Virus (Mechanically transmitted)",
                "symptoms": "Mottled light and dark green mosaic pattern on foliage, leaf distortion or 'fern-like' shoestringing, and stunted plant vigor.",
                "organic_treatment": [
                    "Remove and incinerate infected plants immediately.",
                    "Dip pruning tools in 20% non-fat dry milk solution or 10% trisodium phosphate."
                ],
                "chemical_treatment": [
                    "No direct chemical cure for plant viruses. Focus on strict tool disinfection."
                ],
                "prevention": [
                    "Plant ToMV-resistant cultivars.",
                    "Do not smoke or handle tobacco products prior to working in tomato beds."
                ]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "मोज़ेक वायरस (Mosaic Virus)",
                "pathogen": "विषाणु (स्पर्श द्वारा प्रसारित)",
                "symptoms": "पत्तियों पर हल्के और गहरे हरे रंग के चितकबरे धब्बे (मोज़ेक), पत्तियों का सिकुड़ना या धागेनुमा होना।",
                "organic_treatment": ["संक्रमित पौधों को तुरंत उखाड़कर नष्ट करें। औजारों को दूध के घोल या सैनिटाइज़र से धोएं।"],
                "chemical_treatment": ["वायरस के लिए कोई रासायनिक दवा नहीं है। स्वच्छता पर ध्यान दें।"],
                "prevention": ["तंबाकू उत्पादों को छूने के बाद पौधों को न छुएं। प्रतिरोधी किस्में लगाएं।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಮೊಸಾಯಿಕ್ ವೈರಸ್ (Mosaic Virus)",
                "pathogen": "ವೈರಸ್",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ತಿಳಿ ಮತ್ತು ದಟ್ಟ ಹಸಿರು ಚುಕ್ಕೆಗಳ ಮೊಸಾಯಿಕ್ ಮಾದರಿ.",
                "organic_treatment": ["ಸೋಂಕಿತ ಗಿಡಗಳನ್ನು ನಾಶಪಡಿಸಿ."],
                "chemical_treatment": ["ಯಾವುದೇ ರಾಸಾಯನಿಕ ಔಷಧವಿಲ್ಲ."],
                "prevention": ["ಉಪಕರಣಗಳನ್ನು ಶುಚಿಯಾಗಿಡಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "मोझॅक व्हायरस (Mosaic Virus)",
                "pathogen": "विषाणू",
                "symptoms": "पानांवर फिकट व गडद हिरवे पट्टे (मोझॅक) आणि पाने विकृत होतात.",
                "organic_treatment": ["रोगट झाडे उपटून जाळून टाका."],
                "chemical_treatment": ["विषाणूंवर थेट औषध उपलब्ध नाही."],
                "prevention": ["तंबाखू हाताळल्यानंतर पिकाला हात लावू नका."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "மொசைக் வைரஸ் (Mosaic Virus)",
                "pathogen": "வைரஸ்",
                "symptoms": "இலைகளில் வெளிர் மற்றும் அடர் பச்சை நிற தேமல் புள்ளிகள் தோன்றும்.",
                "organic_treatment": ["பாதிக்கப்பட்ட செடிகளை அழிக்கவும்."],
                "chemical_treatment": ["மருந்து இல்லை."],
                "prevention": ["தூய்மை பராமரிக்கவும்."]
            }
        }
    },

    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy Leaf",
        "pathogen": "None",
        "severity": "Healthy",
        "translations": {
            "en": {
                "crop_name": "Tomato",
                "disease_name": "Healthy Tomato Leaf",
                "pathogen": "None (Plant is healthy)",
                "symptoms": "Foliage is uniformly vibrant green, firm, free of lesions, curling, webbing, or chlorotic halos.",
                "organic_treatment": ["Apply balanced vermicompost and foliar seaweed extract every 14 days."],
                "chemical_treatment": ["None required. Maintain balanced N-P-K-Ca nutrition."],
                "prevention": ["Consistent drip irrigation and clean organic mulching."]
            },
            "hi": {
                "crop_name": "टमाटर (Tomato)",
                "disease_name": "स्वस्थ पत्ती (Healthy)",
                "pathogen": "कोई नहीं",
                "symptoms": "पत्ती पूरी तरह से हरी, चमकदार और रोगमुक्त है।",
                "organic_treatment": ["संतुलित जैविक खाद और समुद्री शैवाल अर्क दें।"],
                "chemical_treatment": ["किसी दवा की आवश्यकता नहीं है।"],
                "prevention": ["नियमित ड्रिप सिंचाई करें।"]
            },
            "kn": {
                "crop_name": "ಟೊಮೆಟೊ (Tomato)",
                "disease_name": "ಆರೋಗ್ಯಕರ ಎಲೆ (Healthy)",
                "pathogen": "ಯಾವುದೂ ಇಲ್ಲ",
                "symptoms": "ಎಲೆಗಳು ಶುಭ್ರ ಹಸಿರಾಗಿದ್ದು, ರೋಗಮುಕ್ತವಾಗಿವೆ.",
                "organic_treatment": ["ಸಾವಯವ ಗೊಬ್ಬರ ನೀಡಿ."],
                "chemical_treatment": ["ಯಾವುದೇ ಅಗತ್ಯವಿಲ್ಲ."],
                "prevention": ["ಹನಿ ನೀರಾವರಿ ಪಾಲಿಸಿ."]
            },
            "mr": {
                "crop_name": "टोमॅटो (Tomato)",
                "disease_name": "निरोगी पान (Healthy)",
                "pathogen": "काही नाही",
                "symptoms": "पाने गर्द हिरवीगार आणि कोणत्याही डागांशिवाय निरोगी आहेत.",
                "organic_treatment": ["सेंद्रिय खतांचा वापर करा."],
                "chemical_treatment": ["कोणत्याही औषधांची गरज नाही."],
                "prevention": ["ठिबक सिंचन चालू ठेवा."]
            },
            "ta": {
                "crop_name": "தக்காளி (Tomato)",
                "disease_name": "ஆரோக்கியமான இலை (Healthy)",
                "pathogen": "எதுவும் இல்லை",
                "symptoms": "இலைகள் பசுமையாக ஆரோக்கியமாக உள்ளன.",
                "organic_treatment": ["இயற்கை உரங்கள் இடவும்."],
                "chemical_treatment": ["தேவையில்லை."],
                "prevention": ["சொட்டு நீர் பாசனம் செய்யவும்."]
            }
        }
    },

    # ==================== POTATO (3 CLASSES) ====================
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "pathogen": "Fungus (Alternaria solani)",
        "severity": "Moderate to High",
        "translations": {
            "en": {
                "crop_name": "Potato",
                "disease_name": "Early Blight",
                "pathogen": "Fungus (Alternaria solani)",
                "symptoms": "Dark brown circular or angular spots with distinct concentric rings ('target' pattern) on older lower leaves, causing premature vine death.",
                "organic_treatment": ["Copper hydroxide sprays every 7-10 days.", "Apply bio-fungicides with Bacillus subtilis."],
                "chemical_treatment": ["Chlorothalonil, Mancozeb, Pyraclostrobin, or Boscalid."],
                "prevention": ["Plant certified disease-free seed tubers.", "Minimum 3-year rotation away from solanaceous crops."]
            },
            "hi": {
                "crop_name": "आलू (Potato)",
                "disease_name": "अगेती झुलसा (Early Blight)",
                "pathogen": "कवक (Alternaria solani)",
                "symptoms": "पुरानी पत्तियों पर गोल या कोणीय भूरे धब्बे जिनके अंदर संकेंद्री छल्ले (Target rings) बनते हैं।",
                "organic_treatment": ["कॉपर कवकनाशी या जैविक बैसिलस का छिड़काव करें।"],
                "chemical_treatment": ["मैन्कोजेब या क्लोरोथैलोनिल का स्प्रे करें।"],
                "prevention": ["प्रमाणित रोगमुक्त आलू के बीज बोएं और 3 वर्ष का फसल चक्र रखें।"]
            },
            "kn": {
                "crop_name": "ಆಲೂಗಡ್ಡೆ (Potato)",
                "disease_name": "ಮುಂಚಿನ ಕರಗು ರೋಗ (Early Blight)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Alternaria solani)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ಚಕ್ರಾಕಾರದ ಕಂದು ಕಲೆಗಳು.",
                "organic_treatment": ["ತಾಮ್ರದ ಕವಕನಾಶಕ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಮ್ಯಾಂಕೋಜೆಬ್ ಬಳಸಿ."],
                "prevention": ["ರೋಗಮುಕ್ತ ಬೀಜಗೆಡ್ಡೆಗಳನ್ನು ಬಳಸಿ."]
            },
            "mr": {
                "crop_name": "बटाटा (Potato)",
                "disease_name": "लवकर येणारा करपा (Early Blight)",
                "pathogen": "बुरशी (Alternaria solani)",
                "symptoms": "खालच्या पानांवर गोल, वलयाकार तपकिरी डाग पडतात.",
                "organic_treatment": ["कॉपर बुरशीनाशकाची फवारणी करा."],
                "chemical_treatment": ["मॅन्कोझेब किंवा क्लोरोथॅलोनिल फवारा."],
                "prevention": ["प्रमाणित बियाणे वापरा."]
            },
            "ta": {
                "crop_name": "உருளைக்கிழங்கு (Potato)",
                "disease_name": "முன் கருகல் நோய் (Early Blight)",
                "pathogen": "பூஞ்சை (Alternaria solani)",
                "symptoms": "இலைகளில் வட்ட வளையங்கள் போன்ற பழுப்பு நிற புள்ளிகள்.",
                "organic_treatment": ["காப்பர் மருந்து தெளிக்கவும்."],
                "chemical_treatment": ["மேன்கோசெப் தெளிக்கவும்."],
                "prevention": ["சான்றளிக்கப்பட்ட விதைக்கிழங்குகளைப் பயன்படுத்தவும்."]
            }
        }
    },

    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "pathogen": "Oomycete (Phytophthora infestans)",
        "severity": "Severe / Critical",
        "translations": {
            "en": {
                "crop_name": "Potato",
                "disease_name": "Late Blight",
                "pathogen": "Oomycete (Phytophthora infestans)",
                "symptoms": "Water-soaked irregular black/dark-brown blotches with pale green margins rapidly destroying foliage. White downy mold on lower surface during humid weather.",
                "organic_treatment": ["Bordeaux mixture or copper hydroxide applied protectively prior to spore dispersal."],
                "chemical_treatment": ["Mandipropamid (Revus), Cyazofamid (Ranman), or Metalaxyl + Mancozeb."],
                "prevention": ["Destroy cull potato piles (primary source of spores). Deep hilling to shield tubers."]
            },
            "hi": {
                "crop_name": "आलू (Potato)",
                "disease_name": "पछेती झुलसा (Late Blight)",
                "pathogen": "ओओमीसीट (Phytophthora infestans)",
                "symptoms": "पत्तियों पर पानी से भीगे हुए काले-भूरे धब्बे जो पूरी फसल को कुछ ही दिनों में नष्ट कर देते हैं। निचली सतह पर सफेद फफूंद।",
                "organic_treatment": ["बोर्डो मिश्रण का छिड़काव करें। खराब पौधों को जला दें।"],
                "chemical_treatment": ["रिडोमिल गोल्ड (Metalaxyl + Mancozeb) का तुरंत छिड़काव करें।"],
                "prevention": ["खेत के पास बेकार आलू के ढेर न रहने दें और कंदों पर गहरी मिट्टी चढ़ाएं।"]
            },
            "kn": {
                "crop_name": "ಆಲೂಗಡ್ಡೆ (Potato)",
                "disease_name": "ತಡವಾದ ಕರಗು ರೋಗ (Late Blight)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Phytophthora infestans)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ಕಪ್ಪು ನೀರಿನ ಕಲೆಗಳು ಮತ್ತು ಬೆಳೆಯನ್ನು ಸಂಪೂರ್ಣ ನಾಶಮಾಡುವ ಶಿಲೀಂಧ್ರ.",
                "organic_treatment": ["ಬೋರ್ಡೋ ದ್ರಾವಣ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ರಿಡೋಮಿಲ್ ಗೋಲ್ಡ್ ಬಳಸಿ."],
                "prevention": ["ಗೆಡ್ಡೆಗಳ ಮೇಲೆ ಮಣ್ಣನ್ನು ಸರಿಯಾಗಿ ಮುಚ್ಚಿ."]
            },
            "mr": {
                "crop_name": "बटाटा (Potato)",
                "disease_name": "उशिरा येणारा करपा (Late Blight)",
                "pathogen": "बुरशी (Phytophthora infestans)",
                "symptoms": "पानांवर जलमय काळे-तपकिरी डाग जे काही दिवसांत संपूर्ण पीक नष्ट करतात.",
                "organic_treatment": ["बोर्डो मिश्रण फवारा."],
                "chemical_treatment": ["रिडोमिल गोल्डची तात्काळ फवारणी करा."],
                "prevention": ["झाडांना योग्य मातीची भर लावा."]
            },
            "ta": {
                "crop_name": "உருளைக்கிழங்கு (Potato)",
                "disease_name": "பின் கருகல் நோய் (Late Blight)",
                "pathogen": "பூஞ்சை (Phytophthora infestans)",
                "symptoms": "இலைகளில் வேகமாகப் பரவும் பெரிய கருப்பு அழுகல் புள்ளிகள்.",
                "organic_treatment": ["போர்டோ கலவை தெளிக்கவும்."],
                "chemical_treatment": ["ரிடோமில் கோல்ட் தெளிக்கவும்."],
                "prevention": ["கிழங்குகளை மூடி மண் அணைக்கவும்."]
            }
        }
    },

    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy Leaf",
        "pathogen": "None",
        "severity": "Healthy",
        "translations": {
            "en": {
                "crop_name": "Potato",
                "disease_name": "Healthy Potato Leaf",
                "pathogen": "None",
                "symptoms": "Leaves are smooth, deep green, crisp, and robust with no dark necrotic rings or mildew present.",
                "organic_treatment": ["Apply balanced seaweed extract and mycorrhizal inoculant."],
                "chemical_treatment": ["None required."],
                "prevention": ["Ensure proper hilling and maintain steady moisture."]
            },
            "hi": {
                "crop_name": "आलू (Potato)",
                "disease_name": "स्वस्थ पत्ती (Healthy)",
                "pathogen": "कोई नहीं",
                "symptoms": "पत्ती गहरी हरी, चिकनी और मजबूत है। कोई धब्बा नहीं है।",
                "organic_treatment": ["संतुलित खाद दें।"],
                "chemical_treatment": ["किसी दवा की आवश्यकता नहीं है।"],
                "prevention": ["समय पर मिट्टी चढ़ाएं।"]
            },
            "kn": {
                "crop_name": "ಆಲೂಗಡ್ಡೆ (Potato)",
                "disease_name": "ಆರೋಗ್ಯಕರ ಎಲೆ (Healthy)",
                "pathogen": "ಯಾವುದೂ ಇಲ್ಲ",
                "symptoms": "ಎಲೆಗಳು ಶುಭ್ರ ಹಸಿರಾಗಿದ್ದು ರೋಗಮುಕ್ತವಾಗಿವೆ.",
                "organic_treatment": ["ಸಾವಯವ ಗೊಬ್ಬರ ನೀಡಿ."],
                "chemical_treatment": ["ಯಾವುದೇ ಅಗತ್ಯವಿಲ್ಲ."],
                "prevention": ["ಸಮರ್ಪಕ ನೀರು ನಿರ್ವಹಣೆ ಮಾಡಿ."]
            },
            "mr": {
                "crop_name": "बटाटा (Potato)",
                "disease_name": "निरोगी पान (Healthy)",
                "pathogen": "काही नाही",
                "symptoms": "पाने गडद हिरवीगार व निरोगी आहेत.",
                "organic_treatment": ["सेंद्रिय खते द्या."],
                "chemical_treatment": ["कोणत्याही औषधांची गरज नाही."],
                "prevention": ["मातीची योग्य भर लावा."]
            },
            "ta": {
                "crop_name": "உருளைக்கிழங்கு (Potato)",
                "disease_name": "ஆரோக்கியமான இலை (Healthy)",
                "pathogen": "எதுவும் இல்லை",
                "symptoms": "இலைகள் புள்ளிகள் இன்றி பசுமையாக உள்ளன.",
                "organic_treatment": ["இயற்கை உரங்கள் இடவும்."],
                "chemical_treatment": ["தேவையில்லை."],
                "prevention": ["சரியான பாசனம் செய்யவும்."]
            }
        }
    },

    # ==================== CAPSICUM / BELL PEPPER (2 CLASSES) ====================
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Capsicum",
        "disease": "Bacterial Spot",
        "pathogen": "Bacterium (Xanthomonas euvesicatoria)",
        "severity": "High",
        "translations": {
            "en": {
                "crop_name": "Capsicum (Bell Pepper)",
                "disease_name": "Bacterial Spot",
                "pathogen": "Bacterium (Xanthomonas euvesicatoria)",
                "symptoms": "Small, water-soaked, circular to irregular lesions (1-3mm) turning dark brown to black with chlorotic yellow halos, causing severe defoliation.",
                "organic_treatment": ["Copper octanoate or fixed copper bactericide sprays.", "Bacillus subtilis bio-fungicide."],
                "chemical_treatment": ["Fixed copper hydroxide tank-mixed with Mancozeb."],
                "prevention": ["Use certified disease-free seeds and resistant hybrids.", "Drip irrigation."]
            },
            "hi": {
                "crop_name": "शिमला मिर्च (Capsicum)",
                "disease_name": "जीवाणु पत्ती धब्बा (Bacterial Spot)",
                "pathogen": "जीवाणु (Xanthomonas euvesicatoria)",
                "symptoms": "पत्तियों पर 1-3 मिमी के काले-भूरे धब्बे जिनके चारों ओर पीला घेरा होता है। पत्तियां तेजी से झड़ती हैं।",
                "organic_treatment": ["कॉपर सोप या नीम तेल का छिड़काव करें।"],
                "chemical_treatment": ["कॉपर हाइड्रोक्साइड + मैन्कोजेब मिलाकर स्प्रे करें।"],
                "prevention": ["रोगमुक्त बीज लगाएं और ड्रिप सिंचाई करें।"]
            },
            "kn": {
                "crop_name": "ಕ್ಯಾಪ್ಸಿಕಂ (Capsicum)",
                "disease_name": "ಬ್ಯಾಕ್ಟೀರಿಯಲ್ ಎಲೆ ಚುಕ್ಕೆ (Bacterial Spot)",
                "pathogen": "ಬ್ಯಾಕ್ಟೀರಿಯಾ (Xanthomonas euvesicatoria)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ನೀರಿನಿಂದ ಕೂಡಿದ ಸಣ್ಣ ಕಪ್ಪು ಚುಕ್ಕೆಗಳು ಹಳದಿ ಅಂಚಿನೊಂದಿಗೆ ಕಾಣಿಸಿಕೊಳ್ಳುತ್ತವೆ.",
                "organic_treatment": ["ತಾಮ್ರದ ಸಾಬೂನು ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಕಾಪರ್ ಹೈಡ್ರಾಕ್ಸೈಡ್ + ಮ್ಯಾಂಕೋಜೆಬ್ ಬಳಸಿ."],
                "prevention": ["ಹನಿ ನೀರಾವರಿ ಪಾಲಿಸಿ."]
            },
            "mr": {
                "crop_name": "ढोबळी मिरची (Capsicum)",
                "disease_name": "जिवाणूजन्य करपा (Bacterial Spot)",
                "pathogen": "जिवाणू (Xanthomonas euvesicatoria)",
                "symptoms": "पानांवर लहान, काळे-तपकिरी रंगाचे डाग पिवळ्या वलयांसह दिसतात.",
                "organic_treatment": ["कॉपर सोपची फवारणी करा."],
                "chemical_treatment": ["कॉपर हायड्रॉक्साईड + मॅन्कोझेब फवारा."],
                "prevention": ["ठिबक सिंचन वापरा."]
            },
            "ta": {
                "crop_name": "குடைமிளகாய் (Capsicum)",
                "disease_name": "பாக்டீரியா இலைப்புள்ளி (Bacterial Spot)",
                "pathogen": "பாக்டீரியா (Xanthomonas euvesicatoria)",
                "symptoms": "இலைகளில் சிறிய நீர் ஊறிய கரும் புள்ளிகள் மஞ்சள் வளையத்துடன் தோன்றும்.",
                "organic_treatment": ["காப்பர் மருந்து தெளிக்கவும்."],
                "chemical_treatment": ["காப்பர் ஹைட்ராக்சைடு + மேன்கோசெப் தெளிக்கவும்."],
                "prevention": ["சொட்டு நீர் பாசனம் செய்யவும்."]
            }
        }
    },

    "Pepper,_bell___healthy": {
        "crop": "Capsicum",
        "disease": "Healthy Leaf",
        "pathogen": "None",
        "severity": "Healthy",
        "translations": {
            "en": {
                "crop_name": "Capsicum (Bell Pepper)",
                "disease_name": "Healthy Plant Leaf",
                "pathogen": "None",
                "symptoms": "Smooth, glossy, emerald green pointed leaves with uniform texture, no spots, blisters, or yellowing.",
                "organic_treatment": ["Foliar calcium and magnesium spray (Epsom salts) to promote cell wall strength."],
                "chemical_treatment": ["None required."],
                "prevention": ["Maintain warm root zone temperatures and avoid waterlogging."]
            },
            "hi": {
                "crop_name": "शिमला मिर्च (Capsicum)",
                "disease_name": "स्वस्थ पत्ती (Healthy)",
                "pathogen": "कोई नहीं",
                "symptoms": "पत्ती पूरी तरह से चमकदार हरी, चिकनी और रोगमुक्त है।",
                "organic_treatment": ["कैल्शियम और मैग्नीशियम का छिड़काव करें।"],
                "chemical_treatment": ["किसी दवा की आवश्यकता नहीं है।"],
                "prevention": ["खेत में जलभराव न होने दें।"]
            },
            "kn": {
                "crop_name": "ಕ್ಯಾಪ್ಸಿಕಂ (Capsicum)",
                "disease_name": "ಆರೋಗ್ಯಕರ ಎಲೆ (Healthy)",
                "pathogen": "ಯಾವುದೂ ಇಲ್ಲ",
                "symptoms": "ಎಲೆಗಳು ಶುಭ್ರ ಹಸಿರಾಗಿದ್ದು ರೋಗಮುಕ್ತವಾಗಿವೆ.",
                "organic_treatment": ["ಸಾವಯವ ಗೊಬ್ಬರ ನೀಡಿ."],
                "chemical_treatment": ["ಯಾವುದೇ ಅಗತ್ಯವಿಲ್ಲ."],
                "prevention": ["ನೀರು ನಿಲ್ಲದಂತೆ ನೋಡಿಕೊಳ್ಳಿ."]
            },
            "mr": {
                "crop_name": "ढोबळी मिरची (Capsicum)",
                "disease_name": "निरोगी पान (Healthy)",
                "pathogen": "काही नाही",
                "symptoms": "पाने गडद हिरवीगार व चमकदार आहेत.",
                "organic_treatment": ["सेंद्रिय खते द्या."],
                "chemical_treatment": ["कोणत्याही औषधांची गरज नाही."],
                "prevention": ["पाण्याचा निचरा योग्य ठेवा."]
            },
            "ta": {
                "crop_name": "குடைமிளகாய் (Capsicum)",
                "disease_name": "ஆரோக்கியமான இலை (Healthy)",
                "pathogen": "எதுவும் இல்லை",
                "symptoms": "இலைகள் பசுமையாக ஆரோக்கியமாக உள்ளன.",
                "organic_treatment": ["இயற்கை உரங்கள் இடவும்."],
                "chemical_treatment": ["தேவையில்லை."],
                "prevention": ["நீர் தேங்காமல் பராமரிக்கவும்."]
            }
        }
    },

    # ==================== GRAPES (4 CLASSES) ====================
    "Grape___Black_rot": {
        "crop": "Grapes",
        "disease": "Black Rot",
        "pathogen": "Fungus (Guignardia bidwellii)",
        "severity": "High",
        "translations": {
            "en": {
                "crop_name": "Grapes",
                "disease_name": "Black Rot",
                "pathogen": "Fungus (Guignardia bidwellii)",
                "symptoms": "Small, reddish-brown circular spots on leaf upper surface with dark borders and tiny black pycnidia pimples. Berries shrivel into hard black mummies.",
                "organic_treatment": ["Copper hydroxide or sulfur sprays from bud-break.", "Prune away mummified grape clusters."],
                "chemical_treatment": ["Myclobutanil (Rally 40WSP), Mancozeb, or Tebuconazole."],
                "prevention": ["Canopy shoot positioning for sunlight exposure.", "Clean vineyard floor."]
            },
            "hi": {
                "crop_name": "अंगूर (Grapes)",
                "disease_name": "काला सड़न रोग (Black Rot)",
                "pathogen": "कवक (Guignardia bidwellii)",
                "symptoms": "पत्तियों पर लाल-भूरे रंग के गोल धब्बे और उनके अंदर छोटे काले दाने। फल काले होकर सूख जाते हैं।",
                "organic_treatment": ["कॉपर सल्फेट या सल्फर का छिड़काव करें।"],
                "chemical_treatment": ["माइक्लोबुटानिल या मैन्कोजेब का छिड़काव करें।"],
                "prevention": ["बेलों की छंटाई करें ताकि धूप मिले।"]
            },
            "kn": {
                "crop_name": "ದ್ರಾಕ್ಷಿ (Grapes)",
                "disease_name": "ಕಪ್ಪು ಕೊಳೆ ರೋಗ (Black Rot)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Guignardia bidwellii)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ಕೆಂಪು-ಕಂದು ಚುಕ್ಕೆಗಳು, ಹಣ್ಣುಗಳು ಕಪ್ಪಾಗಿ ಒಣಗುತ್ತವೆ.",
                "organic_treatment": ["ಬೋರ್ಡೋ ದ್ರಾವಣ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಮೈಕ್ಲೋಬುಟಾನಿಲ್ ಸಿಂಪಡಿಸಿ."],
                "prevention": ["ಸಮರ್ಪಕ ಗಾಳಿ-ಬೆಳಕು ಒದಗಿಸಿ."]
            },
            "mr": {
                "crop_name": "द्राक्षे (Grapes)",
                "disease_name": "काळा कुजवा (Black Rot)",
                "pathogen": "बुरशी (Guignardia bidwellii)",
                "symptoms": "पानांवर लालसर-तपकिरी गोल डाग पडतात व मणी काळे पडून सुकून जातात.",
                "organic_treatment": ["कॉपर हायड्रॉक्साईड किंवा गंधकाची फवारणी करा."],
                "chemical_treatment": ["मायक्लोब्युटॅनिल किंवा मॅन्कोझेब फवारा."],
                "prevention": ["वेलींची योग्य छाटणी करा."]
            },
            "ta": {
                "crop_name": "திராட்சை (Grapes)",
                "disease_name": "கருப்பு அழுகல் (Black Rot)",
                "pathogen": "பூஞ்சை (Guignardia bidwellii)",
                "symptoms": "இலைகளில் சிவப்பு-பழுப்பு வட்ட புள்ளிகள் தோன்றும். பழங்கள் காய்ந்து கருப்பாக மாறும்.",
                "organic_treatment": ["போர்டோ கலவை தெளிக்கவும்."],
                "chemical_treatment": ["மைகுளோபுட்டானில் தெளிக்கவும்."],
                "prevention": ["கொடிகளுக்கு சூரிய ஒளி கிடைக்க கவாத்து செய்யவும்."]
            }
        }
    },

    "Grape___Esca_(Black_Measles)": {
        "crop": "Grapes",
        "disease": "Esca (Black Measles)",
        "pathogen": "Fungal Complex (Phaeomoniella)",
        "severity": "Severe / Chronic",
        "translations": {
            "en": {
                "crop_name": "Grapes",
                "disease_name": "Esca / Black Measles",
                "pathogen": "Fungal Complex (Phaeomoniella chlamydospora)",
                "symptoms": "Tiger-stripe leaf pattern: interveinal chlorosis and necrosis with green bands remaining along primary veins. Berries show speckled dark purple spots.",
                "organic_treatment": ["Apply Trichoderma wound sealant to fresh pruning wounds."],
                "chemical_treatment": ["Seal cuts with fungicidal paste containing Thiophanate-methyl."],
                "prevention": ["Prune late in dormant season and sterilize pruning tools."]
            },
            "hi": {
                "crop_name": "अंगूर (Grapes)",
                "disease_name": "एस्का / ब्लैक मीजल्स (Esca)",
                "pathogen": "कवक कॉम्प्लेक्स",
                "symptoms": "पत्तियों पर बाघ जैसी धारियां (Tiger-stripe), नसों के बीच पीलापन व सूखापन।",
                "organic_treatment": ["घावों पर ट्राइकोडर्मा का लेप लगाएं।"],
                "chemical_treatment": ["घावों पर फफूंदनाशक पेस्ट लगाएं।"],
                "prevention": ["छंटाई के औजारों को सैनिटाइज करें।"]
            },
            "kn": {
                "crop_name": "ದ್ರಾಕ್ಷಿ (Grapes)",
                "disease_name": "ಎಸ್ಕಾ / ಬ್ಲ್ಯಾಕ್ ಮೀಸಲ್ಸ್ (Esca)",
                "pathogen": "ಶಿಲೀಂಧ್ರ ಸಂಕೀರ್ಣ",
                "symptoms": "ಎಲೆಯ ನರಗಳ ನಡುವೆ ಹಳದಿ ಮತ್ತು ಕಂದು ಬಣ್ಣದ 'ಹುಲಿ ಪಟ್ಟೆ' ಮಾದರಿ.",
                "organic_treatment": ["ಟ್ರೈಕೋಡರ್ಮಾ ಲೇಪನ ಹಚ್ಚಿ."],
                "chemical_treatment": ["ಶಿಲೀಂಧ್ರನಾಶಕ ಪೇಸ್ಟ್ ಹಚ್ಚಿ."],
                "prevention": ["ಉಪಕರಣಗಳನ್ನು ಸ್ಯಾನಿಟೈಸ್ ಮಾಡಿ."]
            },
            "mr": {
                "crop_name": "द्राक्षे (Grapes)",
                "disease_name": "एस्का / ब्लॅक मिझल्स (Esca)",
                "pathogen": "बुरशी संकुल",
                "symptoms": "पानांवर वाघाच्या पट्ट्यांप्रमाणे (Tiger-stripe) शिरांच्या मध्ये पिवळे व तपकिरी पट्टे पडतात.",
                "organic_treatment": ["ट्रायकोडर्माचा लेप लावा."],
                "chemical_treatment": ["बुरशीनाशक पेस्ट लावून जखमा सील करा."],
                "prevention": ["हत्यारे निर्जंतुक करा."]
            },
            "ta": {
                "crop_name": "திராட்சை (Grapes)",
                "disease_name": "எஸ்கா / அம்மை நோய் (Esca)",
                "pathogen": "பூஞ்சை தொகுப்பு",
                "symptoms": "இலை நரம்புகளுக்கு இடையே புலி வரிகள் போன்ற மஞ்சள் காய்ந்த வரிகள் தோன்றும்.",
                "organic_treatment": ["டிரைக்கோடெர்மா பூசவும்."],
                "chemical_treatment": ["பூஞ்சாணக் கொல்லி பசை பூசவும்."],
                "prevention": ["கருவிகளை கிருமி நீக்கம் செய்யவும்."]
            }
        }
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grapes",
        "disease": "Leaf Blight",
        "pathogen": "Fungus (Pseudocercospora vitis)",
        "severity": "Moderate",
        "translations": {
            "en": {
                "crop_name": "Grapes",
                "disease_name": "Leaf Blight (Isariopsis)",
                "pathogen": "Fungus (Pseudocercospora vitis)",
                "symptoms": "Large, irregular, angular dark-brown to black necrotic patches on older leaves delimited by veins. Leaves turn yellow and drop prematurely.",
                "organic_treatment": ["Bordeaux mixture or copper soap sprays post-harvest or at first sign."],
                "chemical_treatment": ["Mancozeb, Chlorothalonil, or Azoxystrobin."],
                "prevention": ["Rake and destroy fallen leaves to reduce overwintering spores."]
            },
            "hi": {
                "crop_name": "अंगूर (Grapes)",
                "disease_name": "पत्ती झुलसा / इसारियोप्सिस (Leaf Blight)",
                "pathogen": "कवक (Pseudocercospora vitis)",
                "symptoms": "पुरानी पत्तियों पर नसों द्वारा सीमित बड़े, कोणीय काले-भूरे धब्बे। पत्तियां पीली पड़कर गिर जाती हैं।",
                "organic_treatment": ["बोर्डो मिश्रण या कॉपर सोप का छिड़काव करें।"],
                "chemical_treatment": ["मैन्कोजेब या क्लोरोथैलोनिल का स्प्रे करें।"],
                "prevention": ["गिरे हुए पत्तों को इकट्ठा कर नष्ट करें।"]
            },
            "kn": {
                "crop_name": "ದ್ರಾಕ್ಷಿ (Grapes)",
                "disease_name": "ಎಲೆ ಒಣಗು ರೋಗ (Leaf Blight)",
                "pathogen": "ಶಿಲೀಂಧ್ರ (Pseudocercospora vitis)",
                "symptoms": "ಎಲೆಗಳ ಮೇಲೆ ಕಪ್ಪು-ಕಂದು ಬಣ್ಣದ ದೊಡ್ಡ ಕಲೆಗಳು ಮತ್ತು ಎಲೆ ಉದುರುವಿಕೆ.",
                "organic_treatment": ["ಬೋರ್ಡೋ ಮಿಶ್ರಣ ಸಿಂಪಡಿಸಿ."],
                "chemical_treatment": ["ಮ್ಯಾಂಕೋಜೆಬ್ ಬಳಸಿ."],
                "prevention": ["ಉದುರಿದ ಎಲೆಗಳನ್ನು ನಾಶಪಡಿಸಿ."]
            },
            "mr": {
                "crop_name": "द्राक्षे (Grapes)",
                "disease_name": "पानावरील करपा (Leaf Blight)",
                "pathogen": "बुरशी (Pseudocercospora vitis)",
                "symptoms": "पानांवर शिरांनी मर्यादित मोठे, वेडेवाकडे काळे-तपकिरी डाग पडतात व पाने गळतात.",
                "organic_treatment": ["बोर्डो मिश्रण फवारा."],
                "chemical_treatment": ["मॅन्कोझेब किंवा अझोक्सीस्ट्रोबिन फवारा."],
                "prevention": ["गळलेली पाने गोळा करून नष्ट करा."]
            },
            "ta": {
                "crop_name": "திராட்சை (Grapes)",
                "disease_name": "இலை கருகல் நோய் (Leaf Blight)",
                "pathogen": "பூஞ்சை (Pseudocercospora vitis)",
                "symptoms": "இலைகளில் ஒழுங்கற்ற பெரிய கருப்பு கருகல் புள்ளிகள் தோன்றும்.",
                "organic_treatment": ["போர்டோ கலவை தெளிக்கவும்."],
                "chemical_treatment": ["மேன்கோசெப் தெளிக்கவும்."],
                "prevention": ["உதிர்ந்த இலைகளை அகற்றவும்."]
            }
        }
    },

    "Grape___healthy": {
        "crop": "Grapes",
        "disease": "Healthy Leaf",
        "pathogen": "None",
        "severity": "Healthy",
        "translations": {
            "en": {
                "crop_name": "Grapes",
                "disease_name": "Healthy Grape Leaf",
                "pathogen": "None",
                "symptoms": "Broad, vibrant green lobed leaves with clean margins and robust shoot growth, free from spots or discoloration.",
                "organic_treatment": ["Apply balanced seaweed extract and mycorrhizal compost."],
                "chemical_treatment": ["None required."],
                "prevention": ["Regular canopy shoot positioning for airflow."]
            },
            "hi": {
                "crop_name": "अंगूर (Grapes)",
                "disease_name": "स्वस्थ पत्ती (Healthy)",
                "pathogen": "कोई नहीं",
                "symptoms": "पत्ती गहरी हरी, चौड़ी और चमकदार है, कोई धब्बा नहीं है।",
                "organic_treatment": ["संतुलित जैविक खाद दें।"],
                "chemical_treatment": ["किसी दवा की आवश्यकता नहीं है।"],
                "prevention": ["बेलों का सही प्रबंधन करें।"]
            },
            "kn": {
                "crop_name": "ದ್ರಾಕ್ಷಿ (Grapes)",
                "disease_name": "ಆರೋಗ್ಯಕರ ಎಲೆ (Healthy)",
                "pathogen": "ಯಾವುದೂ ಇಲ್ಲ",
                "symptoms": "ಎಲೆಗಳು ಶುಭ್ರ ಹಸಿರಾಗಿದ್ದು ರೋಗಮುಕ್ತವಾಗಿವೆ.",
                "organic_treatment": ["ಸಾವಯವ ಗೊಬ್ಬರ ನೀಡಿ."],
                "chemical_treatment": ["ಯಾವುದೇ ಅಗತ್ಯವಿಲ್ಲ."],
                "prevention": ["ಸಮರ್ಪಕ ಹಂದರ ನಿರ್ವಹಣೆ ಮಾಡಿ."]
            },
            "mr": {
                "crop_name": "द्राक्षे (Grapes)",
                "disease_name": "निरोगी पान (Healthy)",
                "pathogen": "काही नाही",
                "symptoms": "पाने रुंद, हिरवीगार व निरोगी आहेत.",
                "organic_treatment": ["सेंद्रिय खते द्या."],
                "chemical_treatment": ["कोणत्याही औषधांची गरज नाही."],
                "prevention": ["वेलींचे योग्य व्यवस्थापन करा."]
            },
            "ta": {
                "crop_name": "திராட்சை (Grapes)",
                "disease_name": "ஆரோக்கியமான இலை (Healthy)",
                "pathogen": "எதுவும் இல்லை",
                "symptoms": "இலைகள் பசுமையாக ஆரோக்கியமாக உள்ளன.",
                "organic_treatment": ["இயற்கை உரங்கள் இடவும்."],
                "chemical_treatment": ["தேவையில்லை."],
                "prevention": ["சரியான பந்தல் பராமரிப்பு செய்யவும்."]
            }
        }
    }
}

CLASS_KEYS = list(DISEASE_CATALOG.keys())

def get_localized_disease_info(class_name: str, lang: str = "en") -> dict:
    """Retrieve disease info localized in 'en', 'hi', 'kn', 'mr', or 'ta'."""
    lang = lang if lang in ["en", "hi", "kn", "mr", "ta"] else "en"
    if class_name in DISEASE_CATALOG:
        entry = DISEASE_CATALOG[class_name]
        loc = entry["translations"].get(lang, entry["translations"]["en"])
        return {
            "class_key": class_name,
            "crop": entry["crop"],
            "disease": entry["disease"],
            "severity": entry["severity"],
            "localized_crop": loc["crop_name"],
            "localized_disease": loc["disease_name"],
            "pathogen": loc["pathogen"],
            "symptoms": loc["symptoms"],
            "organic_treatment": loc["organic_treatment"],
            "chemical_treatment": loc["chemical_treatment"],
            "prevention": loc["prevention"],
            "lang": lang
        }
    return {
        "class_key": class_name,
        "crop": "Unknown",
        "disease": class_name,
        "severity": "Moderate",
        "localized_crop": class_name,
        "localized_disease": class_name,
        "pathogen": "Unknown",
        "symptoms": "No detailed symptoms recorded.",
        "organic_treatment": ["Consult local agricultural officer."],
        "chemical_treatment": ["Apply protective broad-spectrum fungicide."],
        "prevention": ["Crop rotation and balanced irrigation."],
        "lang": lang
    }
