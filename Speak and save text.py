import speech_recognition as sr

def takeCommand():
    savefile=open('file.txt', 'a')
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query= r. recognize_google(audio, language='en-in')     
        savefile.write(query)
        savefile.write(" ")
        savefile.close()
    
    except Exception as e:
        print(e)        
        print("say that again please")
        return "None"
    return query
        
if __name__ == "__main__":
        query=takeCommand().lower()
        