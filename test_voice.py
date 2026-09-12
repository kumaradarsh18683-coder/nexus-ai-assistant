import speech_recognition as sr

MIC_INDEX = 1

r = sr.Recognizer()
r.dynamic_energy_threshold = False
r.energy_threshold = 100

print("================================")
print("NEXUS MICROPHONE TEST")
print("================================")
print("Mic index:", MIC_INDEX)

with sr.Microphone(device_index=MIC_INDEX) as source:
    print("Microphone opened.")
    print("Ab 5 seconds tak normally bolo...")
    
    audio = r.record(source, duration=5)

print("Audio recording complete.")
print("Audio bytes:", len(audio.frame_data))

try:
    text = r.recognize_google(audio, language="en-IN")
    print("Recognized:", text)
except sr.UnknownValueError:
    print("Audio mila, lekin speech recognize nahi hui.")
except sr.RequestError as e:
    print("Google Speech error:", e)
except Exception as e:
    print("ERROR:", type(e).__name__, e)