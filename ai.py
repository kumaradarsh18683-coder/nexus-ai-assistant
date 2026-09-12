import asyncio
import edge_tts
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import uuid

VOICE = "en-IN-NeerjaNeural"




async def speak_async(text):
    print("Nexus AI:", text)

    filename = f"{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(
    text=text,
    voice=VOICE,
    rate="+5%",
    pitch="-2Hz")


    await communicate.save(filename)

    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()

    if os.path.exists(filename):
        os.remove(filename)


def speak(text):
    asyncio.run(speak_async(text))

   
def greet():
    speak("Hello Adarsh. Nexus AI is online.")
    speak("How can I help you today?")

if __name__ == "__main__":
    greet()