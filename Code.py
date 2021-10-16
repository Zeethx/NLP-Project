import speech_recognition
import pyttsx3
import pyaudio
import tkinter as tk
import webbrowser as wb

window = tk.Tk()
window.title()

window.configure()
#window.mainloop()

def search(data):
    speak(f"searching for {data} on walmart")
    wb.open("https://www.walmart.ca/search?q="+data)

def grocery_list():
    recognizer = speech_recognition.Recognizer()
    exit_phrases = ["exit", "i'm done", "bye", "that's it"]
    exit_text = ""
    for e in exit_phrases:
        if(e != exit_phrases[-1]):
            exit_text += e + "/ "
        else:
            exit_text += e
    print("Say any of the following to exit( " + exit_text + " )")
    while True:
        
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.1)

                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                for _ in range(50): time.sleep(0.1)
                #recorded msg forwarding
                if text in exit_phrases:
                    break
                if "create" in text:
                    grocery_list = []
                    print("Grocery List Created!\n")
                try:
                    if("add" or "include") in text:
                        textbreak = text.split(" ")
                        print(text)
                        if (textbreak[textbreak.index("add")+1] in (["one", "two", "three", "to"]) or range(100)):                            
                            usevalue = textbreak.index("add") + 2
                        else:
                            usevalue = textbreak.index("add") + 1
                        grocery_list.append(textbreak[usevalue])
                        print("Added: "+ textbreak[usevalue])
                        if ("search" in text) and :
                            search(textbreak[usevalue])

                except:
                    print("Create a grocery list first!")
                if("show") in text:
                    showlist()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue

def showlist(grocery_list):
    fstr = ""
    for e in grocery_list:
        fstr+=e + " "
    return fstr
    

grocery_list()


