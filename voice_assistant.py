import pyttsx3
import speech_recognition as sr
from newspaper import Article

# Инициализация для синтеза речи
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Функция для парсинга статьи
def parse_article(url):
    article = Article(url, language="ru")
    article.download()
    article.parse()
    return article

# Инициализация для распознавания речи
def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Ввод голосовой команды...")
        audio = r.listen(source, timeout=5)  # Установка времени записи на 5 секунд
        try:
            text = r.recognize_google(audio, language="ru-RU")
            return text.lower()  # Возвращаем распознанный текст в нижнем регистре
        except sr.UnknownValueError:
            return ""  # Если не удалось распознать речь, возвращаем пустую строку

speak("Привет! Я ваш ассистент. Чем могу помочь?")

while True:
    user_input = recognize_speech()  # Получаем голосовую команду

    if user_input == "привет":
        speak("Привет! Как дела?")
    elif user_input == "пока":
        speak("До свидания!")
        break
    elif user_input == "расписание":
        speak("Понедельник, пара номер 1 физкультура, пара номер 2 математика")
    elif user_input == "мероприятия":
        article_url = "https://www.iubip.ru/news/282/"  # URL для получения статьи
        article = parse_article(article_url)

        title = article.title
        text = article.text[:500]

        events_text = f"Заголовок: {title}\nТекст статьи: {text}"
        speak(events_text)  # Озвучиваем текст статьи
    else:
        speak("Извините, я не понимаю. Попробуйте еще раз.")