import streamlit as st
from PIL import Image

# Dictionary of Mandela Effect examples
mandela_effect_images = {
   
    "coca_cola_logo": {
        "image1": "images/coca_cola_no_dash.jpg",
        "image2": "images/coca_cola_with_dash.jpg",
        "correct": "image2",
    },
    "dharma_productions_logo": {
        "image1": "images/dharma_old_logo.jpg",
        "image2": "images/dharma_new_logo.jpg",
        "correct": "image2",
    },
    "oreo_double_stuf": {
        "image1": "images/oreo_double_stuff.jpg",
        "image2": "images/oreo_double_stuf.jpg",
        "correct": "image2",
    },
    "peace_symbol": {
        "image1": "images/peace_symbol_incorrect.jpg",
        "image2": "images/peace_symbol_correct.jpg",
        "correct": "image2",
    },
    "pikachu_tail": {
        "image1": "images/pikachu_black_tail.jpg",
        "image2": "images/pikachu_no_black_tail.jpg",
        "correct": "image2",
    },
    "starbucks_logo": {
        "image1": "images/starbucks_incorrect_logo.jpg",
        "image2": "images/starbucks_correct_logo.jpg",
        "correct": "image2",
    },
    "volkswagen_logo": {
        "image1": "images/volkswagen_no_gap.jpg",
        "image2": "images/volkswagen_with_gap.jpg",
        "correct": "image2",
    },
    "zindagi_na_milegi_dobara": {
        "image1": "images/znmd_incorrect_scene.jpg",
        "image2": "images/znmd_correct_scene.jpg",
        "correct": "image2",
    },
    "zor_zor_se_scheme": {
        "image1": "images/zor_zor_incorrect.jpg",
        "image2": "images/zor_zor_correct.jpg",
        "correct": "image2",
    },
}

# Streamlit App Setup
st.title("Mandela Effect Quiz")
st.write("Can you identify the correct version of these famous logos, symbols, and scenes?")

# Quiz State Initialization
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# List of questions
questions = list(mandela_effect_images.keys())

if st.session_state.current_question < len(questions):
    # Get current question
    question = questions[st.session_state.current_question]
    data = mandela_effect_images[question]

    # Display question
    st.write(f"**Question {st.session_state.current_question + 1}: {question.replace('_', ' ').title()}**")

    # Display images side by side
    col1, col2 = st.columns(2)
    with col1:
        img1 = Image.open(data["image1"]).resize((300, 300))
        st.image(img1, caption="Option 1")
        if st.button("Choose Option 1", key=f"{question}_1"):
            if data["correct"] == "image1":
                st.session_state.score += 1
            st.session_state.current_question += 1

    with col2:
        img2 = Image.open(data["image2"]).resize((300, 300))
        st.image(img2, caption="Option 2")
        if st.button("Choose Option 2", key=f"{question}_2"):
            if data["correct"] == "image2":
                st.session_state.score += 1
            st.session_state.current_question += 1
else:
    # Show final score
    st.write(f"### Quiz Complete! 🎉 Your Score: {st.session_state.score}/{len(questions)}")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_question = 0
