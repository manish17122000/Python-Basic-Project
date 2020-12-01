import pyttsx3 #have to install
import datetime
import speech_recognition as sr  #have to install
import wikipedia as wp  #have to install
import webbrowser as wb  #have to install
import os
"""Pyaudio can create a problem so go to Unofficial windows binary for python with
 https://www.lfd.uci.edu/~gohlke/pythonlibs/   link and download pyaudio and also install it in kernal"""

"""While install library the problem can be occur that file is missing at this time 
go to conda lib>> check downloaded file>> change the name accordingly either in code or in Library"""

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:
        speak("Manish you should sleep other wise mamma will wish you, get well soon")   #Funtalk
    elif hour>=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    elif hour>=17 and hour<22:
        speak("Good evening")
    elif hour>=22 and hour<24:
        speak("Good Night")
    speak("Hello manish, i'm your Assistent, How may i help you...")
    
#Takecommand function is use to change audio in text    
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query= r. recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)        
        print("say that again please")
        return "None"
    return query
    
    
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        
        #this is wkipedia search        
        if 'wikipedia' in query:
            speak("Searching in WIKIpedia")
            query= query.replace("wikipedia", "")
            results = wp.summary(query, sentences =2)
            speak("According to Wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            wb.open("youtube.com")
        
        elif 'open google' in query:
           wb.open("google.com")
           
        elif 'open hackerrank' in query:
           wb.open("hackerrank.com")
        
        elif 'play music' in query:
           music_dir='E:\\music'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir, songs[0]))
           
        elif 'the time' in query:
           strTime= datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The Time Is,  {strTime}")
           