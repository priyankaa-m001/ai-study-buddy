"""
AI Study Buddy - Quiz Generator
Paste any topic or your own notes, and this app uses AI to generate
quiz questions with answers so you can test yourself.
"""

import json
import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Study Buddy", page_icon="Book", layout="centered")

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

st.title("AI Study Buddy")
st.write(
    "Paste a topic (e.g. 'Two Pointer Technique') or your own notes below, "
    "and I'll generate quiz questions to help you test yourself."
)

topic = st.text_area(
    "Topic or notes to quiz yourself on:",
    placeholder="e.g. Arrays and Two-Pointer Technique in DSA",
    height=150,
)

num_questions = st.slider("Number of questions", min_value=3, max_value=10, value=5)

def generate_quiz(topic_text, count):
    prompt = f"""
    You are a helpful quiz generator. Based on the topic or notes below,
    create {count} multiple-choice quiz questions to help a student practice.

    Topic/Notes:
    \"\"\"{topic_text}\"\"\"

    Return ONLY valid JSON, no extra text, in this exact format:
    [
      {{
        "question": "...",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "explanation": "..."
      }}
    ]
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    raw_text = response.choices[0].message.content.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.replace("json", "", 1).strip()
    return json.loads(raw_text)

if st.button("Generate Quiz", type="primary"):
    if not topic.strip():
        st.warning("Please enter a topic or some notes first.")
    else:
        with st.spinner("Generating your quiz..."):
            try:
                quiz = generate_quiz(topic, num_questions)
                st.session_state["quiz"] = quiz
                st.session_state["answers"] = {}
            except Exception as e:
                st.error(f"Something went wrong: {e}")

if "quiz" in st.session_state:
    st.divider()
    st.subheader("Your Quiz")
    for i, q in enumerate(st.session_state["quiz"]):
        st.write(f"Q{i + 1}. {q['question']}")
        choice = st.radio(
            "Choose one:",
            q["options"],
            key=f"q_{i}",
            index=None,
            label_visibility="collapsed",
        )
        st.session_state["answers"][i] = choice
        st.write("")

    if st.button("Check Answers"):
        score = 0
        st.divider()
        st.subheader("Results")
        for i, q in enumerate(st.session_state["quiz"]):
            user_answer = st.session_state["answers"].get(i)
            correct = q["answer"]
            if user_answer == correct:
                score += 1
                st.success(f"Q{i + 1}: Correct!")
            else:
                st.error(f"Q{i + 1}: Incorrect - Correct answer: {correct}")
            st.caption(q["explanation"])
        st.info(f"Final Score: {score} / {len(st.session_state['quiz'])}")
