import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()


def stream_chat(message, history):
    contents = []
    # History parsing logic remains identical to step 2
    for msg in history:
        role = "model" if msg["role"] == "assistant" else "user"
        text_content = "".join(
            [block["text"] for block in msg["content"] if block["type"] == "text"])
        contents.append(types.Content(role=role, parts=[
                        types.Part.from_text(text=text_content)]))

    contents.append(types.Content(role="user", parts=[
                    types.Part.from_text(text=message)]))

    # Enable streaming in the API call
    response_stream = client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=contents
    )

    partial_message = ""
    for chunk in response_stream:
        if chunk.text is not None:
            partial_message += chunk.text
            # Yielding updates the UI immediately
            yield partial_message


demo = gr.ChatInterface(
    fn=stream_chat,
    title="Streaming Gemini Chatbot"
)

if __name__ == "__main__":
    demo.launch()
