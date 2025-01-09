import streamlit as st
from PIL import Image

# Dictionary of Mandela Effect examples
mandela_effect_images = {
    "coca_cola_logo": {
        "image1": "images/coca_cola_with_dash.jpg",
        "image2": "images/coca_cola_no_dash.jpg",
        "correct": "image1",
        "explanation": "The Coca-Cola logo never had a dash in between the words 'Coca' and 'Cola'."
    },
    "oreo_double_stuf": {
        "image1": "images/oreo_double_stuff.jpg",
        "image2": "images/oreo_double_stuf.jpg",
        "correct": "image2",
        "explanation": "Oreo has always spelled it 'Double Stuf' without an extra 'f' at the end."
    },
    "peace_symbol": {
        "image1": "images/peace_symbol_correct.jpg",
        "image2": "images/peace_symbol_incorrect.jpg",
        "correct": "image1",
        "explanation": "The peace symbol has a vertical line in the center, which has been part of its iconic design."
    },
    "pikachu_tail": {
        "image1": "images/pikachu_black_tail.jpg",
        "image2": "images/pikachu_no_black_tail.jpg",
        "correct": "image2",
        "explanation": "Pikachu has always had a solid yellow tail. It never had a black tip."
    },
    "starbucks_logo": {
        "image1": "images/starbucks_incorrect_logo.jpg",
        "image2": "images/starbucks_correct_logo.jpg",
        "correct": "image2",
        "explanation": "The Starbucks logo has always shown a two-tailed siren, never a single tail."
    },
    "volkswagen_logo": {
        "image1": "images/volkswagen_no_gap.jpg",
        "image2": "images/volkswagen_with_gap.jpg",
        "correct": "image2",
        "explanation": "The Volkswagen logo has always had a gap between the 'V' and 'W'."
    },
    "skechers_logo": {
        "image1": "images/skechers_correct.jpg",
        "image2": "images/sketchers_incorrect.jpg",
        "correct": "image1",
        "explanation": "The correct spelling is 'Skechers' with an 'E', not 'Sketchers'."
    },
    "kitkat_logo": {
        "image1": "images/kitkat_with_dash.jpg",
        "image2": "images/kitkat_no_dash.jpg",
        "correct": "image2",
        "explanation": "KitKat's logo has never had a dash between 'Kit' and 'Kat'."
    },
    "looney_tunes": {
        "image1": "images/looney_tunes.jpg",
        "image2": "images/looney_toons.jpg",
        "correct": "image1",
        "explanation": "The correct name is 'Looney Tunes' with a 'U', not 'Looney Toons'."
    },
    # Seahorse emoji question (correct answer is False)
    "seahorse_emoji": {
        "image1": "images/seahorse_emoji.jpg",  # Single seahorse emoji image
        "correct": "False",  # The correct answer is 'False', the emoji does not exist
        "correct": "True",
        "explanation": "No, the Seahorse emoji does not exist in the current Unicode standard."
    }
}

# Streamlit App Setup
st.title("Mandela Effect Quiz")
st.write("Can you identify the correct version of these famous logos, symbols, and scenes?")

# Quiz State Initialization
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []  # To store user answers and correctness

# List of questions
questions = list(mandela_effect_images.keys())

if st.session_state.current_question < len(questions):
    # Get current question
    question = questions[st.session_state.current_question]
    data = mandela_effect_images[question]

    # Display question
    st.write(f"**Question {st.session_state.current_question + 1}: {question.replace('_', ' ').title()}**")

    # For Seahorse Emoji question (resize it smaller)
    if question == "seahorse_emoji":
        seahorse_image = Image.open(data["image1"]).resize((150, 150))  # Resize to smaller dimensions
        st.image(seahorse_image, caption="Seahorse Emoji")

        # Add buttons for True or False
        if st.button("True"):
            user_choice = "True"
            is_correct = (user_choice == data["correct"])
            st.session_state.user_answers.append((question, user_choice, is_correct))
            if is_correct:
                st.session_state.score += 1
            st.session_state.current_question += 1

        if st.button("False"):
            user_choice = "False"
            is_correct = (user_choice == data["correct"])
            st.session_state.user_answers.append((question, user_choice, is_correct))
            if is_correct:
                st.session_state.score += 1
            st.session_state.current_question += 1

    # For all other image-based questions
    else:
        # Display images side by side
        col1, col2 = st.columns(2)
        with col1:
            img1 = Image.open(data["image1"]).resize((300, 300))
            st.image(img1, caption="Option 1")
            if st.button("Choose Option 1", key=f"{question}_1"):
                user_choice = "image1"
                is_correct = (user_choice == data["correct"])
                st.session_state.user_answers.append((question, "Option 1", is_correct))
                if is_correct:
                    st.session_state.score += 1
                st.session_state.current_question += 1

        with col2:
            img2 = Image.open(data["image2"]).resize((300, 300))
            st.image(img2, caption="Option 2")
            if st.button("Choose Option 2", key=f"{question}_2"):
                user_choice = "image2"
                is_correct = (user_choice == data["correct"])
                st.session_state.user_answers.append((question, "Option 2", is_correct))
                if is_correct:
                    st.session_state.score += 1
                st.session_state.current_question += 1
else:
    # Show final score and answer feedback
    st.balloons()
    st.write(f"### Quiz Complete! 🎉 Your Score: {st.session_state.score}/{len(questions)}")

    # Display detailed feedback for each question with correct images and explanation
    st.write("### Detailed Feedback:")
    for question, answer, is_correct in st.session_state.user_answers:
        data = mandela_effect_images[question]
        st.write(f"**{question.replace('_', ' ').title()}**")

        # For Seahorse Emoji question (use the smaller size here too)
        if question == "seahorse_emoji":
            seahorse_image = Image.open(data["image1"]).resize((150, 150))  # Keep the smaller size for feedback
            st.image(seahorse_image, caption="Seahorse Emoji")
        
        # Show correct image and explanation for other questions
        elif question != "seahorse_emoji":
            correct_image = Image.open(data[data["correct"]]).resize((300, 300))
            st.image(correct_image, caption=f"Correct answer: {answer}")
        
        st.write(f"**Explanation:** {data['explanation']}")

    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.user_answers = []
