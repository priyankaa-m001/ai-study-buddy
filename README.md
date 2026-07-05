# 📚 AI Study Buddy — Quiz Generator

An AI-powered web app that turns any topic or your own notes into a
multiple-choice quiz, so you can test yourself instantly.

**Why I built this:** I was studying Data Structures & Algorithms and
kept wishing I had a quick way to quiz myself on whatever I'd just
learned — so I built an AI tool that does exactly that.

## Features
- Paste any topic or notes and generate a custom quiz in seconds
- Choose how many questions you want (3–10)
- Interactive multiple-choice UI built with Streamlit
- Instant scoring with explanations for each answer

## Tech Stack
- **Python**
- **Streamlit** — for the interactive web UI
- **Groq API** (free tier, OpenAI-compatible) — to generate quiz questions dynamically

## How It Works
1. User enters a topic or notes
2. The app sends a prompt to the OpenAI API asking for quiz questions
   in a structured JSON format
3. Streamlit renders the questions as an interactive quiz
4. User submits answers and gets instant scoring + explanations

## Setup & Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/priyankaa-m001/ai-study-buddy.git
cd ai-study-buddy

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your free Groq API key as an environment variable
# Get one at https://console.groq.com (no card required)
export GROQ_API_KEY="your-api-key-here"      # Mac/Linux
setx GROQ_API_KEY "your-api-key-here"        # Windows

# 4. Run the app
streamlit run app.py
```

## Security Note
The API key is read from an environment variable and is never
hardcoded or committed to the repository.

## Future Improvements
- Save quiz history and track progress over time
- Support difficulty levels (easy/medium/hard)
- Add a timer for a more exam-like experience

## Screenshot
*(Add a screenshot of your running app here after you deploy or run it locally)*