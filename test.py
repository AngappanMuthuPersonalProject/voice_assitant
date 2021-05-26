import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

print(sr.Microphone.list_microphone_names())

mic = 0

with sr.Microphone(mic) as source:
    print('Speak now')
    audio = r3.listen(source)



    if 'hi' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = ''
        with sr.Microphone(mic) as source:
            print('Search your qurey')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.open_new(url+get)
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError as e:
                print('failed'.format(e))


