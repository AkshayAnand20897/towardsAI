
import webbrowser
import string
import speech_recognition as sr

import pyttsx

# obtain audio from computer 
r = sr.Recognizer()

#r.energy_threashold=some_value

with sr.Microphone() as source:
    print("Hello, what can i help you find?[Player lookup,Weather,resturants, or just to search the web: ]")
    k = pyttsx.init()
    k.say("Hello, what can i help you find?[Player lookup,Weather,resturants, or just to search the web: ]")
    k.runAndWait()
    audio = r.listen(source)
    

if "player" in r.recognize_google(audio):
    # obtain audio from the microphone
    r2 = sr.Recognizer()
    url = 'https://en.wikipedia.org/wiki/'
    with sr.Microphone() as source:
        print("Say any sports players name to see there Bio: ")
        k = pyttsx.init()
        k.say('Say any sports players name to see there Bio: ')
        k.runAndWait()

        audio2 = r2.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r2.recognize_google(audio2))
            
            k = pyttsx.init()
            k.say("Google Speech Recognition thinks you said " + r2.recognize_google(audio2))
            k.runAndWait()
            webbrowser.open_new(url+r2.recognize_google(audio2))
            
        except sr.UnknownValueError:
            #if can't find the audio
            print("Google Speech Recognition could not understand audio")
            k = pyttsx.init()
            k.say("Google Speech Recognition could not understand audio")
            k.runAndWait()
        except sr.RequestError as e:
            #when not connect to internet
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            k = pyttsx.init()
            k.say("Could not request results from Google Speech Recognition service; {0}")
            k.runAndWait()


if "weather" in r.recognize_google(audio):
    # obtain audio from the microphone
    r3 = sr.Recognizer()
    url3 = 'https://www.accuweather.com/en/world-weather'
    with sr.Microphone() as source:
        print("Please say a city and state: ")
        k = pyttsx.init()
        k.say('Please say a city and state:')
        k.runAndWait()

        
        audio3 = r3.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r3.recognize_google(audio3))
            
            k = pyttsx.init()
            k.say("Google Speech Recognition thinks you said " + r3.recognize_google(audio3))
            k.runAndWait()
            webbrowser.open_new(url3+r3.recognize_google(audio3))
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            k = pyttsx.init()
            k.say("Google Speech Recognition could not understand audio")
            k.runAndWait()
        except sr.RequestError as e:
            
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            k = pyttsx.init()
            k.say("Could not request results from Google Speech Recognition service; {0}")
            k.runAndWait()


if "restaurants" in r.recognize_google(audio):
    # obtain audio from the microphone
    r4 = sr.Recognizer()
    url4 = 'https://www.yelp.com/search?cflt=restaurants&find_loc='
    with sr.Microphone() as source:
        print("Please state a location to search for restaurants: ")
        k = pyttsx.init()
        k.say('Please state a location to search for restaurants:')
        k.runAndWait()

        
        audio4 = r4.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r4.recognize_google(audio4))
            
            k = pyttsx.init()
            k.say("Google Speech Recognition thinks you said " + r4.recognize_google(audio4))
            k.runAndWait()
            webbrowser.open_new(url4+r4.recognize_google(audio4))
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            k = pyttsx.init()
            k.say("Google Speech Recognition could not understand audio")
            k.runAndWait()
        except sr.RequestError as e:
            
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            k = pyttsx.init()
            k.say("Could not request results from Google Speech Recognition service; {0}")
            k.runAndWait()

if "search" in r.recognize_google(audio):
    # obtain audio from the microphone
    r5 = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("what website would you like me to search for you? ")
        k = pyttsx.init()
        k.say('what website would you like me to search for you? ')
        k.runAndWait()
        audio5 = r5.listen(source)
        url5= r5.recognize_google(audio5)

        try:
            print("Google Speech Recognition thinks you said " + r5.recognize_google(audio5))
            
            k = pyttsx.init()
            k.say("Google Speech Recognition thinks you said " + r5.recognize_google(audio5))
            k.runAndWait()
            webbrowser.open_new(url5)
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            k = pyttsx.init()
            k.say("Google Speech Recognition could not understand audio")
            k.runAndWait()
        except sr.RequestError as e:
            
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            k = pyttsx.init()
            k.say("Could not request results from Google Speech Recognition service; {0}")
            k.runAndWait()
