import os
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import smtplib 

# text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1])
engine.setProperty('voice', voices[0].id)


def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good evening!")

    speak("I am Paso Sir, please tell me how can I help you")

def takeCommand():
    # take audio as a input and print it OR speech to text 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 300   #frequency of user sound 
        r.pause_threshold = 1      #end time after listening
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('priyanshujangir08@gmail.com','9414664064')
    server.sendmail('priyanshujangir08@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    wishMe() 
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open Youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

#        elif 'play music' in query:
#            webbrowser.open("youtube.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)
            speak(f"Sir,The time is{strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = "primer20paso@gmail.com"
                sendEmail(to,content)
                speak('Email has been send!')
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send ")
                print("Sorry sir, I am not able to send ")

        elif 'quit' or 'bye paso' or 'close the program' in query:
            break 

speak("bye Sir")
