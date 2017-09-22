import os.path
import sys
import json
import pprint
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
### input the api.ai client access token id
CLIENT_ACCESS_TOKEN = 'f8d86d6642ca4aa5a78dc5e830bbf7d0'

def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    #request.session_id = "e15aa00a-2ebb-45f1-bbaa-9dc0f14d8e56"
    print('say something ...')
    request.query = raw_input()

    response = json.loads(request.getresponse().read())
    speech = response['result']['fulfillment']['messages'][0]['speech'] 
    f = open('response.txt','w')
    f.write(str(response))
    print (speech)

if __name__ == '__main__':
    main()
