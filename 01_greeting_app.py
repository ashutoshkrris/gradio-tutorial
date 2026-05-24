import gradio as gr


# 1. Define the core Python logic
def greet_user(name):
    return f"Hello, {name}! Welcome to your first AI app."


# 2. Create the Interface
demo = gr.Interface(
    fn=greet_user,
    inputs="text",
    outputs="text",
    title="Greeting Generator",
    description="Enter your name to get a custom greeting."
)

# 3. Launch the web server
if __name__ == "__main__":
    demo.launch()
