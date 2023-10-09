import speech_recognition as sr
import pyttsx3
import webbrowser

# Define a dictionary of websites and their corresponding keywords
websites = {
    "Google": "https://www.google.com",
    "YouTube": "https://www.youtube.com",
    "GitHub": "https://www.github.com",
    "Leetcode": "https://www.leetcode.com",
    "chat gpt" : "https://chat.openai.com",
    "neet code" : "https://neetcode.io",
    # Add more websites and keywords as needed
}

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    sr_engine = sr.Recognizer()

    with sr.Microphone() as source:
        print("Silence please...")
        sr_engine.adjust_for_ambient_noise(source, duration=2)
        print("Speak now please...")

        audio = sr_engine.listen(source)

        try:
            text = sr_engine.recognize_google(audio)
            text = text.lower()
            print("Did you say: " + text)

            # Check if the recognized text matches a website keyword
            for keyword, url in websites.items():
                if keyword.lower() in text:
                    print("Opening " + keyword)
                    speak("Opening " + keyword)
                    webbrowser.open(url)
                    break  # Exit the loop if a match is found

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print("Error making the request to Google Speech Recognition: {0}".format(e))
            speak("Sorry, there was an error with the speech recognition service.")
        except Exception as e:
            print("Error: {0}".format(e))
            speak("Sorry, there was an error processing your request.")
