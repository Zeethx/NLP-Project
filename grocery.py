import speech_recognition
import pyttsx3
import pyaudio
import tkinter as tk
import webbrowser as wb

def search(data):
    print(f"Searching for {data} on walmart")
    wb.open("https://www.walmart.ca/search?q="+data)

def grocery_intro():
    fstr = "Grocery List Created!\n"
    fstr += "You can use the following commands\n1) Add [item] to the grocery list\n2) Remove [item] from the list\n3) Show my list\n4) Search [item] on walmart(should be in your list)\n5) (Exit/ I'm done/ That's it) to stop navigating\n"

    return fstr

def grocery_list():
    recognizer = speech_recognition.Recognizer()
    exit_phrases = ["exit", "i'm done", "bye", "that's it"]
    print(grocery_intro())   
    grocerylist = []
    while True:

        try:
            #recording audio
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)

                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                #recorded msg forwarding
                print(f"Recorded:{text}")
                if text in exit_phrases:
                    break
                
                if("add") in text:
                    textbreak = text.split(" ")
                    usevalue = textbreak[textbreak.index("add")+1]
                    numbervalues = ["one", "two", "three", "four", "five", "to"]
                    if usevalue in numbervalues or usevalue.isdigit():                           
                        usevalue = textbreak.index("add") + 2
                        grocerylist.append(textbreak[usevalue])
                        print(f"Added: {textbreak[usevalue]}")
                    else:
                        usevalue = textbreak.index("add") + 1
                        grocerylist.append(textbreak[usevalue])
                        print(f"Added: {textbreak[usevalue]}")

                #remove item from list
                if("remove") in text:
                    try:
                        textbreak = text.split(' ')
                        usevalue = textbreak[textbreak.index("remove")+1]
                        if(usevalue in grocerylist):
                            remitem = grocerylist[grocerylist.index(usevalue)]
                            print(f"Removed:{remitem}")
                            del grocerylist[grocerylist.index(usevalue)]
                    except:
                        print("Item not in the list")
                        showlist(grocerylist)
                        pass
                #show the list to user
                if("show") in text:
                    print(f"\n-----Grocery List-----\n{showlist(grocerylist)}")

                #search for item on walmart
                if ("search") in text:
                    textbreak = text.split(" ")
                    try:
                        usevalue = textbreak[textbreak.index("search") + 1]
                        if usevalue in grocerylist:
                            search(usevalue)
                        else:
                            print("Try saying 'search [item] on walmart'(item should be in your grocery list)\n")                        
                    except IndexError:
                        print("Try saying 'search [item] on walmart'(item should be in your grocery list)\n")

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue

def showlist(grocery_list):
    fstr = ""
    i=1
    for item in grocery_list:
        fstr += f"{i}){item}\n"
        i+=1
    return fstr
grocery_list()
