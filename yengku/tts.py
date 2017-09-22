from gtts import gTTS
from pygame import time
from pygame import mixer
import tempfile

def speak(sentence):
        with tempfile.NamedTemporaryFile(delete=True) as fp:
        
                tts = gTTS(text=sentence, lang='zh')
                tts.save('{}.mp3'.format(fp.name))
                #tts.save('hello.mp3')
                mixer.init()
                mixer.music.load('{}.mp3'.format(fp.name))
                mixer.music.play()
                while mixer.music.get_busy():
                        time.Clock().tick(10)

