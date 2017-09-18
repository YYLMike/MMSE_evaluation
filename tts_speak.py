import speech_recognition as sr
def stt():
	# obtain audio from the microphone
	r = sr.Recognizer()
	r.pause_threshold = 0.5
	with sr.Microphone(device_index=5) as source:
		print("Say something!")
		audio = r.listen(source)

	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    spoke = r.recognize_google(audio,language='zh_TW')
	    print(spoke)
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	
	return str(spoke.encode('utf-8'))
spokes = stt()
