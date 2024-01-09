#Author Seth Banta
import pyautogui
import tkinter as tk

transX, transY, altX, altY, augX, augY, regX, regY, scourX, scourY, exaltX, exaltY, showcaseX, showcaseY = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
clipboardData = ''
modArray = ["deez"]
modArray.append("Powerful")
modArray.append("Glowing")
modArray.append("Meteor")
modArray.append("Prodigy")


alterationCount = 0
altInput = ''
clippy = tk.Tk()
clippy.withdraw()

#Function used to perform transmuting an item
def transmute():
    print(f'Transmuted')
    #pick up transmute, 100,100 will need to change to the location of wherever transmutes are 
    #in your resolution
    pyautogui.moveTo(transX,transY,duration=0.17)
    pyautogui.rightClick()
    pyautogui.PAUSE
    pyautogui.moveTo(showcaseX,showcaseY,duration=0.17)
    pyautogui.leftClick()
    #copy to clipboard and see if the item somehow hit what we want
    pyautogui.hotkey('alt','ctrl','c')
    pyautogui.PAUSE
    deez = clippy.clipboard_get().split()
    #grab data from clipboard
    #split or truncate so that we find the mods on the item
    #search in an array if the mods that are on the item are what we want
    #if its what we want move to regal, if its not, alt
    for str in deez:
        str = str.strip('\"') 
        if(modArray.count(str)):
            regal()
    alteration()

#Function used to perform alting an item
def alteration():
    global alterationCount
    #pick up alt
    pyautogui.moveTo(altX,altY, duration=0.17)
    pyautogui.rightClick()
    while (alterationCount > 0):
        print(f'Alted')
        #use alt
        pyautogui.keyDown('shift')
        pyautogui.moveTo(showcaseX,showcaseY,duration=0.17)
        pyautogui.leftClick()
        alterationCount = alterationCount - 1
        #grab item data
        pyautogui.hotkey('alt','ctrl','c')
        pyautogui.PAUSE
        clipboardData = clippy.clipboard_get().split()
        #deez = clipboardData.split('--------')[3].split('\"')
        #print(f'{deez}')
        #deezLen = len(deez)
        #if it matches, regal, if it doesnt, do nothing and keep rolling
        for str in clipboardData:  
            str = str.strip('\"')       
            if(modArray.count(str)):
                foundMod = str
                pyautogui.keyUp('shift')
                aug = 1
                #at this point, the item has at least ONE desired mod, we need to check if we should augment it, or regal
                if(aug == 1):
                    #augment
                    print(f'augmented')
                    pyautogui.moveTo(augX,augY,duration=0.17)
                    pyautogui.rightClick()
                    pyautogui.moveTo(showcaseX,showcaseY,duration=0.17)
                    pyautogui.leftClick()
                    #check if it needs to be regaled or keep alting
                    pyautogui.hotkey('alt','ctrl','c')
                    clipboardData = clippy.clipboard_get().split()
                    for str in clipboardData:
                        str = str.strip('\"')
                        if(modArray.count(str) and str != foundMod):
                            aug = 0
                            regal()
                    aug = 0
                    #pick up alt
                    pyautogui.moveTo(altX,altY, duration=0.17)
                    pyautogui.rightClick()
    pyautogui.keyUp('shift')
    print(f'Reached alteration count, exiting')
    exit()
        
    
    

#Function used to perform regaling an item
def regal():
    print(f'Regaled')
    #grab regal
    pyautogui.moveTo(regX,regY,duration=0.17)
    pyautogui.rightClick()
    pyautogui.PAUSE
    #use regal
    pyautogui.moveTo(showcaseX,showcaseY,duration=0.17)
    pyautogui.leftClick()
    pyautogui.PAUSE
    #check mods
    pyautogui.hotkey('alt','ctrl','c')
    pyautogui.PAUSE
    deez = clippy.clipboard_get().split()
    desiredMods = 0
    for str in deez:
        str = str.strip('\"') 
        if(modArray.count(str)):
            desiredMods = desiredMods + 1
    if(desiredMods == 3):
        exalt()
    else:
        scour()
                
#Function used to perform scouring an item
def scour():
    print(f'Scoured')
    #pick up scour
    pyautogui.moveTo(scourX,scourY,duration=0.17)
    pyautogui.rightClick()
    pyautogui.PAUSE
    #use scour
    pyautogui.moveTo(showcaseX,showcaseY,duration=0.17)
    pyautogui.leftClick()
    pyautogui.PAUSE
    #back to transmuting
    transmute()
    
#Function used to perform exalting an item
def exalt():
    print(f'Exalted')
    #pick up exalt
    pyautogui.moveTo(exaltX,exaltY,duration=0.17)
    pyautogui.rightClick()
    pyautogui.PAUSE
    #use exalt
    pyautogui.moveTo(showcaseX,showcaseY,duration=0.17)
    pyautogui.leftClick()
    pyautogui.PAUSE
    #at this point user will manually check what was slammed and get asked if they want to scour or not
    question = input('scour? (y/n) ')
    match question:
        case "y":
            scour()
        case _:
            pyautogui.keyUp('shift')
            print(f'Exiting')
            exit()

input(f'Place cursor over transmute then hit enter')
transX = pyautogui.position().x
transY = pyautogui.position().y
input(f'Place cursor over alteration then hit enter')
altX = pyautogui.position().x
altY = pyautogui.position().y
input(f'Place cursor over augment then hit enter')
augX = pyautogui.position().x
augY = pyautogui.position().y
input(f'Place cursor over regal then hit enter')
regX = pyautogui.position().x
regY = pyautogui.position().y
input(f'Place cursor over scour then hit enter')
scourX = pyautogui.position().x
scourY = pyautogui.position().y
input(f'Place cursor over exalt then hit enter')
exaltX = pyautogui.position().x
exaltY = pyautogui.position().y
input(f'Place cursor over showcase then hit enter')
showcaseX = pyautogui.position().x
showcaseY = pyautogui.position().y
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