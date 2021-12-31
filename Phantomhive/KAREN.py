import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import urllib.request
import urllib.parse
import re
import unidecode
import requests
import time
import difflib
import holidays
#data chat bot
from chatbot import *
#chatterbot import
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot.filters import get_recent_repeated_responses

#vitural assistant:
vitural_assistant = pyttsx3.init()
voice = vitural_assistant.getProperty('voices')
vitural_assistant.setProperty('voice',voice[1].id)

#chat bot:
karen = ChatBot(
    "Karen",
    logic_adapters = [                
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": levenshtein_distance,
            "response_selection_method": get_first_response
        }                       
    ],
    filters=[get_recent_repeated_responses],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///db.sqlite3',
    read_only = True    
)

# train:
train_list = ListTrainer(karen)
for key in chatbot_data.keys():
    train_list.train(chatbot_data[key])
# holidays:
vi_holidays = holidays.Vietnam() + holidays.US() 
# global:
check_i = 0
isRunning = True
#feature:

def Match_command(query):
    max_ability = 0
    key_choose = ''
    for k in chatbot_command.keys():
        for data in chatbot_command[k]:
            diff1 = difflib.SequenceMatcher(None,query,data).ratio()
            if diff1 > max_ability:
                key_choose = k
                max_ability = round(diff1,2)
    return key_choose,max_ability

def speak(audio):    
    print(bot_name + ': ' + audio)    
    vitural_assistant.say(audio)
    vitural_assistant.runAndWait()

def time_now():    
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
    hour = datetime.datetime.now().hour
    if hour == 11:
        speak('Time to eat something')
    elif hour == 12:
        speak('Did you eat anything?')
        speak('Lunch is very important')
        speak('I can suggest you some food for lunch')
        wb.get().open(f'https://shopeefood.vn/ha-noi/food')
    elif hour == 13:
        speak('You should sleep')
        speak('It is for you health')
    elif hour == 17:
        speak('You should cook for dinner')  
    time.sleep(3) 

def lock_Karen():    
    global isRunning
    Time = datetime.datetime.now().strftime("%I:%M:%p")    
    hour = datetime.datetime.now().hour
    if hour == 22 or hour == 23 or 0 <= hour <= 5:
       speak('You must go to bed')
       speak('It is too dangerous for your health')       
       isRunning = False
       return
    speak('How can i help you?')    
         
def today():
    t = datetime.date.today().strftime("%B %d, %Y")
    speak(t)        

def check_today():
    day = datetime.date.today().day
    month = datetime.date.today().month
    year = datetime.date.today().year
    check_holiday = str(str(day) + '-' + str(month) + '-' + str(year))
    check_hd = vi_holidays.get(check_holiday)
    if check_hd == None:
        speak('A normal day!')
    else:
        speak(check_hd)
    time.sleep(3)

def Welcome():   
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak('Good Morning ' + user_name)
    elif 12 <= hour < 18:
        speak('Good Afternoon ' + user_name)
    elif 18 <= hour < 24:
        speak('Good Evening ' + user_name)
    elif 0 <= hour < 6:
        speak('Good Night ' + user_name)
    
    speak('Welcome to the V.A project') 
    return     

def Wikipedia():
    speak('About what')    
    search = command().lower()
    search = search.replace(" ","_")
    url = f'https://vi.wikipedia.org/wiki/{search}'
    wb.get().open(url)
    speak(f'Here you are')
    time.sleep(3)

def Youtube():
    speak('Search or Video?')

    query = command().lower()

    while "tìm" not in query and "video" not in query:
        speak('You must choose! search or video!')
        speak("Can you say again?")
        query = command().lower()
    
    if "tìm" in query:
        speak("What should i search?")
        search = command().lower()            
        youtube_search = search.replace(" ","+")
        url = f"https://www.youtube.com/results?search_query={youtube_search}"        
                                                      
        wb.get().open(url)            
                    
        speak(f'Here is your list of video on Youtube')
    elif "video" in query:
        speak("What should i search?")
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
            speak('Do you want open more!')
            choose = command().lower()

            while 'có' not in choose and 'không' not in choose:
                speak('I do not understand')
                speak('Please choose, Yes or No in Vietnamese!')
                choose = command().lower()

            if 'có' in choose:
                index += 1
                try:
                    wb.get().open("https://www.youtube.com/watch?v=" + search_results[index])
                    speak(f'Here is your video on Youtube')
                except IndexError:
                    speak('Oh no, I can not open more!')
                    speak('I opened all the videos that youtube has')
                    speak('You can try to find another keyword')
                    break
            elif 'không' in choose:
                stop = 1
                speak('Enjoy the video!')                                 

def Github():
    speak('I will do it right now')
    wb.get().open(f'https://github.com/')

def remove_accent(text):
    return unidecode.unidecode(text)

def Google():    
    speak("What should i search?")
    search = command().lower()
    url = f"https://www.google.com.vn/search?q={search}"
    wb.get().open(url)
    speak(f'Here you are')

def Facebook():
    speak('Here you are')
    url = f"https://www.facebook.com/"
    wb.get().open(url)  

def Messenger():
    speak('Here you are')
    url = f"https://www.facebook.com/messages/"
    wb.get().open(url)

def TFT():
    speak('Here you are')
    url = f"https://tftactics.gg/tierlist/team-comps"
    wb.get().open(url)

