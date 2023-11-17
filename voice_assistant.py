import pyttsx3
import speech_recognition as sr
from newspaper import Article
import csv

filename = 'classmates.csv'  # Укажите имя вашего CSV-файла

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
  value = data[0][0]
   value2 = data[0][1]
    value3 = data[0][2]
     value4 = data[0][3]
      value5 = data[0][4]
       value6 = data[0][5]
        value7 = data[0][6]
         value8 = data[0][7]
          value9 = data[0][8]
           value10 = data[0][9]

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

    if user_input == "привет" or user_input == "хай" or user_input == "hello" :
        speak(value)
    elif user_input == "пока" or user_input == "стоп" or user_input == "хватит" :
        speak(value2)
    elif user_input == "музло":
        speak(value3)
    elif user_input == "Бакалавриат" :
        speak(value4)
    elif user_input == "Магистратура":
        speak(value5)
    elif user_input == "Аспирантура" :
        speak(value6)
    elif user_input == "Дополнительное профессиональное образование" or user_input == "Дополнительное образование" or user_input == "Доп образование" :
        speak(value7)
    elif user_input == "Среднее профессиональное образование" or user_input == "Среднее образование" :
        speak(value8)
    elif user_input == "услуги" or user_input == "услуги университета" or user_input == "перечень услуг" :
        speak(value9)
        break
    elif user_input == "О университете" or user_input == "университет" or user_input == "иубип":
        speak(value10)
    elif user_input == "мероприятия" or user_input == "новости":
        article_url = "https://www.iubip.ru/news/282/"  # URL для получения статьи
        article = parse_article(article_url)

        title = article.title
        text = article.text[:500]

        events_text = f"Заголовок: {title}\nТекст статьи: {text}"
        speak(events_text)  # Озвучиваем текст статьи
    else:
        speak("Извините, я не понимаю. Попробуйте еще раз.")