import pyautogui
import webbrowser as wb
import time
import pyttsx3
import speech_recognition as sr
import os

os.system('clear')

def speak(x):
    engine = pyttsx3.init()
    engine.say(x)
    # engine.save_to_file(filename="hello.txt", text="who are you")
    engine.runAndWait()
def rec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sr.Recognizer().adjust_for_ambient_noise(source, duration=0.5)
        while(True):
            audio = r.listen(source)
            x = r.recognize_google(audio, language="en-IN", show_all=False)
            print("Did you say: {}".format(x))
            speak("Did you say: {}".format(x))
            audio_1 = r.listen(source)
            y= r.recognize_google(audio_1,language="en-IN",show_all=False)
            print(y)
            if y == "yes" or y == "Yes" or y == "yah" or y =="yo" or y=="yeah":          # yah,yo --> yes
                break
            elif y == "no" or y == "No" or y =="new" or y == "now":         # now,new --> no
                speak("Say it again")
            else:
                speak("Please Answer with yes or no")
        return x
def run():               # to cut the error that comes when we are very quick
    try:
        rec()
    except:
        print("Hold down! Please be a bit slow")
        speak("Hold down! Please be a bit slow")
        rec()

questions = [
    "What Do You Want me to Spam?",
    "What is the number of whom you'd like to spam?",
    "How many times would you like to spam this message?"
]
spam_ans = 0
num_ans = 0
rep_ans = 0


def askRecieve(q, type):
    print(q)
    speak(q)
    if type == "spam_ans":
        spam_ans= rec().capitalize().split(" ")
    elif type == "num_ans":
        num_ans = rec()
        num_ans = int(num_ans.replace(" ",""))
        num_ans = int(num_ans.replace("-",""))
    elif type == "rep_ans":
        rep_ans = int(rec())

# welcome speech

print(" Abrar's Whatsapp Spam Bot \n\n".center(75))
speak("Welcome to Abrar's Whatsapp Spam Bot")
# getting data from user

askRecieve(questions[0], "spam_ans")
askRecieve(questions[1], "num_ans")
askRecieve(questions[2], "rep_ans")


#QUESTION - I
# spam_ques ="--> What do you want me to spam?"
# print(spam_ques)
# speak(spam_ques)
# spam_ans= rec().capitalize().split(" ")       #  "how are you" = ["How","are","you"]

# #QUESDTION -II
# num_ques = "--> What is the number to whom you want to text?"
# print(num_ques)
# speak(num_ques)
# num_ans = rec()
# num_ans = int(num_ans.replace(" ",""))     #   '123 4567 890' = 1234567890

# #QUESTION-III 
# rep_ques ="--> How many times do you want to send this text?"
# print(rep_ques)
# speak(rep_ques)
# rep_ans = int(rec())                  #    "202" = 202

# Switch to Whatsapp

wb.open("https://wa.me/91{}".format(num_ans))
time.sleep(10)                            # --> waiting for loading
pyautogui.press("enter")                  # --> to allow
time.sleep(10)
for i in range(rep_ans):
    for j in range(len(spam_ans)):
        pyautogui.write(spam_ans[j],interval=0.2)
        pyautogui.press("enter")


print(time.localtime())