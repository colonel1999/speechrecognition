import speech_recognition as sr
from datetime import datetime

#Lines to added to the file in one go
lines=[]
filename=str(datetime.now())+".txt"
def writeToFile(text):
    lines.append(text)
    file1 = open(filename,"a") 
    file1.writelines(lines)     
    
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        writeToFile(text)
        print("Log saved at : {}".format(filename))

    except:
        print("Sorry could not recognize what you said")