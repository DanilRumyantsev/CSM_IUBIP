# pip install PyAudio
# pip install SpeechRecognition

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

sr.LANGUAGE = "ru-RU"

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("Ввод голосовой команды...")
    audio = r.listen(source, timeout=5)  # Устанавливаем время записи 5 секунд

text = r.recognize_google(audio, language="ru-RU")

print(f"Вы сказали: {text}")