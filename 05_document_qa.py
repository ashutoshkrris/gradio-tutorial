import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()


def analyze_document(file_obj, user_question):
    # Prevent crashing if the user clicks Ask without a file
    if file_obj is None:
        return "Please upload a text file first."

    # Read the file text
    with open(file_obj.name, "r", encoding="utf-8") as f:
        file_content = f.read()

    # Inject the file contents directly into the system prompt
    config = types.GenerateContentConfig(
        system_instruction=f"Use this document context to answer questions:\n\n{file_content}"
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user_question,
        config=config
    )

    return response.text


with gr.Blocks() as demo:
    gr.Markdown("# Document Q&A App")

    with gr.Row():
        file_input = gr.File(label="Upload a .txt file")
        question_input = gr.Textbox(label="Ask a question about the file")

    submit_btn = gr.Button("Ask")

    gr.Markdown("### AI Answer")
    # Using gr.Markdown allows Gemini's bold text, lists, and code blocks to render beautifully
    output_markdown = gr.Markdown(value="Your answer will appear here...")

    submit_btn.click(
        fn=analyze_document,
        inputs=[file_input, question_input],
        outputs=output_markdown  # Send the result straight to the Markdown component
    )

if __name__ == "__main__":
    demo.launch()
