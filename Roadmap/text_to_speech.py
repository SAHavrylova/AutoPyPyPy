from gtts import gTTS
from googletrans import Translator
from pydub import AudioSegment
import re  # Import the regular expression module

# Введіть ваш словник тут (слово англійською як ключ, переклад українською як значення)
dictionary = {
    "dispute": "суперечка",
    "domestic": "домашній",
    "mediator": "посередник",
    "tension": "напруга",
    "to build up": "нарощувати, створювати",
    "clear the air": "внести ясність, розрядити атмосферу",
    "to be on speaking terms with somebody": "бути в гарних відносинах",
    "awkward": "незграбний, незручний",
    "to make up": "надолужувати відносини",
    "to side with": "стати на бік",
    "to resolve a dispute": "вирішити спір",
    "to escalate": "загострювати",
    "ongoing": "безперервний",
    "to come to blows over smth": "вступати в бійку",
    "to quarrel": "сваритися",
    "to confront": "суперечити, нападати",
    "kick someone out": "виганяти",
    "to end up in": "закінчитись чимось",
    "a strike": "страйк, забастовка",
    "willing": "готовий",
    "be willing to": "бути охочим",
    "to compromise": "йти на компроміс",
    "to give up": "здаватися, кидати",
    "to get out of control": "вийти з-під контролю",
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
