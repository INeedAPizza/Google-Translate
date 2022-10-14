#Importing needed libraries
import random
import googletrans
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
from plyer import notification

#Defining translator
translator = Translator()

#Getting list of languages
Lan = googletrans.LANGUAGES
LanKey = list(Lan.keys())

#Text we are translating
text = '''
Pizza angel!
'''
print(text)

#For the while loop, will repeat five times
x = 0
Up = 5

#While loop
while x < Up:
    while True:
        try:
            #Chooses a random language and translates text
            LK = random.choice(LanKey)
            translation = translator.translate(text, dest=LK)
            text = translation.text
            #Un-hashtag if you would like to see the English
            #translationEN = translator.translate(text, dest='en')
            #print(translationEN.text, "\n")
            x += 1
            break
        except:
            None

#When the loop is done        
if x >= Up:
    while True:
        try:
            #Translates to English
            translation = translator.translate(text, dest='en')
            print(translation.text)
            text = translation.text

            #Makes a notification
            note = "Python:"

            message = "Your program is ready!"

            notification.notify(title = note,
                                message = message,
                                app_icon = None,
                                timeout = 10,
                                toast = False)
            break
        except:
            None

#Converts speech to text
tts = gTTS(text)
tts.save("Translate.mp3")

#Plays the resulting audio
os.system("Translate.mp3")
#
