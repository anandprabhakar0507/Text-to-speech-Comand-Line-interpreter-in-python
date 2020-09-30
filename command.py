import pip
import os
import pyttsx3

engine = pyttsx3.init()




engine.say("Hello there..how are you..")
engine.say("Please tell me your name by typing ")
engine.runAndWait()
user = input("Please Enter Your name : ")
engine.say("Hello {0}".format(user))
engine.runAndWait()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine.say("If you are a boy then simply type b and for girl please type g")
engine.runAndWait()
gender = input(str("please write here b for boy or g for girl : "))

if( gender == "B" or gender =="b"):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine = pyttsx3.init()
    engine.say("Thank you you are ready to go..")
    engine.runAndWait()
    engine.stop()
    
elif( gender =="F" or gender =="f"):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine = pyttsx3.init()
    engine.say("Thank you you are ready to go..")
    engine.runAndWait()
    engine.stop()
    
else:
    engine = pyttsx3.init()
    engine.say("please enter a character g or b according to your gender")
    engine.runAndWait()
    engine.stop()



os.system("color 0e")

def install(package):
    os.system("color 5f")
    engine = pyttsx3.init()
    engine.say("keep working meanwhile i am checking your voice dependencies")
    engine.runAndWait()
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
    engine.say("All dependencies are update and working")
    engine.runAndWait()
    
    

engine.say("This is a Modern command line Interface created by Anand Prabhakar")
engine.runAndWait()

print("==========================================================================")
print("\n||\tCommand Line Interface CLI 1.0 By Anand Prabhakar,Bihar,India\t||\n||\tPowered by Python. \t\t\t\t\t\t||\n||\tjust learning..no commercial use.. \t\t\t\t||\n")
print("==========================================================================")
def main():
    engine = pyttsx3.init()
    engine.say("Please Enter the command you want to run")
    engine.runAndWait()
    command = input("\n\tEnter the command you want to execute : ")
    
    print("Output after execution : \n")
    print("============================================================")
    commanding(command)
    print("============================================================")
    
    
    

def commanding(i):
    os.system("color 0e")
    engine = pyttsx3.init()
    engine.say("You have entered the following command")
    engine.say(i)
    engine.runAndWait()
    a = os.system(i)
    engine.say("Here is output for the command you entered")
    engine.runAndWait()
    print("\n\t\tDo you want to Enter Command again\n")
    print("-------------------------------------------------------------")
    main()
    return a

if __name__ == "__main__":
    install('pyttsx3')
    main()
    

