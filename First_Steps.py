#Importing Googletrans Translator (pip install googletrans).
from googletrans import Translator

#Getting needed URL.
translat = Translator()

#Translates from (in this case) German to English.
translat.translate("Der Himmel ist blau und ich mag Bananen", dest='en')

#Printing the translated text.
print(translate.text)
