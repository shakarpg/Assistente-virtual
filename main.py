import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os

# Inicializa o motor de voz
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Desculpe, não entendi.")
        return ""
    except sr.RequestError:
        speak("Erro na conexão com o serviço de reconhecimento.")
        return ""

def execute_command(command):
    if "youtube" in command:
        speak("Abrindo o YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "wikipedia" in command:
        speak("O que você quer pesquisar na Wikipedia?")
        query = listen()
        if query:
            wikipedia.set_lang("pt")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
    elif "farmácia" in command:
        speak("Abrindo o Google Maps para farmácias próximas")
        webbrowser.open("https://www.google.com/maps/search/farmácia")
    elif "sair" in command:
        speak("Encerrando o assistente. Até logo!")
        exit()
    else:
        speak("Comando não reconhecido.")

if __name__ == "__main__":
    speak("Olá! Sou seu assistente virtual. Como posso ajudar?")
    while True:
        cmd = listen()
        if cmd:
            execute_command(cmd)