def codeforce():    
    speak('Good luck!')
    url = f"https://codeforces.com/"
    wb.get().open(url) 

def email():   
    url = f"https://mail.google.com/mail/u/0/#inbox"   
    wb.get().open(url)
    speak('Here you are')

def google_map():
    speak('What place do you want to find?')
    place = command().lower()
    place = place.replace(" ","+")
    url = f"https://www.google.com/maps/place/{place}"    
    wb.get().open(url)
    speak('Here you are') 

def go_to():
    speak('Go to where?')
    query = command().lower()
    if not query:
        pass
    place_1 = place_now.replace(" ","+")
    place_2 = query.replace(" ","+")
    url = f"https://www.google.com/maps/dir/{place_1}/{place_2}/"
    wb.get().open(url)
    speak('I found the way for you, it is the best way')
   
def current_weather():
    speak("Where are you?")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = command().lower()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]        
        current_humidity = city_res["humidity"]        
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.today().strftime("%B %d, %Y")
        
        content = """ 
        Today is {today}         
        Average temperature is {temp} degrees C         
        Humidity is {humidity}%
        Weather description: {plz}""".format(   today = now,                                                  
                                                temp = current_temperature, humidity = current_humidity,
                                                plz = weather_description,   )
        
        speak(content)
        time.sleep(3)
    else:
        speak("Your city is not found! Please try agian!")

def chat_bot(query): 
    response = karen.get_response(query)    
    if response.confidence < 0.65:
        speak('i don\'t know, i\'m still learning')        
    else:
        answer = str(response)
        speak(answer)
    time.sleep(1) 

def Security():
    global isRunning, check_i    
    speak('What is the password?')    
    query = command_user().lower()
    password = AI_pass
    while password not in query:
        speak('Wrong!')
        query = command_user().lower()
        check_i += 1
        if check_i == 2:
            speak('Security mode on !')
            isRunning = False
            return

def sleep_mode():    
    speak('If you want something, just call me!')
    wake_up = command_open().lower()
    while 'dậy' not in wake_up and 'làm việc' not in wake_up and 'có ở đó' not in wake_up:
        wake_up = command_open().lower()
    speak('I\'m back')
    return 

def open_Web():
    speak('What\'s website?')
    query = command().lower()
    if "google" in query and "map" in query:
        google_map()
    elif "google" in query:
        Google()
    elif "youtube" in query:
        Youtube()
    elif "facebook" in query:
        Facebook()
    elif "đấu trường chân lý" in query:
        TFT()
    elif "lập trình thi đấU" in query:
        codeforce()
    elif "messenger" in query:
        Messenger()    
    elif "email" in query:
        email()    
    else:        
        wb.get().open('https://www.google.com.vn/search?q={query}')
        speak('Here you are. I\'m not sure')
        time.sleep(3)
        return
      
    time.sleep(3)

#command:
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")           
        audio = c.record(source,duration=5)        
    try:
        query = c.recognize_google(audio,language = 'vi')
        print(user_name + ': ' + query)
    except sr.UnknownValueError:                
        query = command()
        
    return query

def command_open():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("sleeping...")             
        audio = c.record(source,duration=6)        
    try:
        query = c.recognize_google(audio,language = 'vi')        
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
        print("PASSWORD: " + query)        
    except sr.UnknownValueError:
        query = 'none'
        print("PASSWORD: " + query)
        
    return query
 
#KAREN:            
def KAREN():
    global isRunning    
    query = command().lower()   
    
    key_cmd,ability = Match_command(query)
        
    if ability < 0.7:
        key_cmd = 'chat'
        print('--Chat mode--') 

    if 'tắt nguồn' in key_cmd:
        speak('See you again Sir!')
        isRunning = False
        return               
    elif 'giờ' in key_cmd:
        time_now()
    elif 'ngày' in key_cmd:
        today()
        check_today()
    elif 'thời tiết' in key_cmd:
        current_weather()
    elif 'ở đâu' in key_cmd:
        place = place_now
        place = place.replace(" ","+")
        url = f"https://www.google.com/maps/place/{place}"    
        wb.get().open(url)
        speak('Here you are')
    elif 'đi tới' in key_cmd:
        go_to()
    elif 'thông tin' in key_cmd:
        Wikipedia()
    elif 'web' in key_cmd:
        open_Web()    
    elif 'nghỉ ngơi' in key_cmd:
        sleep_mode()
    else:
        chat_bot(query)

def run_vitural_assistant():    
    # Security()
    # if isRunning == False:
    #     quit() 
    Welcome()    
    lock_Karen()    
    while isRunning:
        KAREN()

if __name__ == '__main__':
    run_vitural_assistant()

# def chat_bot(query):
#     max_abi = 0
#     index = 0
#     key = 0    
#     for i in chatbot_data.keys():
#         data = chatbot_data[i]
#         for k, val in enumerate(data):
#             dif = difflib.SequenceMatcher(None,query,val).ratio()
#             if dif > max_abi:
#                 max_abi = round(dif,2)
#                 index = k+1
#                 key = i
    
#     if max_abi < 0.55:
#         speak('i don\'t understand sir, i\'m still learning')
#     else:
#         print('Match rate = ' + str(max_abi))
#         speak(chatbot_data[key][index])
    
#     time.sleep(1)        
    
    

