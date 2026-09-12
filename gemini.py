import os
from dotenv import load_dotenv
from google import genai
from PIL import Image


load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(question):
    
    try:
        response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
Tum Nexus AI ho.
Hamesha simple Hinglish me jawab do.
Agar user English me puche tab bhi Hinglish me jawab do.
Jawab chhota aur natural rakho.

User: {question}
"""
)
        
        return response.text
    except Exception as e:
        print("Gemini Error:", e)
        return "Maaf kijiye, Gemini se jawab nahi mil paaya."

def ask_gemini_image(image_path, question):

    try:
        
        print("1. Opening image...")

        image = Image.open(image_path)
        
        print("2. Sending to Gemini...")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                image,
                f"""
Tum Nexus AI ho.

Hamesha simple Hinglish me jawab do.

User ka question:
{question}
"""
            ]
        )

        print("3. Response received!")

        return response.text

    except Exception as e:
        print("Vision Error:", e)
        return "Screen ko analyze nahi kar paaya."