import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello I am Took Took Developed by Vighnesh and how can I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")  

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vighneshdeepsharan2002@gmail.com','vds@3210')
    server.sendmail('vighneshdeepsharan2002@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
   # while True:
if 1:
        query = takeCommand().lower()
      

if 'wikipedia' in query:
    speak("Searching Wikipedia...")
    query = query.replace('wikipedia', "")
    results = wikipedia.summary(query, sentences=4)
    speak("According to wikipedia")
    print(results)
    speak(results)

elif 'youtube' in query:
    webbrowser.open("youtube.com")

elif 'google' in query:
    webbrowser.open("google.com")

elif 'stackoverflow' in query:
    webbrowser.open("stackoverflow.com")

elif 'github' in query:
    webbrowser.open("github.com")

elif 'music'  in query:
    music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
    songs = os.listdir(music_dir)
    
    os.startfile(os.path.join(music_dir, songs[0]))

elif 'time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

elif 'code' in query:
    codepath = "C:\\Users\\Vighnesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)

elif 'chrome' in query:
    codepath = "D:\\Web Projects\\chrome\\index.html"
    os.startfile(codepath)

elif 'mail' in query:
    try:
        speak("What should I say?")
        content = takeCommand()
        to = "vighneshdeepsharan2002@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
    except Exception as e:
            print(e)
            speak("Sorry Vighnesh bhai ye humse na hopayega!!")

elif 'answer' in query:
    speak("Sir do you want your system to be shutdown?")
    shutdown = takeCommand()
if shutdown == 'no':
    speak("Sir Jarvis is not shutting down!!!")
    exit()


else:
    os.system("shutdown /s /t 1")
    

      
	




   
    
         
        
    
