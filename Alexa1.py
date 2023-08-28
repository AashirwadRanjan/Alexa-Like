import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Thomas. what can i do for you?")       

def takecommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        

    except:  

        print("Say that again Please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aashuranjan09@gmail.com', '9483226839')
    server.sendmail('aashuranjan09.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    	
        query = takecommand().lower()

       
        if "wikipedia" in query:
        	speak('searching wikipedia...')
        	query = query.replace("wikipedia", "")
        	results = wikipedia.summary(query, sentences=2)
        	speak("According to wikipedia")
        	print(results)  

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'please open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'please open google' in query:
            webbrowser.open("google.com")                

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'play music' in query:
            music_dir = 'D:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")   

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'stock market' in query:
            webbrowser.open("tradingview.com")

        elif 'comedk' in query:
            webbrowser.open("comedk.org")
            
        elif 'amazon' in query:
            webbrowser.open("amazon.co.in")

        elif 'flipkart' in query:
            webbrowser.open("flipkart.co.in")

        elif 'discord' in query:
            webbrowser.open("dicord.com")
        
        # genral chat box
            
        elif 'I am sad' in query:
            speak("yes tell me what i can do?")

        elif 'Friends' in query:
            speak("Yes, offcourse")    
            
            
         # chat box contents ends       

        elif 'send email to Raj' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "gameidonly09@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am unable to send Email at this moment.Try Again later.")

        elif 'send mail to Raj' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "gameidonly09@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am unable to send Email at this moment.Try Again later.") 

        elif 'send email to Ranjay' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "kumarranjay09@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am unable to send Email at this moment.Try Again later.")

        elif 'send mail to Ranjay' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "kumarranjay09@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am unable to send Email at this moment.Try Again later.")
            break
        
        elif 'bye bye' in query:
            speak("bye sir")
            quit()
            
        elif 'exit' in query:
            speak("Thank you for your time...Remember me again")
            quit()
       


                              
