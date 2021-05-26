import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import googlesearch as google
import pyttsx3

# Ignore any warning massages
warnings.filterwarnings('ignore')


# #speech engine
# # initialisation
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# # print(voices[1].id)


#Record audio ad return it as string
def recordAudio():

    #Record the audio
    r = sr.Recognizer() # creating a recognizer object

    #Open the microphone and start recording
    with sr.Microphone() as source:
        print('Say something ..')
        audio = r.listen(source)

    # Use google speech recognition
    data = ''

    try:
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValueError: # check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request result form google recognition service error '+ e)

    return data


def assitantResponse(text):
    print(text)

    #Convert the text to speech
    myobj = gTTS(text=text,lang='en',slow=False)

    #Save teh converted audio to a file
    myobj.save('assistant_response.mp3')

    #Play the converted file
    os.system('start assistant_response.mp3')


    #
    # # testing
    # engine.say(text)


# A function for wake word(s) or phrase
def wakeWord(text):
    WAKE_WORDS = ['hey computer','okey computer','computer'] # A list of wake words

    text = text.lower() # converting the all text to lower case words

    # Check to see if the user command/text contains a wake word /phrase

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    # If the wake word isn't fount in the text from the loop and so it return false
    return False

# A fuction to get the current date
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()] # e.g. Friday
    monthNum = now.day
    dayNum = now.day

    # A list of mounths
    month_names = ['January','February','March','April','May','June','July','August',
                   'October','November','December']

    # A list of original numbers
    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                       '11th','12th','13th','14th','15th','16th','17th','18th','19th',
                       '20th','21st','22nd','23rd','24th','25th','26th','27th','28th',
                       '29th','30th','31th']



    return  'Today is '+weekday+' '+month_names[monthNum - 1]+' the '+ordinalNumbers[dayNum -1]+'.'


# A function to return a random greeting response
def greeting(text):

    # Greeting inputs
    GEETING_INPUTS = ['hi','hey','halo','greetings','wassup','hello']

    # Greeting responses
    GEETING_RESPONSES = ['howdy','whats good','hello', 'hey there']

    # If the users input is a greeting, then return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GEETING_INPUTS:
            return random.choice(GEETING_RESPONSES) +' -'

    # If no greeting was detected then return an empty string
    return ''

# A function to get a persons first and last name from the text
def getPerson(text):

    wordList = text.split() # Splitting the text into a list of words

    for i in range(0,len(wordList)):
        if i+3 <= len(wordList) -1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2]+' '+wordList[i+3]
def getDefinition(text):

    wordList = text.split() # Splitting the text into a list of words

    for i in range(0,len(wordList)):
        if i+3 <= len(wordList) -1 and wordList[i].lower() == 'what' and wordList[i+1].lower() == 'is':
            return wordList[i+2]+' '+wordList[i+3]



while True:

    # Record the audio
    text = recordAudio()
    responses = ''

    # Check for the wake word/phrase
    if(wakeWord(text)==True):
        print("Iam wake....")
        #Check for greeting by ther user
        responses = responses + greeting(text)

        #Check to see if the user said anything having to do with the date
        if('date' in text):
            get_date = getDate()
            responses = responses + ' ' +get_date

        #Check tto see if the user is said anything having to do with time
        if('time' in text):
            now = datetime.datetime.now()
            meridien = ''
            if now.hour >=12:
                meridien = 'p.m' # Post Meridien (PM) after midday
                hour = now.hour - 12
            else:
                meridien = 'a.m' # Ante Meridian (Am) before midday
                hour = now.hour

            #Coverting minute into proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)

            responses = responses + ' '+ 'It is '+str(hour)+':'+minute+' '+meridien+ ' .'

        #Check to see if the user said 'who is'
        if('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person,sentences=2)
            responses = responses+ ' ' + wiki

        # Check to see if the user said 'who is'
        if ('what is' in text):
            define = getDefinition(text)
            g = google.search(text)
            print(g)
            wiki = wikipedia.summary(define, sentences=2)
            responses = responses + ' ' + wiki

        #Have the assitant respond back using audio and the text from response
        if responses != '':

            assitantResponse(responses)
    else:
        continue






