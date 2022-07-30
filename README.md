# Rice Coding
Rice coding, a specialised form of Golomb coding, is used to encode strings of numbers with a variable bit length for each number. A fairly good compression can be achieved if the numbers are small. Rice coding is generally used to encode entropy in an audio/video codec.

A Golomb-Rice code is a Golomb code where the divisor is a power of two, enabling an efficient implementation using shifts and masks rather than division and modulo.

### How to run
- ```Sounds\Sound1.wav``` is the audio file to be encoded.
- ```rice-coder.py``` contains rice encoder and decoder custom functions.
- ```main.py``` can be run directly to achieve encoding and decoding.
