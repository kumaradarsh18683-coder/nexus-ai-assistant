import speech_recognition as sr


def wait_for_wake_word():

    r = sr.Recognizer()

    while True:

        with sr.Microphone() as source:

            print("👂 Waiting for 'Nexus'...")

            r.adjust_for_ambient_noise(source, duration=0.5)

            try:

                audio = r.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

                text = r.recognize_google(audio).lower()

                print("Heard:", text)

                if "nexus" in text:
                    print("✅ Wake Word Detected")
                    return

            except:
                pass