import speech_recognition as sr
import traceback


def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("🎤 Sun raha hoon...")

        r.energy_threshold = 300
        r.pause_threshold = 1

        r.adjust_for_ambient_noise(source, duration=0.5)

        try:

            audio = r.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

            try:
                text = r.recognize_google(audio, language="en-IN")

            except sr.UnknownValueError:
                try:
                    text = r.recognize_google(audio, language="hi-IN")
                except sr.UnknownValueError:
                    print("❌ Voice samajh nahi aayi.")
                    return ""

            except sr.RequestError:
                print("❌ Google Speech service unavailable.")
                return ""

            print("Aap:", text)
            return text.lower()

        except sr.WaitTimeoutError:
            print("⏰ Koi voice nahi mili.")
            return ""

        except Exception as e:
            print("=" * 50)
            print("VOICE ERROR")
            print(type(e).__name__)
            print(str(e))
            traceback.print_exc()
            print("=" * 50)
            return ""