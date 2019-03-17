from sys import byteorder
from array import array
from struct import pack


import speech_recognition as sr
import pyaudio
import wave



while True:
    THRESHOLD = 500
    CHUNK_SIZE = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    RECORD_SECONDS = 5
    

    def normalize(snd_data):
        "Average the volume out"
        MAXIMUM = 16384
        times = float(MAXIMUM)/max(abs(i) for i in snd_data)

        r = array('h')
        for i in snd_data:
            r.append(int(i*times))
        return r

   
    def record():
        """
        Record a word or words from the microphone and 
        return the data as an array of signed shorts.
        Normalizes the audio, trims silence from the 
        start and end, and pads with 0.5 seconds of 
        blank sound to make sure VLC et al can play 
        it without getting chopped off.
        """
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=1, rate=RATE,
            input=True, output=True,
            frames_per_buffer=CHUNK_SIZE)

        r = array('h')

        for i in range(0, int(RATE / CHUNK_SIZE * RECORD_SECONDS)):
            # little endian, signed short
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big':
                snd_data.byteswap()
            r.extend(snd_data)

          

        sample_width = p.get_sample_size(FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        r = normalize(r)
        return sample_width, r

    def record_to_file(path):
        "Records from the microphone and outputs the resulting data to 'path'"
        sample_width, data = record()
        data = pack('<' + ('h'*len(data)), *data)

        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()

    if __name__ == '__main__':
        print("Recording...")
        record_to_file('demo.wav')
        print("Done... Processing...")

