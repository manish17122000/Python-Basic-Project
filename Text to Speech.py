import pyttsx3


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    savefile =open('C:\\Users\\Dell\\Desktop\\Python project\\file.txt', 'r')
    speak(savefile.read())
    savefile.close()

    
if __name__ == "__main__":
        takeCommand()