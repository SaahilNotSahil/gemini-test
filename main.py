import os

import google.generativeai as genai
from dotenv import load_dotenv


def chat(model_name="gemini-pro", generation_config={}, safety_settings=[]):
    model = genai.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    chat = model.start_chat(history=[])

    while True:
        user_msg = input("User: ")

        if user_msg == "ENDCHAT":
            print("\nBye :)")

            break
        
        try:
            response = chat.send_message(user_msg, stream=True)

            print("\nAssistant:", end=" ")

            for chunk in response:
                print(f"{chunk.text}", end="")

            print("\n")
        except Exception as e:
            print(f"\n{e}\n")

            try:
                chat.rewind()
            except Exception:
                pass

if __name__ == "__main__":
    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    
    generation_config = {
        "temperature": 0.9,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        }
    ]

    chat(generation_config=generation_config, safety_settings=safety_settings)

