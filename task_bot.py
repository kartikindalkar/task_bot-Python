import sys
import os
import pyttsx3 as pyt

print("*"*100)
print("""
This Bot Is Help for you.To Open, execute or run Task like Calculator(calc),Notepad,Wmplayer,Firefox.
You Can run this Bot on provided commands.
Steps:
1.Enter Your Name
2.Enter your Task Name
    eg.open notepad,run firefox,
    can you open wmplayer,want to open calc,etc;
""")
print("*"*100)
pyt.speak("Enter Your Name Below")
name = str(input("Enter Your Name:  "))
pyt.speak("Hello" + name + " What i can do for You.")
pyt.speak("We are here for do your some task like notepad,firefox,calc")
pyt.speak("Enter Your Input Below")
while True: 
    keys = input("Enter your Input: ")
    if ((("run" in keys)
        and ("start" in keys)
        and ("execute" in keys)
        and ("run" in keys)
        and ("open" in keys))
        or (("i")
        and ("want to start" in keys)
        and ("want to open" in keys)
        and ("want to run" in keys)
        and ("want to execute" in keys))
        or (("can you")
        and ("please start" in keys)
        and ("please open" in keys)
        and ("please run" in keys)
        and ("please execute" in keys)
        or ("notepad" in keys))):
        os.startfile("notepad")
        pyt.speak("Notepad started")
            
    elif((("run" in keys)
        and ("start" in keys)
        and ("execute" in keys)
        and ("run" in keys)
        and ("open" in keys))
        or (("i")
        and ("want to start" in keys)
        and ("want to open" in keys)
        and ("want to run" in keys)
        and ("want to execute" in keys))
        or (("can you")
        and ("please start" in keys)
        and ("please open" in keys)
        and ("please run" in keys)
        and ("please execute" in keys)
        or ("wmplayer" in keys))):
        os.startfile("wmplayer")
        pyt.speak("wmplayer started")
        
    elif((("run" in keys)
        and ("start" in keys)
        and ("execute" in keys)
        and ("run" in keys)
        and ("open" in keys))
        or (("i")
        and ("want to start" in keys)
        and ("want to open" in keys)
        and ("want to run" in keys)
        and ("want to execute" in keys))
        or (("can you")
        and ("please start" in keys)
        and ("please open" in keys)
        and ("please run" in keys)
        and ("please execute" in keys)
        or ("firefox" in keys))):
        os.startfile("firefox")
        pyt.speak("firefox started")
        
    elif((("run" in keys)
        and ("start" in keys)
        and ("execute" in keys)
        and ("run" in keys)
        and ("open" in keys))
        or (("i")
        and ("want to start" in keys)
        and ("want to open" in keys)
        and ("want to run" in keys)
        and ("want to execute" in keys))
        or (("can you")
        and ("please start" in keys)
        and ("please open" in keys)
        and ("please run" in keys)
        and ("please execute" in keys)
        or ("calc" in keys))):
        os.startfile("calc")
        pyt.speak("calc started")
        
    elif(("no") or ("stop") or ("exit") or ("no thanks") or ("no thank you") or("bye") or("close") in key):
        pyt.speak("Program exit")   
        pyt.speak("Welcome"+ name + "visit again")        
        break   

        
    
    


