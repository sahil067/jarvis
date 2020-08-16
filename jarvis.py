import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)



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

    speak("I am Jarvis Sir, Please tell me how may i help you")
        
if __name__ == "__main__":
    speak("twinkle ak achi larki hai")

def takeCommand():
    # It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause.threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, Language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)

            print("Say that again Please...")
            return "None"
        return query
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.startls()
        server.login('ramugoswami027@gmail.com', 'your-password')
        server.sendmail('ramugoswami027@gmail.com', to, content)
        server.close()

        

    if __name__ == "__main__":
            wishMe()
            while True:
               query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summery(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                    webbrowser.open("google.com")

            elif 'open salesforce' in query:
                    webbrowser.open("salesforce.com")

            elif 'open facebook' in query:
                    webbrowser.open("facebook.com")

            elif 'open stackoverFlow' in query:
                    webbrowser.open("stackoverFlow.com")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\MY_PC\\Downloads\\song\\old song'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                strTime = datetime.datetime.now().strFtime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\MY_PC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'email to harry' in query:
               try:
                   speak("What should I say?")
                   content = takeCommand()
                   to = "ramugoswami675@gmail.com"
                   sendEmail(to, content)
                   speak Exception as e:
                   print(e)
                   speak("sorry")