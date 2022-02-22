import pyttsx3
import speech_recognition as sr
#data
from myself import *
#chatterbot import
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response
from chatterbot.comparisons import levenshtein_distance
from chatterbot.filters import get_recent_repeated_responses
#
import json

#START:
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)

Jarvis = ChatBot(
    "JARVIS",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [                
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": levenshtein_distance,
            "response_selection_method": get_first_response
        }                       
    ],
    filters=[get_recent_repeated_responses],    
    database_uri='sqlite:///data.sqlite3',
    read_only = True    
)

train_list = ListTrainer(Jarvis)
for key in chatbot_data.keys():
    train_list.train(chatbot_data[key])        

# global:
check_i = 0
isRunning = 1
# chat bot:
def speak(audio):    
    print('J.A.R.V.I.S. ' + ': ' + audio)    
    friday.say(audio)
    friday.runAndWait()

def welcome():       
    speak('Hello')      
      
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")           
        audio = c.record(source,duration=8)        
    try:
        query = c.recognize_google(audio,language = 'vi')
        print('Duong' + ': ' + query)
    except sr.UnknownValueError:                
        query = command()       
    return query


def chat_bot(query):
    pass
            

# Jarvis:            
def Jarvis():
    global isRunning    
    query = command().lower()    
    chat_bot(query)
    isRunning += 1

def run_vitural_assistant():  
    welcome()     
    while isRunning <= 100:
        Jarvis()

# if __name__ == '__main__':
#     run_vitural_assistant()

        
    
    

