import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import pyaudio

print("PyAudio is installed and working!")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get user input from microphone
def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting.")
    return ""

# Main function to greet and respond
def greet_user():
    speak("Hello, Andrew. How are you?")
    user_response = input("How was your day? Type your response: ").lower()

    if "fine" in user_response or "good" in user_response or "positive" in user_response:
        speak("Welcome on board, let's do some coding.")
    elif "bad" in user_response:
        speak("All will be well. Playing your favorite song to cheer you up.")


    # Play your favorite song
    speak("Playing your favorite song.")
    webbrowser.open("https://www.youtube.com/watch?v=Vpo3StUe5Ko&pp=ygULbWFtYmlhIHlhbmU%3D")  # Replace with your song link
    time.sleep(1000)  # Wait for song to play for a bit before speaking again

    # Encouragement after song
    speak("Let's go on with coding. It's a cool stuff; you don't want to miss out!")

# Run the greeting function
if __name__ == "__main__":
    greet_user()
