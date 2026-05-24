# Build AI Apps with Gradio & Python

This repository contains the complete code examples for the tutorial: **[Build AI Apps with Gradio: Turn Your Python Scripts into Web Apps](https://blog.ashutoshkrris.in/build-ai-apps-with-gradio-turn-your-python-scripts-into-web-apps)**.

These scripts demonstrate how to take basic Python logic and terminal chatbots and convert them into interactive web applications using Gradio and Google's free-tier Gemini API.

## 📖 Read the Tutorial
For a full step-by-step breakdown of how this code works, including engineering insights and UI concepts, [read the full article on my blog](https://blog.ashutoshkrris.in/build-ai-apps-with-gradio-turn-your-python-scripts-into-web-apps).

## 🗂️ What's Inside

*   **`01_greeting_app.py`**: The "Hello World" of Gradio. A simple text-in, text-out web interface.
*   **`02_basic_chatbot.py`**: A fully functional web chatbot that parses Gradio's history dictionaries into Gemini API requests.
*   **`03_custom_layout.py`**: An introduction to `gr.Blocks`, demonstrating rows, columns, and custom button events.
*   **`04_streaming_chatbot.py`**: A chatbot that uses Python generators (`yield`) to stream LLM responses word-by-word.
*   **`05_document_qa.py`**: A file-upload application where the AI answers questions based on a provided `.txt` document, rendering outputs in rich Markdown.

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone [https://github.com/ashutoshkrris/gradio-tutorial.git](https://github.com/ashutoshkrris/gradio-tutorial.git)
cd gradio-tutorial
```

### 2. Set up a virtual environment
```bash
# Mac/Linux
python -m venv ai_app_env
source ai_app_env/bin/activate

# Windows
python -m venv ai_app_env
ai_app_env\Scripts\activate
```

### 3. Install dependencies
```bash
pip install gradio google-genai python-dotenv
```

### 4. Add your Gemini API Key
Create a file named `.env` in the root folder of this project. Get a free API key from Google AI Studio and add it to the file:
```
GEMINI_API_KEY=your_actual_api_key_here
```
> (Note: Never commit your `.env` file to version control. It is already included in the .gitignore of this repository).

### 5. Run an app
Pick any script and run it via the terminal:
```bash
python 05_document_qa.py
```
Open the local URL (usually `http://127.0.0.1:7860`) in your browser to test it out.

## 🤝 Share Your Work!
If you use this code to build your own AI app, take a screenshot or screen recording and share it on Twitter! Tag me at [@ashutoshkrris](http://x.com/ashutoshkrris) so I can see what you built and showcase your work.
