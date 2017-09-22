#!/usr/bin/python
#coding:utf-8
from gtts import gTTS
from pygame import time
from pygame import mixer
import tempfile
import speech_to_text as stt
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
def main():
	question_list = []
	f = open('MMSE_table.txt', 'r')
	tmp_str = f.read()
	question_list = tmp_str.split('\n')	
	f.close()
	f = open('user_answer.txt','w')
	
	for i in range(len(question_list)-1):
		speak(question_list[i])
		print('請回答：')		
		user_ans = stt.stt()#replace to speech later
		f.write(user_ans+'\n')
if __name__ == '__main__':
    main()
