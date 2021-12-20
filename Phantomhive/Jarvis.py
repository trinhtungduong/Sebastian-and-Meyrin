import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import random
import urllib.request
import urllib.parse
import re


friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)
voice_num = 0

def speak(audio):
    global voice_num
    if voice_num == 0:
        print('JINN-SAN: ' + audio)
    elif voice_num == 1:
        print('SAKURA-SAN: ' + audio)

    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

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
        
    if voice_num == 0:
        speak('I am Jinn.')
    elif voice_num == 1:
        speak('I am Sakura.')       
    
def change_voice(num):
    global voice_num
    if num == 1:
        friday.setProperty('voice',voice[0].id)
        voice_num = 0
    elif num == 2:
        friday.setProperty('voice',voice[1].id)
        voice_num = 1
    
    welcome()


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")      
        
        audio = c.record(source,duration=5)        
    try:
        query = c.recognize_google(audio,language = 'en')
        print("Koumei: " + query)
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


if __name__ == '__main__':
    welcome()
    while True:
        speak('How can i help you?')
        query = command().lower()
        if "google" in query:
            speak("What should i search Sir?")
            search = command().lower()
            url = f"https://www.google.com.vn/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on Google')
        elif "youtube" in query:
            speak("What should i search Sir?")
            search = command().lower()            
            youtube_search = search.replace(" ","+")
            url = f"https://www.youtube.com/results?search_query={youtube_search}"            
            
            html_content = urllib.request.urlopen(url)
            search_results = re.findall(r'watch\?v=(\S{11})', html_content.read().decode())                                  
            
            wb.get().open("https://www.youtube.com/watch?v=" + search_results[0])            
                    
            speak(f'Here is your {search} on Youtube')
        elif "go to bed" in query:
            speak('Goodbye Sir!')
            break        
        elif "facebook" in query:            
            url = f"https://www.facebook.com/"
            wb.get().open(url)
        elif "lady voice" in query:
            change_voice(2)
        elif "man voice" in query:
            change_voice(1)
        elif "what time" in query:
            time()
        else:
            speak("i do not understand")
            continue

        
    
    

