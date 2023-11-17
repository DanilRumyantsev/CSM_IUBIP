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

    if user_input == "привет" or user_input == "хай" or user_input == "hello" :
        speak("Привет! Как дела?")
    elif user_input == "пока" or user_input == "стоп" or user_input == "хватит" :
        speak("До свидания!")
        break
    elif user_input == "О университете" or user_input == "университет" or user_input == "иубип":
        speak("Частное образовательное учреждение высшего образования ЮЖНЫЙ УНИВЕРСИТЕТ Институт Управления, Бизнеса и Права был основан в 1991 году и является первым негосударственным вузом современной России. На сегодняшний день в Университете работает более 500 преподавателей, и обучается около 5 000 студентов. За время работы университетом подготовлено более 20 000 квалифицированных специалистов. ЮЖНЫЙ УНИВЕРСИТЕТ ИУБиП стал одним из первых вузов на юге страны, получившим от Федеральной службы по надзору в сфере образования и науки бессрочную лицензию на право образовательной деятельности. Программы бакалавриата и магистратуры университета прошли государственную аккредитацию. По итогам обучения студентам вручаются государственные дипломы Российской Федерации, подтверждающие качество подготовки выпускников. В соответствии с действующим законодательством предоставляется отсрочка от службы в Вооруженных силах РФ. Университет вошел в число лучших негосударственных вузов страны, которым на конкурсной основе впервые в истории современного российского высшего образования были выделены бюджетные средства для бесплатного обучения студентов")
    elif user_input == "мероприятия" or user_input == "новости":
        article_url = "https://www.iubip.ru/news/282/"  # URL для получения статьи
        article = parse_article(article_url)

        title = article.title
        text = article.text[:500]

        events_text = f"Заголовок: {title}\nТекст статьи: {text}"
        speak(events_text)  # Озвучиваем текст статьи
    else:
        speak("Извините, я не понимаю. Попробуйте еще раз.")