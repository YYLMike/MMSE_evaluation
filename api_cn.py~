#!/usr/bin/python
#coding:utf-8
import os.path
import sys
import json
import uniout
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

### input the api.ai client access token id
CLIENT_ACCESS_TOKEN = '4e32bfebb8f9405d9e937070af8b52ec'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

def main():
    question_list = []
    f = open('MMSE_table.txt','r')
    tmp_str = f.read()
    question_list = tmp_str.split('\n')
    f.close()
    f = open('response.txt','w') #user answer
    for i in range(len(question_list)-1):
	    request = ai.text_request()
	    request.lang = 'cn'  # optional, default value equal 'en'
	    #request.session_id = "e15aa00a-2ebb-45f1-bbaa-9dc0f14d8e56"
	    print(question_list[i])
	    user_ans = raw_input()
	    request.query = question_list[i]
	    response = json.loads(request.getresponse().read())
	    speech = response['result']['fulfillment']['messages'][0]['speech'] 
	    f.write(user_ans+'\n')
	    print (speech)
	    #if(speech.encode('utf-8')=='再見' or speech.encode('utf-8')=='掰掰'):
	    #	print('下次見')
	    #	break

    f.close()
if __name__ == '__main__':
    main()
