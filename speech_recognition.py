import speech_recognition as sr

# Set the language to Brazilian Portuguese
language = "pt-BR"

# Initialize the recognizer
r = sr.Recognizer()

# Set the audio source
with sr.Microphone() as source:
    # Adjust the recognizer sensitivity
    r.adjust_for_ambient_noise(source)
    # Record audio
    audio = r.listen(source)

# Recognize the speech
try:
    # Print the transcript of the audio
    print(r.recognize_google(audio, language=language))
except sr.UnknownValueError:
    # If the audio is not recognized, print an error message
    print("Could not understand the audio")
except sr.RequestError as e:
    # If there is an error with the request, print an error message
    print("Error with the request: {0}".format(e))
