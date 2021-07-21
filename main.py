# $ pip install gTTS
# $ pip install mpyg321

# Import the required module for text
# to speech conversion
from gtts import gTTS

# To play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Good Morning!'

# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file 
myobj.save("greet.mp3")

# Playing the converted file
os.system("mpg321 greet.mp3")
