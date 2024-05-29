from gtts import gTTS
import os

text = 'Lol I am going to Wonderla'
output = gTTS(text=text,lang='en', tld='co.uk',slow=False)
output.save('C:/python/Udemy-Course/Speech Converter/Audio_from_text.mp3')

# os.system('start Audio_from_text.mp3')