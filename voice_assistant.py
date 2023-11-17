# pip install PyAudio
# pip install SpeechRecognition
# pip install pyttsx3

import pyttsx3
import speech_recognition as sr

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

while True:
    user_input = recognize_speech()  # Получаем голосовую команду
    if user_input == "привет":
        speak("Привет! Как дела?")
    elif user_input == "пока":
        speak("До свидания!")
        break
    elif user_input == "расписание":
        speak("Понедельник, пара номер 1 физкультура, пара номер 2 математика")
    else:
        speak("Извините, я не понимаю. Попробуйте еще раз.")
