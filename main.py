import ctypes
import os
import pyttsx3
import datetime
import speech_recognition as srecog
import wikipedia
import webbrowser
import random
import pyautogui 
from time import sleep 
import screen_brightness_control as sbc 
import time
from bs4 import BeautifulSoup
import requests
import subprocess
from ecapture import ecapture as ec
import sys
import platform
import clipboard
import winshell as winshell          
from geopy.geocoders import Nominatim
from geopy import distance
from pywikihow import search_wikihow 
import openai
import psutil
import wmi
import cohere


co = cohere.Client("WoCIsw0H3SOeEuHtzGGmQeP28i7CDHiIT6GAgpsK")


openai.api_key = "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"




system = platform.system()
if system == "Windows":
    print("System: Windows")
    print("Loading Sapi5 engine")
    engine_to_use = "sapi5"
elif system == "Darwin":
    print("System: MacOS")
    print("Loading nsss engine")
    engine_to_use = "nsss"
else:
    # Linux, Posix, BSD, etc.
    print("System: %s" % system)
    print("Loading espeak engine")
    engine_to_use = "espeak"
try:
    engine = pyttsx3.init(engine_to_use)
except Exception as err:
    print("Could not load the TTS engine. Do you have it properly installed?")
    print("Error:")
    print(err)
    sys.exit("Critical Error")
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')
list_of_jokes = ["The three most well known languages in India are English, Hindi, and... JavaScript","Interviewer... Where were you born?Me in India... Interviewer:.. oh, which part?... Me: What ‘which part’ ..? Whole body was born in India","how many Indians does it take to fix a lightbulb?Two. One to do the task and other to explain how lightbulbs were actually invented in ancient India","What do you call bread from India? It's Naan of your business","Britain: Drive on the left side... Europe and America: Drive on the right side...India: lol what's a 'traffic law'?"]
jokes = len(list_of_jokes)-1
ran_joke=random.randint(0,jokes)

def speak(audio): #speak audio
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #wishes me
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=3:
        speak("It's Late Night Sir!, You should sleep right now")
    elif hour>=4 and hour<12:
        speak("Good Moring Master!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir !")
    elif hour>=17 and hour<19:
        speak("Good Evening !")
    elif hour>=19 and hour<24:
        speak("Good Night Sir!")
    if hour>=0 and hour<=4:
        pass
    else:
        speak("I am Your Personal assistant, atom! version 1.2!")

def takeCommand(): #takes microphone inout and returns output
    global meaw
    r=srecog.Recognizer()
    with srecog.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:   
        return "None" 
    return query



