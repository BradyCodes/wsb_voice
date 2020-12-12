
import os
import pyautogui
import webbrowser as wb
import time
import pyttsx3
import speech_recognition as sr

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
            x = r.recognize_google(audio, language="en-US", show_all=False)
            print("Did you say: {}".format(x))
            speak("Did you say: {}".format(x))
            audio_1 = r.listen(source)
            y= r.recognize_google(audio_1,language="en-US",show_all=False)
            print(y)
            if y == "yes" or y == "Yes" or y == "yah" or y =="yo" or y=="yeah":          # yah,yo --> yes
                break
            elif y == "no" or y == "No" or y =="new" or y == "now":         # now,new --> no
                speak("Say it again")
            else:
                speak("Oh O you just said something out of the window.Answer to what is asked naah!")
        return x
def run():               # to cut the error that comes when we are very quick
    try:
        rec()
    except:
        print("Hold down! Please be a bit slow")
        speak("Hold down! Please be a bit slow")
        rec()

# welcome speech

print(" Abrar's Whatsapp Spam Bot \n\n".center(75))
speak("Welcome to Abrar's Whatsapp Spam Bot")
# getting data from user

#QUESTION - I
spam_ques ="--> What do you want me to spam?"
print(spam_ques)
speak(spam_ques)
spam_ans= rec().capitalize().split(" ")       #  "how are you" = ["How","are","you"]

#QUESDTION -II
num_ques = "--> What is the number to whom you want to text?"
print(num_ques)
speak(num_ques)
num_ans = rec()
num_ans = str(num_ans.replace(" ",""))     #   '123 4567 890' = 1234567890
num_ans = str(num_ans.replace("-", ""))
int(num_ans)

#QUESTION-III
rep_ques ="--> How many times do you want to send this text?"
print(rep_ques)
speak(rep_ques)
rep_ans = str(rec().replace(" ", ""))                  #    "202" = 202
rep_ans = int(rep_ans)

# Switch to Whatsapp

wb.open("https://wa.me/1{}".format(num_ans))
time.sleep(10)                            # --> waiting for loading
pyautogui.press("enter")                  # --> to allow
time.sleep(10)
for i in range(rep_ans):
    for j in range(len(spam_ans)):
        pyautogui.write(spam_ans[j],interval=0.2)
        pyautogui.press("enter")


print(time.localtime())
