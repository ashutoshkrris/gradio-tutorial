import os
import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from the .env file
load_dotenv()

# Initialize the Gemini client (it automatically picks up the GEMINI_API_KEY env variable)
client = genai.Client()


def chat_with_ai(user_message, history):
    contents = []

    # Map Gradio 6's dictionary format into Gemini's Content format
    for msg in history:
        # Map Gradio's 'assistant' role to Gemini's 'model' role
        role = "model" if msg["role"] == "assistant" else "user"

        # Extract the actual text from Gradio's content blocks
        text_content = "".join(
            [block["text"] for block in msg["content"] if block["type"] == "text"])

        contents.append(types.Content(role=role, parts=[
                        types.Part.from_text(text=text_content)]))

    # Append the current user message
    contents.append(types.Content(role="user", parts=[
                    types.Part.from_text(text=user_message)]))

    # Configure system instructions
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful engineering assistant."
    )

    # Call the free-tier Gemini model
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=contents,
        config=config
    )

    return response.text


# Create the Chat Interface
demo = gr.ChatInterface(
    fn=chat_with_ai,
    title="Gemini Engineering Assistant",
    description="Ask me anything about Python or system design."
)

if __name__ == "__main__":
    demo.launch()
