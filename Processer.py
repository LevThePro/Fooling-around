from sys import byteorder
from array import array
from struct import pack
import speech_recognition as sr
import pyaudio
import wave

r = sr.Recognizer()
ricky = sr.AudioFile('D:\\Py\\asdf\\demo.wav') #COMPUTER SPECIFIC CHANGE ME
with ricky as source:
    audio = r.record(source)
try:
    print(r.recognize_google(audio)) 
except sr.UnknownValueError:
    print("No sound was captured")
