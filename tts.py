import pyttsx3

# Create an instance of the text-to-speech engine
engine = pyttsx3.init()

myinput = input("What do you want to do with our tts service: ")

# Call the 'say' method on the engine instance
engine.say(myinput)

# Run and wait for the speech to complete
engine.runAndWait()
