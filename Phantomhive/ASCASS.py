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
from googletrans import Translator
#chatterbot import
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot.filters import get_recent_repeated_responses

# Vitural assistant:
vitural_assistant = pyttsx3.init()
voice = vitural_assistant.getProperty('voices')
vitural_assistant.setProperty('voice',voice[0].id)

# Translated:
trans = Translator()

# Chat bot:
Ascass = ChatBot(
    "ASCASS",
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

# A Smart Chatbot And Support System
bot_text_name = 'A.S.C.A.S.S.'
bot_name = 'ASCASS' 
user_name = 'Mr D'
AI_pass = '2003'
# chatbot:
mybot = ListTrainer(Ascass)
# holidays:
vi_holidays = holidays.Vietnam() + holidays.US() 
# global:
check_i = 0
isRunning = True
list_to_train = []
# command:
chatbot_command = {
    'tắt nguồn' : [
        'tắt nguồn',
        'ngắt kết nối',
        'tắt kết nối',
        'tạm biệt',
        'tạm biệt karen',
        'chúc ngủ ngon',
        'ngủ ngon',
        'tôi ra ngoài',
        'tôi phải ra ngoài',
        'tôi phải đi đây'        
    ],
    
    'giờ' : [
        'bây giờ là mấy giờ',
        'mấy giờ rồi',
        'bây giờ là'

    ],
    
    'ngày' : [
        'hôm nay là ngày nào',
        'hôm nay là',
        'hôm nay là ngày mấy',
        'hôm nay là ngày bao nhiêu',
        'nay là ngày bao nhiêu',
        'nay là ngày nào',
        'nay là ngày mấy'
    ],
    
    'thời tiết' : [
        'thời tiết hôm nay như thế nào',
        'thời tiết hôm nay',
        'thời tiết hôm nay như nào',
        'thời tiết hôm nay ra sao',
        'thời tiết như nào',
        'thời tiết thì sao',
        'thời tiết ra sao'
    ],
    
    'thông tin' : [
        'tìm thông tin cho tôi',
        'cho tôi biết về',
        'tìm thông tin về',
        'cho tôi biết'                
    ],
    
    'web' : [
        'mở mạng cho tôi',
        'mở website cho tôi',
        'mở mạng',
        'mở web',
        'mở website',
        'mở web cho tôi',
        'mạng',
        'web',
        'website',
        'mở youtube',
        'mở google',
        'mở facebook'
    ],
    
    'nghỉ ngơi' : [
        'chế độ nghỉ ngơi',
        'ngủ trưa',
        'nghỉ ngơi',
        'nghỉ ngơi đi',
        'ok nghỉ ngơi đi',
        'im lặng',
        'im',
        'im miệng',
        'im mồm'
    ]
}

# feature:

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
    print(bot_text_name + ': ' + audio)    
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
    time.sleep(1) 

def lock_ASCASS():    
    # global isRunning    
    # hour = datetime.datetime.now().hour
    # if hour == 22 or hour == 23 or 0 <= hour <= 5:
    #    speak('You must go to bed')
    #    speak('It is too dangerous for your health')       
    #    isRunning = False
    #    return
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
    time.sleep(1)

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
    
    speak('Welcome back')
    speak("I am " + bot_name) 
    return     

def Wikipedia():
    speak('About what')    
    search = command().lower()
    search = search.replace(" ","_")
    url = f'https://vi.wikipedia.org/wiki/{search}'
    wb.get().open(url)
    speak(f'Here you are')
    time.sleep(1)

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

def remove_accent(text):
    return unidecode.unidecode(text)
  
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
        if current_temperature < 15:
            speak("You should wear more coats")
            speak("Or get a girlfriend")
        time.sleep(3)
    else:
        speak("Your city is not found! Please try agian!")
  
def chat_bot(query):
    response = Ascass.get_response(query)
    if response.confidence < 0.75:
        speak("I'm sorry. Can you teach me?")
        choice = input("Yes or No: ")
        if choice == "yes":
            train_new_chat(query)
        else:
            return        
    else:
        speak(str(response))

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
    wake_up = command_open().lower()
    while 'hi' not in wake_up:
        wake_up = command_open().lower()
    speak('How can i help you?')
    return 

def open_Web():
    speak('What\'s website?')
    query = command().lower()
    if "google" in query and "map" in query:
        speak('What place do you want to find?')
        place = command().lower()
        place = place.replace(" ","+")
        url = f"https://www.google.com/maps/place/{place}"    
        wb.get().open(url)
        speak('Here you are') 
    elif "google" in query:
        speak("What should i search?")
        search = command().lower()
        url = f"https://www.google.com.vn/search?q={search}"
        wb.get().open(url)
        speak(f'Here you are')
    elif "youtube" in query:
        Youtube()
    elif "facebook" in query:
        speak('Here you are')
        url = f"https://www.facebook.com/"
        wb.get().open(url) 
    elif "đấu trường chân lý" in query:
        speak('Here you are')
        url = f"https://tftactics.gg/tierlist/team-comps"
        wb.get().open(url)
    elif "lập trình thi đấu" in query:
        speak('Good luck!')
        url = f"https://codeforces.com/"
        wb.get().open(url)
    elif "messenger" in query:
        speak('Here you are')
        url = f"https://www.facebook.com/messages/"
        wb.get().open(url)    
    elif "email" in query:
        url = f"https://mail.google.com/mail/u/0/#inbox"   
        wb.get().open(url)
        speak('Here you are')
    elif "github" in query or "git" in query:
        speak('I will do it right now')
        wb.get().open(f'https://github.com/')
    else:        
        wb.get().open(f'https://www.google.com.vn/search?q={query}')
        speak('Here you are. I\'m not sure')
        time.sleep(3)
        return
      
    time.sleep(3)

# command:

def command():
    global time_count_response
    c = sr.Recognizer()    
    with sr.Microphone() as source:
        print("listening...")          
        audio = c.record(source,duration=8)        
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
        audio = c.record(source,duration=8)        
    try:
        query = c.recognize_google(audio,language = 'en')        
    except sr.UnknownValueError:                
        query = command_open()
        
    return query

def command_user():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("loading...")             
        audio = c.record(source,duration=8)        
    try:
        query = c.recognize_google(audio,language = 'vi')
        print("PASSWORD: " + query)        
    except sr.UnknownValueError:
        query = 'none'
        print("PASSWORD: " + query)       
    return query

# train:

def train_new_chat(query):
    print("New question: " + query)
    new_a = input("New answer: ")
    new_a_after_trans = trans.translate(new_a,src='vi',dest='en').text
    mybot.train([
        query,
        new_a_after_trans
    ])    

# Ascass: 
           
def ASCASS():
    global isRunning, time_count_response   
    query = command().lower()   
    
    key_cmd,ability = Match_command(query)
        
    if ability < 0.7:
        key_cmd = 'chat'
        print('--Chat mode--') 

    if 'tắt nguồn' in key_cmd:        
        speak('See you again ' + str(user_name))
        isRunning = False
        return               
    elif 'giờ' in key_cmd:
        time_now()
    elif 'ngày' in key_cmd:
        today()
        check_today()
    elif 'thời tiết' in key_cmd:
        current_weather()
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
    # train_bot()
    Welcome()    
    lock_ASCASS()    
    while isRunning:
        ASCASS()

if __name__ == '__main__':
    run_vitural_assistant()

     
    
    

