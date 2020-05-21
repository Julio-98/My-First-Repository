#This class is about SPEECH RECOGNITION#Some packages that can be used to 
#speech recognition:
#   apiai
#   assemblyai
#   Google-cloud-speech
#   SpeechRecognition - WILL BE USED IS THIS TUTORIAL
#   Pocketsphinx
#   Watson-developer-cloud
#   wit

#On therminal I should run pip3 install speechrecognition
import speech_recognition as sr

#In order to work with microphone we should run in therminal $pip3 install pyaudio
#I have troubles trying to install pyaudio, so I should
#run $sudo apt-get install portaudio19-dev and than run pip again

import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with Sr.microphone() as source:
    print('[search edureka: search youtube]')
    print('speak now')
    audio = r3.listen(source)

    if 'edureka' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = 'https://www.edureka.co/'
        with sr.Microphone as source:
            print('search your query')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)

            except sr.UnknowValueError:
                print('Error')
            except sr.RequestError as e:
                print('failed'.format(e))
