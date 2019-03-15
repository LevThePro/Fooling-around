from sys import byteorder
from array import array
from struct import pack
import speech_recognition as sr
import pyaudio
import wave
import pygame
import time

pygame.init()
pygame.mixer.music.load("sound.wav") #load in desired sound

while True:
    r = sr.Recognizer()
    ricky = sr.AudioFile('D:\\Py\\asdf\\demo.wav') #COMPUTER SPECIFIC CHANGE ME
    with ricky as source:
        audio = r.record(source)
    try:
        string = str(r.recognize_google(audio)) 
        if "poop" in string: #edit the trigger word
            pygame.mixer.music.play()
            time.sleep(10) #enter the length of the sound
    except sr.UnknownValueError:
        print("No sound was captured")
