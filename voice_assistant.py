# pip install PyAudio
# pip install SpeechRecognition
# pip install pyttsx3

import pyttsx3
import speech_recognition as sr
from newspaper import Article
import requests

r = sr.Recognizer()
mic = sr.Microphone()

sr.LANGUAGE = "ru-RU"

# Функция для распознавания речи
def recognize_speech():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Ввод голосовой команды...")
        audio = r.listen(source, timeout=2)  # Установка времени записи на 2 секунды
        try:
            text = r.recognize_google(audio, language="ru-RU")
            return text.lower()  # Возвращаем распознанный текст в нижнем регистре
        except sr.UnknownValueError:
            return ""  # Если не удалось распознать речь, возвращаем пустую строку

# Инициализация движка для синтеза речи
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Привет! Я ваш ассистент. Чем могу помочь?")

# Функция для парсинга статьи
def parse_article(url):
    try:
        article = Article(url, language="ru")
        article.download()
        article.parse()
        return article
    except requests.RequestException as e:
        print("Новости закончились. Возвращайтесь позже.")
        return None

article_url = "https://www.iubip.ru/news/282/"

def get_events_text(article_url):
    events_text = ""

    while True:
        article = parse_article(article_url)

        if article is not None:
            title = article.title
            text = article.text[:500]
            
            events_text += f"Заголовок: {title}\nТекст статьи: {text}\n\n"

            # Generate the URL for the next article
            article_number = int(article_url.split("/")[-2])
            next_article_number = article_number + 1
            next_article_url = f"https://www.iubip.ru/news/{next_article_number}/"
            article_url = next_article_url
        else:
            break

    return events_text

while True:
    user_input = recognize_speech()  # Get voice command

    if user_input == "привет":
        speak("Привет! Как дела?")
    elif user_input == "пока":
        speak("До свидания!")
        break
    elif user_input == "расписание":
        speak("Понедельник, пара номер 1 физкультура, пара номер 2 математика")
    elif user_input == "мероприятия":
        events_text = get_events_text(article_url)  # Perform article parsing
        speak(events_text)  # Speak out the obtained text
    else:
        speak("Извините, я не понимаю. Попробуйте еще раз.")