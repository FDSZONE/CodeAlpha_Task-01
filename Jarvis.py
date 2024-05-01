import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
      with sr.Microphone() as source:
        print("listening Sir ....")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()

        if "Jarvis" in command:
            command = command.replace("Jarvis", "")
            print(command)

    except:
        pass

    return command

def run_jarvis():
   command = take_command()
   print(command)
   if "play" in command:
      song = command.replace("play", "")
      talk ("playing Sir" + song)
      pywhatkit.playonyt(song)

   elif "time" in command:
      time = datetime.datetime.now().strftime("%H:%M %P")
      talk("current time is " + time)
   elif "who" in command:
      person = command.replace("So", "")
      info = wikipedia.summary(person, 1)
      print(info)
      talk(info)

   elif "date" in command:
      talk("Sorry, I have a headache")

   elif "who are you" in command:
      talk("I am in a relationship with WIFI")  

   elif "joke" in command:
      talk(pyjokes.get_joke())    

   else:
        pywhatkit.search(command)
  

while True:
  run_jarvis()
