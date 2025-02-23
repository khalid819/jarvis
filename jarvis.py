import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import datetime
import wikipedia
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="your news api key"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour>12:
        speak("good morning !")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
speak("initializing jarvis.......")
wish()
op=input("optins[writing/speaking]: ")
if op=="speaking":
    def processcommand(c):
        if "open" in c.lower():
            d=c.lower().split(" ")[1]
            speak(f"opening {d}")
            webbrowser.open(f"https:\\{d}.com")
        elif "search" in c.lower():
            s=c.lower().split(" ")[1]
            speak(f"search results for {s}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={s}")
        elif "news" in c.lower():
            r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data['articles']
                for article in articles:
                    speak(article['title'])
        elif "what is" and "who is" in c.lower():
                j=c.lower().split(" ")[2]
                speak(f"summury about {j}")
                try:
                    summary = wikipedia.summary(j, sentences=5)
                    speak(summary)  
                    print(summary)
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"Disambiguation error: {e.options}")
                except wikipedia.exceptions.HTTPTimeoutError:
                    print("Request timed out. Please try again.")
                except wikipedia.exceptions.RedirectError:
                    print("Redirect error occurred.")
                except wikipedia.exceptions.PageError:
                    print(f"Page not found for {j}.")
                except Exception as e:
                    print(f"An error occurred: {e}")
        elif "time now" in c.lower():
            strf=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strf}")
            print(strf)
        elif "send email" in c.lower():
            a=input("to: ")
            b=input("subject: ")
            o=input("body: ")
            def send_email(sender_email, sender_password, recipient_email, subject, body):
                try:
                   message = MIMEMultipart()
                   message["From"] = sender_email
                   message["To"] = recipient_email
                   message["Subject"] = subject
                   message.attach(MIMEText(body, "plain"))
                   with smtplib.SMTP("smtp.gmail.com", 587) as server:
                     server.starttls()  
                     server.login(sender_email, sender_password)
                     server.sendmail(sender_email, recipient_email, message.as_string())
                     print("Email sent successfully!")
                except Exception as e:
                 print(f"Failed to send email: {e}")
                 if __name__=="__main__":
                     sender_email ="your email address"
                     sender_password = "your password"  
                     recipient_email = a
                     subject =b
                     body = o
                     send_email(sender_email, sender_password, recipient_email, subject, body)
        elif"wether"in c:                
                def get_weather(city, api_key):
                    base_url = "http://api.openweathermap.org/data/2.5/weather"
                    params = {
                        "q": city,
                        "appid": api_key,
                        "units": "metric"  # Use 'imperial' for Fahrenheit
                    }
                    try:
                        response = requests.get(base_url, params=params)
                        response.raise_for_status()
                        data = response.json()
                        weather = data["weather"][0]["description"]
                        temp = data["main"]["temp"]
                        feels_like = data["main"]["feels_like"]
                        humidity = data["main"]["humidity"]
                        wind_speed = data["wind"]["speed"]
                        print(f"Weather in {city}: {weather.capitalize()}")
                        print(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
                        print(f"Humidity: {humidity}%")
                        print(f"Wind Speed: {wind_speed} m/s")
                        speak(f"Weather in {city}: {weather.capitalize()}")
                        speak(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
                        speak(f"Humidity: {humidity}%")
                        speak(f"Wind Speed: {wind_speed} m/s")
                    except requests.exceptions.HTTPError as http_err:
                        print(f"HTTP error occurred: {http_err}")
                    except Exception as err:
                        print(f"An error occurred: {err}")
                api_key = "your open wether api key"
                city = input("Enter the city name: ")
                get_weather(city, api_key)
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listenig......")
                audio = r.listen(source,timeout=5,phrase_time_limit=2)
            print("recognizing.....")
            try:
                with sr.Microphone() as source:
                    print("listenig..............")
                    audio = r.listen(source,timeout=5,phrase_time_limit=5)
                word=r.recognize_google(audio)
                if(word.lower()=="jarvis"):
                    speak("ya")
                with sr.Microphone() as source:
                    print("activating jarvice......")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processcommand(command)
            except Exception as e:
                print("error; {0}".format(e))
elif op=="writing":
    while True:
            def processcommand(c):
             if "open" in c:
                d=c.split(" ")[1]
                speak(f"opening {d}")
                webbrowser.open(f"https:\\{d}.com")
             elif "search" in c:
                s=c.split(" ")[1]
                speak(f"search results for {s}")
                webbrowser.open(f"https://www.youtube.com/results?search_query={s}")
             elif "news" in c:
                r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
                if r.status_code == 200:
                    data = r.json()
                    articles = data['articles']
                    for article in articles:
                        print(article["title"])
                        speak(article['title'])
             elif "time now" in c:
                strf=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strf}")
                print(strf)
             elif "send email" in c:
                a=input("to: ")
                b=input("subject: ")
                o=input("body: ")
                def send_email(sender_email, sender_password, recipient_email, subject, body):
                 try:
                     message = MIMEMultipart()
                     message["From"] = sender_email
                     message["To"] = recipient_email
                     message["Subject"] = subject
                     message.attach(MIMEText(body, "plain"))
                     with smtplib.SMTP("smtp.gmail.com", 587) as server:
                         server.starttls()  # Encrypt the connection
                         server.login(sender_email, sender_password)
                         server.sendmail(sender_email, recipient_email, message.as_string())
                     speak("Email sent successfully!")
                     print("Email sent successfully!")
                 except Exception as e:
                     print(f"Failed to send email: {e}")
                 if __name__ == "__main__":
                    sender_email = "your email address"
                    sender_password = "your password"  # Use an app password if using Gmail
                    recipient_email = a
                    subject = b
                    body = o
                    send_email(sender_email, sender_password, recipient_email, subject, body,)
             elif"wether"in c:                
                def get_weather(city, api_key):
                    base_url = "http://api.openweathermap.org/data/2.5/weather"
                    params = {
                        "q": city,
                        "appid": api_key,
                        "units": "metric"  
                    }
                    try:
                        response = requests.get(base_url, params=params)
                        response.raise_for_status()
                        data = response.json()
                        weather = data["weather"][0]["description"]
                        temp = data["main"]["temp"]
                        feels_like = data["main"]["feels_like"]
                        humidity = data["main"]["humidity"]
                        wind_speed = data["wind"]["speed"]
                        print(f"Weather in {city}: {weather.capitalize()}")
                        print(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
                        print(f"Humidity: {humidity}%")
                        print(f"Wind Speed: {wind_speed} m/s")
                        speak(f"Weather in {city}: {weather.capitalize()}")
                        speak(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
                        speak(f"Humidity: {humidity}%")
                        speak(f"Wind Speed: {wind_speed} m/s")
                    except requests.exceptions.HTTPError as http_err:
                        print(f"HTTP error occurred: {http_err}")
                    except Exception as err:
                        print(f"An error occurred: {err}")
                api_key = "your openwether api key"
                city = input("Enter the city name: ")
                get_weather(city, api_key)
             elif "what is" or "who is" in c:
                j=c.split(" ")[2]
                speak("acording to wikipedia ")
                try:
                    summary = wikipedia.summary(j, sentences=5)
                    print(summary)
                    speak(summary)  
                except wikipedia.exceptions.DisambiguationError as e:
                    print(f"Disambiguation error: {e.options}")
                except wikipedia.exceptions.HTTPTimeoutError:
                    print("Request timed out. Please try again.")
                except wikipedia.exceptions.RedirectError:
                    print("Redirect error occurred.")
                except wikipedia.exceptions.PageError:
                    print(f"Page not found for {j}.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            c=input(": ")
            processcommand(c)
