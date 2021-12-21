import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import random
import urllib.request
import urllib.parse
import re
import sys
import unidecode
import os


friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[1].id)
voice_num = 0

def speak(audio):
    
    print('S.O.S: ' + audio)
    
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
    hour = datetime.datetime.now().hour
    if hour == 11:
        speak('Time to eat something! Sir')
    elif hour == 12:
        speak('Did you eat anything! Sir?')
        speak('Lunch is very important')
        speak('I can suggest you some food for lunch')
        wb.get().open(f'https://shopeefood.vn/ha-noi/food')
    elif hour == 13:
        speak('You should sleep! Sir')
        speak('It is for you health')

def today():
    t = datetime.date.today().strftime("%B %d, %Y")
    speak(t)    



def welcome():
    global voice_num
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak('Good Morning Sir')
    elif 12 <= hour < 18:
        speak('Good Afternoon Sir')
    elif 18 <= hour < 24:
        speak('Good Evening Sir')
    elif 0 <= hour < 6:
        speak('Good Night Sir')
        
    speak('I am S.O.S.') 

def wikipedia():
    speak('Of course Sir, I know everything')
    speak('What do you want to know?')
    search = command().lower()
    search = search.replace(" ","_")
    url = f'https://en.wikipedia.org/wiki/{search}'
    wb.get().open(url)

def youtube():
    speak('What do you want Sir, search or video?')

    query = command().lower()

    while "tìm" not in query and "video" not in query:
        speak("Can you say again?")
        query = command().lower()
    
    if "tìm" in query:
        speak("What should i search Sir?")
        search = command().lower()            
        youtube_search = search.replace(" ","+")
        url = f"https://www.youtube.com/results?search_query={youtube_search}"        
                                                      
        wb.get().open(url)            
                    
        speak(f'Here is your list of video on Youtube')
    elif "video" in query:
        speak("What should i search Sir?")
        search = command().lower()     
        search = remove_accent(search)       
        youtube_search = search.replace(" ","+")
        url = f"https://www.youtube.com/results?search_query={youtube_search}"          
           
        html_content = urllib.request.urlopen(url)
        search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())                               

        index = 0 
        
        wb.get().open("https://www.youtube.com/watch?v=" + search_results[index])
        speak(f'Here is your video on Youtube')        

        stop = 0
        while stop == 0:
            speak('Do you want open more! Sir')
            choose = command_en().lower()

            while 'yes' not in choose and 'no' not in choose:
                speak('I do not know! Sir')
                choose = command_en().lower()

            if 'yes' in choose:
                index += 1
                try:
                    wb.get().open("https://www.youtube.com/watch?v=" + search_results[index])
                    speak(f'Here is your video on Youtube')
                except IndexError:
                    speak('Oh no, I can not open more! Sir')
                    speak('I opened all the videos that youtube has')
                    speak('You can try to find another keyword')
                    break
            elif 'no' in choose:
                stop = 1
                speak('Enjoy the video! Sir')                                 


def remove_accent(text):
    return unidecode.unidecode(text)

def Google():
    speak('I will do it right now')
    speak("What should i search Sir?")
    search = command().lower()
    url = f"https://www.google.com.vn/search?q={search}"
    wb.get().open(url)
    speak(f'Here is your search on Google')

def Facebook():
    speak('Here is your Facebook')
    url = f"https://www.facebook.com/"
    wb.get().open(url)  

def Messenger():
    speak('Here is your Messenger')
    url = f"https://www.facebook.com/messages/"
    wb.get().open(url)

def TFT():
    speak('Here is your Teamfight Tactics')
    url = f"https://tftactics.gg/tierlist/team-comps"
    wb.get().open(url)

def codeforce():
    speak('Here is your Codeforces')
    speak('Good luck! Sir')
    url = f"https://codeforces.com/"
    wb.get().open(url) 

def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")      
        
        audio = c.record(source,duration=5)        
    try:
        query = c.recognize_google(audio,language = 'vi')
        print("ME: " + query)
    except sr.UnknownValueError:
        rand_num = random.randint(1,3)
        if rand_num == 1:            
            speak("Please order me! Sir ")
        elif rand_num == 2:
            speak("Please say something! Sir ")
        elif rand_num == 3:
            speak("Do you want to search something! Sir ")        
        query = command()
        
    return query

def command_en():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")      
        
        audio = c.record(source,duration=5)        
    try:
        query = c.recognize_google(audio,language = 'en')
        print("ME: " + query)
    except sr.UnknownValueError:
        rand_num = random.randint(1,3)
        if rand_num == 1:            
            speak("Please order me! Sir ")
        elif rand_num == 2:
            speak("Please say something! Sir ")
        elif rand_num == 3:
            speak("Do you want to search something! Sir ")        
        query = command_en()
        
    return query

def command_open():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("sleeping...")             
        audio = c.record(source,duration=10)        
    try:
        query = c.recognize_google(audio,language = 'en')        
    except sr.UnknownValueError:                
        query = command_open()
        
    return query

def command_user():
    global check_i,isRunning
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("loading...")             
        audio = c.record(source,duration=5)        
    try:
        query = c.recognize_google(audio,language = 'vi')        
    except sr.UnknownValueError:
        query = ' '
        
    return query

def sleep():
    speak('Okay Sir!')
    speak('If you want something, just call wake up! Sir')
    wake_up = command_open().lower()
    while 'wake up' not in wake_up:
        wake_up = command_open().lower()    

def SOS():
    global isRunning

    speak('How can i help you?')
    query = command().lower()
    if "mở google" in query:
        Google()
    elif "mở youtube" in query:
        youtube()
    
    elif "ngắt kết nối" in query or "tắt kết nối" in query:
        speak('Thank you Sir! Goodbye Sir!')
        isRunning = False
        return        
    elif "mở facebook" in query:            
        Facebook()
    elif "mở messenger" in query:
        Messenger() 
    elif "mở đấu trường chân lý" in query:
        TFT()    
    elif "mấy giờ" in query:
        time()
    elif "hôm nay là ngày" in query:
        today()
    elif "tìm thông tin cho tôi" in query:
        wikipedia()    
    elif "nghỉ ngơi đi" in query:
        sleep()   
    else:
        speak("i do not understand")
        return

def check_user():
    global isRunning, check_i
    speak('Who are you?')    
    query = command_user().lower()
    while 'bùi khắc đạt' not in query:
        speak('Wrong answer!')
        query = command_user().lower()
        check_i += 1
        if check_i == 2:
            speak('You are not my boss')
            speak('Security mode on !')
            isRunning = False
            return

if __name__ == '__main__':
    isRunning = True
    check_i = 0
    check_user()
    if isRunning == False:
        quit()
    welcome()   
    while isRunning:
        SOS()

        
    
    

