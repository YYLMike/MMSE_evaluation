import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'c45478c1cf9a4f9d81fa0739e55e4fdf' 


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'en'  # optional, default value equal 'en'

    request.session_id = "e15aa00a-2ebb-45f1-bbaa-9dc0f14d8e56"

    request.query = "give me a song"

    response = request.getresponse()
    f = open('response.txt','w')
    f.write(str(response.read()))
    #print (response.read())
    print ('Work.')

if __name__ == '__main__':
    main()
