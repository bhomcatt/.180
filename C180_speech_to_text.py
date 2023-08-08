from tkinter import *
import speech_recognition as sr
root = Tk()
root.geometry("500x500")
def r_audio():
    speech_recognisor= sr.Recognizer()
    with sr.Microphone() as source:
        audio=  speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='es-mx')
        except sr.UnknownValueError:
            print('Por favor, repite. No entendí tu solicitud')
    print(voice_data)
    
r_audio()
root.mainloop()