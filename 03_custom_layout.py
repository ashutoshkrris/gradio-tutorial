import gradio as gr


def respond(message, history):
    # Dummy logic for demonstration
    return f"I received your message: {message}"


with gr.Blocks() as demo:
    gr.Markdown("# Custom Chatbot Layout")

    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(height=400)
            msg = gr.Textbox(placeholder="Type a message and press Enter...")

        with gr.Column(scale=1):
            clear_btn = gr.Button("Clear Chat")
            settings = gr.Markdown("### Settings\n(Add dropdowns here later)")

    # Hidden state to store history (Gradio 6 uses list of dicts natively)
    state = gr.State([])

    # Event wiring
    def user_turn(user_message, history):
        # Format the user message exactly how Gradio 6 expects it
        new_msg = {"role": "user", "content": [
            {"type": "text", "text": user_message}]}
        history.append(new_msg)
        return "", history, history  # Returns: clear textbox, update state, update chatbot

    def ai_turn(history):
        # Extract the user's actual text string from the deeply nested history block
        user_message = history[-1]["content"][0]["text"]
        bot_response = respond(user_message, history)

        new_msg = {"role": "assistant", "content": [
            {"type": "text", "text": bot_response}]}
        history.append(new_msg)
        return history, history  # Returns: update state, update chatbot

    # When the user presses Enter in the text box
    msg.submit(user_turn, [msg, state], [msg, state, chatbot], queue=False).then(
        ai_turn, state, [state, chatbot]
    )

    # Clear both the hidden state and the visible UI chatbot
    clear_btn.click(lambda: ([], []), None, [state, chatbot], queue=False)

if __name__ == "__main__":
    demo.launch()
