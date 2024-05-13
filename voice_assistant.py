import speech_recognition as sr
import pyttsx3
import datetime
import requests
import smtplib
import pywhatkit
from bs4 import BeautifulSoup
import webbrowser
import tkinter as tk
from tkinter import ttk

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("User:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't get that.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm having trouble accessing the speech recognition service.")
            return ""
                
def send_email(subject, body, to_email):
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = ''
    sender_password = ''
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, to_email, f"Subject: {subject}\n\n{body}")
    server.quit()

def get_weather(city):
    api_key = '0976d90cc30c21877e4f2497354bc822'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    return f"The weather in {city} is {weather_desc} with a temperature of {temp}°C."

def send_whatsapp_message(phone_number, message):
    if not phone_number.startswith("+"):
        speak("Please provide the country code with the phone number.")
        country_code = take_command()
        phone_number = f"+{country_code}{phone_number}"
    pywhatkit.sendwhatmsg(phone_number, message, datetime.datetime.now().hour, datetime.datetime.now().minute + 1)
    
def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    answer_divs = soup.find_all("div", {"class": "Z0LcW"})
    if answer_divs:
        return answer_divs[0].text
    else:
        return "Sorry, I couldn't find an answer to that question."

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = take_command()
        if "send email" in command:
            speak("What is the subject of the email?")
            subject = take_command()
            speak("What should be the content of the email?")
            body = take_command()
            speak("Who is the recipient?")
            recipient = take_command()
            send_email(subject, body, recipient)
            speak("Email has been sent successfully.")

        elif "weather" in command:
            speak("Sure, which city's weather do you want to know?")
            city = take_command()
            weather = get_weather(city)
            speak(weather)
            
        elif "send whatsapp message" in command:
            speak("Sure, please specify the phone number.")
            phone_number = take_command()
            speak("What message do you want to send?")
            message = take_command()
            send_whatsapp_message(phone_number, message)
            speak("WhatsApp message has been sent successfully.")
        
        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)
            
        elif "exit" in command:
            speak("Goodbye Fardeen!")
            break
        
        else:
            answer = google_search(command)
            speak(answer)
            
if __name__ == "__main__":
    main()
