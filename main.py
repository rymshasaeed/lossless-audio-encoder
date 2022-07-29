import numpy as np
import sounddevice as sd
from scipy.io import wavfile
from rice_coder import rice_encoder, rice_decoder

# Read the audio file to encode
filepath = 'Sounds/Sound1.wav'
sample_rate, audio = wavfile.read(filepath)

# Play original audio
print('Playing original audio...!')
sd.play(audio, sample_rate)

# Encode the audio file and write as .exx2
idx = filepath.find(".wav")
encoded_file = filepath[:idx] + "_Enc.exx2"
M = 4
with open(encoded_file, 'wb') as codedfile:
    for i in range(len(audio)):
        e = rice_encoder(audio[i], M) + '\n'
        codedfile.write(e.encode())
codedfile.close()

# Decode the encoded audio file
decoded_audio = []
with open(encoded_file, 'rb') as codedfile:
    for i in codedfile:
        decoded_audio.append(rice_decoder(i.decode('utf8').strip(), M))
codedfile.close()
decoded_audio = np.array(decoded_audio, dtype='int16')

# Play decoded audio
print('Playing decoded audio...!')
sd.play(decoded_audio, sample_rate)

# Write decoded audio file in .wav format
idx = encoded_file.find(".exx2")
decoded_file = encoded_file[:idx] + "_Dec.wav"
wavfile.write(decoded_file, sample_rate, decoded_audio)
