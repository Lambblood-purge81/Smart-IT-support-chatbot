import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry, could not understand your voice."
