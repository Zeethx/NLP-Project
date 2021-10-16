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
    print(f"searching for {data} on walmart")
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
    print("Grocery List Created!\n")
    grocerylist = []
    while True:
        
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)

                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                #recorded msg forwarding
                print(f"Recorded:{text}")
                if text in exit_phrases:
                    break
                
                if("add" or "include") in text:
                    textbreak = text.split(" ")
                    usevalue = textbreak[textbreak.index("add")+1]
                    if (usevalue in (["one", "two", "three", "to"]) or range(100)) and len(textbreak)>2:                            
                        usevalue = textbreak.index("add") + 2
                        grocerylist.append(textbreak[usevalue])
                        print(f"Added: {textbreak[usevalue]}")
                    else:
                        usevalue = textbreak.index("add") + 1
                        grocerylist.append(textbreak[usevalue])
                        print(f"Added: {textbreak[usevalue]}")

                #remove item from list

                if("show") in text:
                    print(f"Grocery List:{showlist(grocerylist)}")

                if ("search") in text:
                    textbreak = text.split(" ")
                    usevalue = textbreak[textbreak.index("search") + 1]
                    if usevalue in grocerylist:
                        search(usevalue)
                    else:
                        print("Try saying 'search [item] on walmart'(item should in your grocery list)")
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue

def showlist(grocery_list):

    return grocery_list
    

grocery_list()
