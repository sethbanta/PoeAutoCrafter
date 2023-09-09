#Author Seth Banta
import pyautogui
import tkinter as tk

clipboardData = ''
modArray = ["deez"]
modArray.append("Dangerous") #ignore on regal
modArray.append("Powerful")
modArray.append("of the Bear") #ignore on regal
modArray.append("of the Fox")
modArray.append("of the Prodigy")
modArray.append("of the Kaleidoscope")
modArray.append("of Mastery")
modArray.append("of Eviction")
modArray.append("Sanguine")


alterationCount = 0
altInput = ''
clippy = tk.Tk()
clippy.withdraw()

#Function used to perform transmuting an item
def transmute():
    print(f'Transmuted')
    #pick up transmute, 100,100 will need to change to the location of wherever transmutes are 
    #in your resolution
    pyautogui.moveTo(55,268,duration=0.5)
    pyautogui.rightClick()
    pyautogui.PAUSE
    pyautogui.moveTo(339,451,duration=0.4)
    pyautogui.leftClick()
    #copy to clipboard and see if the item somehow hit what we want
    pyautogui.hotkey('alt','ctrl','c')
    pyautogui.PAUSE
    clipboardData = clippy.clipboard_get()
    deez = clipboardData.split('--------')[2].split('\"')
    #grab data from clipboard
    #split or truncate so that we find the mods on the item
    #search in an array if the mods that are on the item are what we want
    #if its what we want move to regal, if its not, alt
    for str in deez:
        if(modArray.count(str)):
            regal()
        else:
            alteration()

#Function used to perform alting an item
def alteration():
    global alterationCount
    while (alterationCount > 0):
        print(f'Alted')
        #pick up alt
        pyautogui.moveTo(118,267, duration=0.1)
        pyautogui.rightClick()
        #use alt
        pyautogui.moveTo(339,451,duration=0.1)
        pyautogui.leftClick()
        alterationCount = alterationCount - 1
        #grab item data
        pyautogui.hotkey('alt','ctrl','c')
        pyautogui.PAUSE
        clipboardData = clippy.clipboard_get()
        deez = clipboardData.split('--------')[2].split('\"')
        deezLen = len(deez)
        #if it matches, regal, if it doesnt, do nothing and keep rolling
        for str in deez:         
            if(modArray.count(str)):
                foundMod = str
                #at this point, the item has at least ONE desired mod, we need to check if we should augment it, or regal
                if(deezLen == 3):
                    #augment
                    print(f'augmented')
                    pyautogui.moveTo(233,327,duration=0.25)
                    pyautogui.rightClick()
                    pyautogui.moveTo(339,451,duration=0.25)
                    pyautogui.leftClick()
                #check if it needs to be regaled or keep alting
                pyautogui.hotkey('alt','ctrl','c')
                clipboardData = clippy.clipboard_get()
                deezTwo = clipboardData.split('--------')[2].split('\"')
                for str in deezTwo:
                    if(modArray.count(str) and str != foundMod):
                        regal()
    print(f'Reached alteration count, exiting')
    exit()
        
    
    

#Function used to perform regaling an item
def regal():
    print(f'Regaled')
    #grab regal
    pyautogui.moveTo(445,264,duration=0.5)
    pyautogui.rightClick()
    pyautogui.PAUSE
    #use regal
    pyautogui.moveTo(339,451,duration=0.4)
    pyautogui.leftClick()
    pyautogui.PAUSE
    #check mods
    pyautogui.hotkey('alt','ctrl','c')
    pyautogui.PAUSE
    clipboardData = clippy.clipboard_get()
    deez = clipboardData.split('--------')[2].split('\"')
    desiredMods = 0
    for str in deez:
        if(modArray.count(str) and (str != "Dangerous" or str != "of the Bear")):
            desiredMods = desiredMods + 1
    if(desiredMods == 3):
        exalt()
    else:
        scour()
                
#Function used to perform scouring an item
def scour():
    print(f'Scoured')
    #pick up scour
    pyautogui.moveTo(436,505,duration=0.3)
    pyautogui.rightClick()
    pyautogui.PAUSE
    #use scour
    pyautogui.moveTo(339,451,duration=0.4)
    pyautogui.leftClick()
    pyautogui.PAUSE
    #back to transmuting
    transmute()
    
#Function used to perform exalting an item
def exalt():
    print(f'Exalted')
    #pick up exalt
    pyautogui.moveTo(303,264,duration=0.5)
    pyautogui.rightClick()
    pyautogui.PAUSE
    #use exalt
    pyautogui.moveTo(339,451,duration=0.4)
    pyautogui.leftClick()
    pyautogui.PAUSE
    #at this point user will manually check what was slammed and get asked if they want to scour or not
    question = input('scour? (y/n) ')
    match question:
        case "y":
            scour()
        case _:
            print(f'Exiting')
            exit()

print('Please have stash open on currency tab with item in the showcase slot')
altInput = input('How many alterations would you like to use? ')
alterationCount = int(altInput)
ready = input('Ready to begin? (y/n) ')
match ready:
        case "y":
            print(f'Starting')
            transmute()
        case _:
            print(f'Exiting')