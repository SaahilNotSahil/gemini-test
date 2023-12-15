import os

import google.generativeai as genai
from dotenv import load_dotenv


def chat(model="gemini-pro"):
    model = genai.GenerativeModel(model)
    chat = model.start_chat(history=[])

    while True:
        user_msg = input("User: ")

        if user_msg == "ENDCHAT":
            print("\nBye :)")

            break

        response = chat.send_message(user_msg, stream=True)
        
        print("\nAssistant:", end=" ")

        for chunk in response:
            print(f"{chunk.text}", end="")

        print("\n")


if __name__ == "__main__":
    load_dotenv()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    
    chat()

