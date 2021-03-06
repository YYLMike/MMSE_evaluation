import speech_recognition as sr
def stt():
	# obtain audio from the microphone
	r = sr.Recognizer()
	m = sr.Microphone()	
	r.pause_threshold = 0.6
	with m as source:
		r.adjust_for_ambient_noise(source)
		#print("Say something!")
		audio = r.listen(source)
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    spoke = r.recognize_google(audio,language='zh_TW')
	    print(spoke)
	    return str(spoke.encode('utf-8'))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	    return "error"
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	    return "error"
	
	

