from gtts import gTTS

text = open("C:/python/Udemy-Course/Speech Converter/Demo.txt",'r').read()
language = 'en'
output = gTTS(text=text,lang=language,slow=False)
output.save('C:/python/Udemy-Course/Speech Converter/File_data_to_audio.mp3')