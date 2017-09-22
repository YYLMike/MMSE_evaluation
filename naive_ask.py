#!/usr/bin/python
#coding:utf-8
import speech_to_text as stt
import tts
def main():
	question_list = []
	f = open('MMSE_table.txt', 'r')
	tmp_str = f.read()
	question_list = tmp_str.split('\n')	
	f.close()
	f = open('user_answer.txt','w')
	
	for i in range(len(question_list)-1):
		tts.speak(question_list[i])
		print('請回答：')
		while True:		
			user_ans = stt.stt()
			if(user_ans != "error"):
				f.write(user_ans+'\n')
				break
if __name__ == '__main__':
    main()
