import pyttsx3
# initailize the text-to-speech engine
engine = pyttsx3.init()

#set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#your birthday message
message = "happy birthay muskan! May your life is filled with happiness"
engine.say(message)
engine.runAndWait()