if __name__ == "__main__":
    wishMe()
    speak("How May I Help You Sir ?")
    while True:
        query = takeCommand().lower()
   
        if 'wikipedia' in query:
            speak('Searching in Wikipedia')
            query = query.replace("according to wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("Accoring to Wikipedia")
            print(results)
            speak(results)
            speak("anything else for which i may assist you")
        
        elif 'screenshot' in query:
            speak("screenshot taking ,sir")
            times = time.time()
            name_img = r"{}.png".format(str(times))
            img = pyautogui.screenshot(name_img)
            speak("screenshot is taken, sir")
            img.show()
        
        elif 'read' in query and 'clipboard' in query:
            text = clipboard.paste()
            try:
                speak(text)
            except Exception as e:
                speak("Cannot read the text ,sir")
      
        elif 'what you want to do' in query:
            speak("I want to help people to do certain tasks on their single voice commands.")
        
        elif 'alexa' in query:
            speak("I don't know Alexa, but I've heard of Alexa. If you have Alexa, "
                        "I may have just triggered Alexa. If so, sorry Alexa.")
        
        elif 'google assistant' in query:
            speak("He was my classmate, too intelligent guy. We both are best friends.")
        
        elif 'siri' in query:
            speak("Siri, She's a competing virtual assistant on   a competitor's phone. "
                        "Not that I'm competitive or anything.")
        
        elif 'cortana' in query:
            speak("I thought you'd never ask. So I've never thought about it.")
        
        elif 'python assistant' in query:
            speak("Are you joking. You're coming in loud and clear.")
        
        elif 'what language you use' in query:
            speak("I am written in Python and I generally speak english.")
        
        elif 'what can you do' in query:
            speak('I am atom version 1 point O your persoanl assistant. I am programmed to minor tasks like searching in youtube, google,open gmail and various platforms ,tell time and date,take a photo,search in wikipedia, predict weather in different cities , get top headline news from times of india, tell about system and can do some automations too and besides it all, I can generate pictures with your imagination with the help of AI!, after this all, I have my friend, nucleus, she is just awesome, I can connect with her too.')
            speak("Just give me commands Master!")
        
        elif 'show me' in query and 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)
        
        elif 'open youtube' in query:
            speak("Here We Go")
            webbrowser.open("youtube.com")
            speak("anything else for which i may assist you")
        
        elif 'youtube' in query and 'search' in query:
            speak("What Should I Search Sir ?")
            search_yt=takeCommand()
            search_yt=search_yt.replace(" ","+")
            speak("Here We Go")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_yt}")
            speak("anything else for which i may assist you")
        
        elif 'open google' in query:
            speak("Here We Go")
            webbrowser.open("google.com")
            speak("anything else for which i may assist you")
        
        elif 'show' in query and 'mails' in query:
            speak("Here We Go")
            webbrowser.open("mail.google.com")
            speak("anything else for which i may assist you")
        
        elif 'open instagram' in query:
            speak("Here We Go")
            webbrowser.open("instagram.com")
            speak("anything else for which i may assist you")
        
        elif 'open facebook' in query:
            speak("Here We Go")
            webbrowser.open("facebook.com")
            speak("anything else for which i may assist you")
        
        elif 'spotify' in query:
            speak("Which song you want to listen to ?")
            songName = takeCommand()
            try:
                os.system("spotify")
                time.sleep(8)
                pyautogui.hotkey("ctrl","l")
                time.sleep(2)
                pyautogui.write(songName, interval=0.1)
                for key in ["enter", 'pagedown', 'tab', 'enter', 'enter']:
                    time.sleep(3)
                    pyautogui.press(key)
                time.sleep(5)
            except:
                speak("Sorry Sir, There is an error")
        
        elif 'open twitter' in query:
            speak("Here We Go")
            webbrowser.open("twitter.com")
            speak("anything else for which i may assist you")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            speak("anything else for which i may assist you")
        
        elif 'the date' in query:
            today=datetime.date.today()
            speak(today)
            speak("anything else for which i may assist you")
        
        elif query == 'atom':
            speak("At Your Service Sir, How can I help you")
        
        elif 'joke' in query:
            URL = 'https://v2.jokeapi.dev/joke/Any'
            response = requests.get(URL)
            data = response.json()
            if response.status_code == 200:
                speak(data['setup'])
                speak(data['delivery'])
            else:
                speak(list_of_jokes[ran_joke])
        
        elif "volume" in query and 'up' in query:
            pyautogui.press("volumeup", presses=5)
            speak("volume upped")
            sleep(1)
            speak("anything else for which i may assist you")
        
        elif "volume" in query and 'down' in query:
            pyautogui.press("volumedown", presses=5)
            speak("volume lowered")
            sleep(1)
            speak("anything else for which i may assist you")  
        
        elif "mute" in query:
            pyautogui.press("volumemute")
            speak("volume muted")
            sleep(1)
            speak("anything else for which i may assist you")
        
        elif "brightness" in query:
            try:
                speak("Which brighness level do you want ?")
                current=sbc.get_brightness()
                bright=int(takeCommand())
                set=sbc.set_brightness(bright)
                speak(f"brightness set to {bright} percent")
                sleep(1)
                speak("anything else for which i may assist you")
            except Exception as e:
                print(e)
                speak("error")
        
        elif 'search' in query:
            query=query.replace("search","")
            query=query.replace(" ","+")
            speak("Here We Go")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak("anything else for which i may assist you")
        
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f'Sir our System still has {percentage} percent battery')
            if percentage >= 75:
                print("\U0001F601")
                speak('Sir we have enough power to continue our work!')
            elif percentage >= 40 and percentage < 75:
                speak(
                    'Sir we should think of connecting our system to the battery supply!')
            elif percentage <= 40 and percentage >= 15:
                speak(
                    "Sir we don't have enough power to work through!... Connect now sir!")
            elif percentage < 15:
                speak(
                    'Sir we have very low power!... Our System may Shutdown anytime soon!...')
        
        elif 'todo' in query or 'to do' in query:
            if 'add' in query or 'create' in query:
                with open('todo.txt','a') as f:
                    todo_w=takeCommand()
                    f.write(f"{todo_w}\n")
                speak("To Do is updated successfully !")                    
            elif 'read' in query or 'tell' in query:
                with open('todo.txt','r') as f:
                    todo_r=f.read()
                    if todo_r =="":
                        todo_r="No Pendning Tasks Sir"
                    speak(todo_r)
            elif 'erase' in query or 'remove all' in query or 'clear' in query:
                with open("todo.txt","w") as f:
                    f.write("")
                speak("All Tasks has been cleared, Sir !")
        
        elif 'pause' in query or 'stop' in query and 'song' in query:
            pyautogui.press("playpause")
            speak("vMusic Paused")
            sleep(1)
            speak("anything else for which i may assist you")
        
        elif 'change' in query and 'song' in query:
            pyautogui.press("nexttrack", presses=1)
            sleep(1)
            speak("anything else for which i may assist you")
        
        elif 'atom quit' in query or 'exit' in query or 'close' in query:
            speak("Thank you for using atom Sir")
            exit()
        
        elif 'note' in query or 'notes' in query:
            speak("What to write on that note?")
            notes=takeCommand()
            with open(f"note.txt",'a') as f:
                    f.write(f"{notes}\n")

            speak("We updated your notes successfully !")
            speak("anything else for which i may assist you")
        
        elif "log off" in query or "sign out" in query:
            speak(
                "Ok , your pc will log off in 10 seconds! make sure you exit from all applications")
            on = 10
            while on !=0:
                speak(on)
                print(on)
                on -= 1

            subprocess.call(["shutdown", "/l"])
                
        elif "weather" in query or 'temperature' in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the name of the city?")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"] - 273.15
                current_temperature = float('%.2f' % current_temperature)
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"Temperature is {current_temperature} degree celcius. Humidity is {current_humidiy} percent. Overall, the weather is {weather_description} today.")
                print(f"Temperature is {current_temperature} degree celcius. Humidity is {current_humidiy} percent. Overall, the weather is {weather_description} today.")
            else:
                speak("Can't find details about this city")
        
        elif "current news" in query or "latest news" in query:
            url = "https://www.indiatoday.in/india"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            # Find all the headlines on the page
            headlines = soup.find_all("h2")
            for headline in headlines[:4]:
                print(headline.text)
                speak(headline.text)    
        
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "atom camera", "img.jpg")
        
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by a Human")
            print("I was built by a Human")
        
        elif 'distance' in query:
            geocoder = Nominatim(user_agent="Singh")
            speak("Tell me the first city name??")
            location1 = takeCommand()
            speak("Tell me the second city name??")
            location2 = takeCommand()
            coordinates1 = geocoder.geocode(location1)
            coordinates2 = geocoder.geocode(location2)
            lat1, long1 = coordinates1.latitude, coordinates1.longitude
            lat2, long2 = coordinates2.latitude, coordinates2.longitude
            place1 = (lat1, long1)
            place2 = (lat2, long2)
            distance_places = distance.distance(place1, place2)
            print(f"The distance between {location1} and {location2} is {distance_places}.")
            speak(f"The distance between {location1} and {location2} is {distance_places}")
        
        elif 'how to' in query:
            try:
                max_results = 1
                data = search_wikihow(query, max_results)
                # assert len(data) == 1
                data[0].print()
                steps = data[0].summary
                speak(data[0].summary)

                speak("should I summarize this for you?")
                ynInput=takeCommand()
                if 'yes' in ynInput.lower():
                    response = co.generate( 
                        model='xlarge', 
                        prompt = steps,
                        max_tokens=40, 
                        temperature=0.8,
                        stop_sequences=["--"])
                    summary = response.generations[0].text
                    print(summary)
                    speak(summary)

            except Exception as e:
                speak('Sorry, I am unable to find the answer for your query.')
        
        elif 'lock' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif "switch the window" in query or "switch window" in query:
            speak("Okay sir, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
        
        elif "system" in query:
            c = wmi.WMI()
            my_system = c.Win32_ComputerSystem()[0]
            print(f"Manufacturer: {my_system.Manufacturer}")
            speak(f"Manufacturer: {my_system.Manufacturer}")
            print(f"Model: {my_system. Model}")
            speak(f"Model: {my_system. Model}")
            print(f"Name: {my_system.Name}")
            speak(f"Name: {my_system.Name}")
            print(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
            speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
            print(f"SystemType: {my_system.SystemType}")
            speak(f"SystemType: {my_system.SystemType}")
            print(f"SystemFamily: {my_system.SystemFamily}")
            speak(f"SystemFamily: {my_system.SystemFamily}")
            ip = requests.get('https://api.ipify.org').text
            print(f"Your ip address is {ip}")
            speak(f"Your ip address is {ip}")

        elif 'summarize' in query:
            speak("Oh, I can summarize texts with cohere AI. Tell me the prompt that I may summarize.")
            prompt = takeCommand()
            response = co.generate( 
                model='xlarge', 
                prompt = prompt,
                max_tokens=40, 
                temperature=0.8,
                stop_sequences=["--"])
            summary = response.generations[0].text
            print(summary)
            speak(summary)

    
        elif 'create image' in query or 'generate image' in query or 'image with ai' in query or 'image with artificial intelligence' in query:
            speak("What kind of photo do you want to generate?")
            imageinfo=takeCommand()
            if imageinfo == "":
                pass
            else:
                speak("just wait a bit! I'm processing it!")
                response = openai.Image.create(prompt=imageinfo,n=1,size="1024x1024")
                image_url=response['data'][0]['url']
                webbrowser.open(image_url)
                speak(f"Here is is!! {imageinfo}")
                print(f"Here is is!! {imageinfo}")

        else:
            api_open=openai.api_key
            if api_open=="":
                speak("API isn't connected Right Now")
                speak("Please Insert API key before you use nucleus")
            else:
                engine1 = pyttsx3.init()
                voices = engine1.getProperty('voices')
                engine1.setProperty('voice', voices[1].id)
                r = srecog.Recognizer()
                mic = srecog.Microphone(device_index=1)
                conversation = ""
                user_name = 'user'
                bot_name = "nucleus"

                if 'exit' in query.lower():
                    break
                else:
                    prompt = user_name + ": " + query + "\n" + bot_name + ": "
                    conversation += prompt 
                    response = openai.Completion.create(
                        engine='text-davinci-003', prompt=conversation, max_tokens=50)
                    response_str = response["choices"][0]["text"].replace(
                        "\n", "")
                    response_str = response_str.split(
                        user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]
                    conversation += response_str + "\n"
                    print(response_str)
                    speak(response_str)
                    engine1.runAndWait()

