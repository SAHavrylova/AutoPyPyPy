from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
import re  # Import the regular expression module

# Введіть ваш словник тут (слово англійською як ключ, переклад українською як значення)
dictionary = {
    "to be stung by a wasp": "бути вжаленим осою",
    "to have an allergic reactionc": "мати алергічну реакцію",
    "to have bad sunburn": "мати сильний сонячний опік",
    "to choke": "задихатися, вдавитися",
    "to hit on the back": "бити по спині",
    "to lean backward": "нахилитися назад",
    "to lie on the side": "лежати на боці",
    "to put on a burn": "покласти на опік",
    "plastic wrap": "харчова плівка",
    "to bleed badly": "сильно кровоточити",
    "a wound": "рана, поранення",
    "to treat a nosebleed": "лікувати носову кровотечу",
    "to lean forward/backward": "нахилятися вперед/назад",
    "to pinch a nose": "затиснути ніс",
    "to collapse on the ground": "впасти на землю",
    "a straight position": "пряме положення",
    "to prevent uncessessary movement": "запобігти непотрібним рухам",
    "to put a bandage": "накласти пов'язку",
    "shoulder blades": "лопатки",
    "to clear the blockage": "усунути засмічення",
    "to reduce swelling and scarring": "зменшити набряк та рубці",
    "to prevent infection": "запобігти зараженню",
    "clean cloth": "чиста тканина",
    "to tilt forward/backward": "нахилятися вперед/назад",
    "itchy": "сверблячий",
    "to bump a head": "вдаритися головою",
    "to be out cold": "знепритомніти",
    "to faint": "знепритомніти",
    "to black out": "знепритомніти",
    "to come down with": "захворіти на",
    "to strain": "розтягнути",
    "to limp": "кульгати",
    "a spine": "хребет",
    "spinal injury": "пошкодження хребта",
    "severely restricted mobility": "суворе обмеження рухливості",
    "kidney failure": "ниркова недостатність",
    "liver failure": "печінкова недостатність",
    "a transplant": "трансплантація",
    "an organ donor": "донор органів",
    "to bash": "сильно забити",
    "a head scan": "сканування голови",
    "to be black and blue": "бути в синцях",
    "a bruise": "синець, забите місце",
    "to develop arthritis": "розвивати артрит",
    "a joint": "суглоб",
    "physical pain": "фізичний біль",
    "sharp pain": "гострий біль",
    "to concede defeat": "визнати поразку",
# Додайте інші слова і переклади
}

# Ініціалізуємо перекладача
translator = Translator()

# Створюємо порожній аудіофайл для об'єднання
combined_audio = AudioSegment.empty()

# Define a function to clean the filename
def clean_filename(filename):
    return re.sub(r'[^\w\s]', '_', filename)

for english_word, ukrainian_translation in dictionary.items():
    # Озвучуємо англійське слово
    english_audio = gTTS(english_word, lang="en", slow=False)
    
    # Перекладаємо український переклад
    translated_text = ukrainian_translation
    
    # Озвучуємо український переклад
    ukrainian_audio = gTTS(translated_text, lang="uk", slow=False)
    
    # Clean the filenames before saving
    english_word_cleaned = clean_filename(english_word)
    translated_text_cleaned = clean_filename(translated_text)
    
    # Save the English and Ukrainian audio with cleaned filenames
    english_audio.save(f"{english_word_cleaned}.mp3")
    ukrainian_audio.save(f"{translated_text_cleaned}.mp3")
    
    # Load the cleaned audio files
    english_audio_segment = AudioSegment.from_mp3(f"{english_word_cleaned}.mp3")
    ukrainian_audio_segment = AudioSegment.from_mp3(f"{translated_text_cleaned}.mp3")
    
    # Додаємо англійське слово та український переклад у порожній аудіофайл
    combined_audio += english_audio_segment + ukrainian_audio_segment

# Зберігаємо об'єднане аудіо в файл
combined_audio.export("combined_audio.mp3", format="mp3")

print("Аудіофайл 'combined_audio.mp3' створено.")
