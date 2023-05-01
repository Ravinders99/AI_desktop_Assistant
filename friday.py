import pyttsx3  #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import random
import requests,json
base_url="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"


engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speach(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speach("Good MOrning !")
    elif hour>=12 and hour <18:
        speach("Good Afternoon !")
    else:
        speach("Good Evening !")
    speach(" I am Friday , How may i help you Sir !")
def takeinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold =1
        audio = r.listen(source)
    try :
        print("Recoganizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User Said : ",query)
    except Exception as e:
        print("Say Something Again..")
        return "None "
    return query
    
if __name__=="__main__":
    wish()
    while True:
        query =takeinput().lower()
        if "wikipedia" in query:
            
            speach("searching in wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speach(results)
        elif "weather" in query:
            response=requests.get(base_url)
            print(response.text)
           
            # if response.status_code == 200:
            # # getting data in the json format
            #     data = response.json()
            #     # getting the main dict block
            #     main = data['main']
            #     # getting temperature
            #     temperature = main['temp']
            #     # getting the humidity
            #     humidity = main['humidity']
            #     # getting the pressure
            #     pressure = main['pressure']
            #     # weather report
            #     report = data['weather']
            #     print(f"Temperature: {temperature}")
            #     print(f"Humidity: {humidity}")
            #     print(f"Pressure: {pressure}")
            #     print(f"Weather Report: {report[0]['description']}")
            # else:
            # # showing the error message
            #     print("Error in the HTTP request")
                
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open google Chrome" in query:
            webbrowser.open("google.com")
        elif "open python" in query:
            webbrowser.open("https://www.python.org/")
        elif "play music" in query:
            musics ='D:\\music'
            song= os.listdir(musics)
            r=random.choice(song)
            os.startfile(os.path.join(musics,r))
        elif "the time" in query:
            strftime =datetime.datetime.now().strftime("%H:%M:%S: ")
            speach(f"Time is : {strftime}")
            print(f"Time is : {strftime}")
        elif "open code" in query:
            codepath ="C:\\Users\\ravin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'bye' in query:
            break
            
    
