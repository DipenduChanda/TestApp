import streamlit as st

# Example quiz data
quiz_data = [
    {
        "question": "1. What is the purpose of pile probing?",
        "choices": [
            "a) To save money",
            "b) To check for potential voids in proposed pile location",
            "c) To check the conditions of the surrounding soil",
            "d) To ensure they have been installed correctly"
        ],
        "answer": "b) To check for potential voids in proposed pile location"
    },
    {
        "question": "2. How does a pile integrity test work?",
        "choices": [
            "a) Through electromagnetic waves",
            "b) By breaking a small piece of the concrete poured",
            "c) Through engineering calculations",
            "d) Sending stress waves through the pile using a hand-held device or sensor"
        ],
        "answer": "d) Sending stress waves through the pile using a hand-held device or sensor"
    }
]

# Function to display the current question and choices
def show_question():
    question = quiz_data[st.session_state.current_question]
    st.write(question['question'])
    selected_choice = st.radio("Select your answer:", question['choices'])
    submit_button = st.button("Submit")
    if submit_button:
        check_answer(selected_choice)

# Function to check the selected answer and provide feedback
def check_answer(selected_choice):
    question = quiz_data[st.session_state.current_question]
    if selected_choice == question["answer"]:
        st.write("Correct!")
        st.write("Click on any of the other option to proceed!")
        st.balloons()
        st.session_state.score += 1
    else:
        st.write("Incorrect!")
        st.write("Click on any of the other option to proceed!")
    next_question()

# Function to move onto the next question
def next_question():
    current_question = st.session_state.current_question + 1
    if current_question < len(quiz_data):
        st.session_state.current_question = current_question
    else:
        st.success(f"Quiz Complete! Your Score: {st.session_state.score}/{len(quiz_data)}  (Reload the page to try again!)")


# Main function - initializing the session state variables
def main():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    st.title("MCQ Quiz for DE")
    show_question()

if __name__ == "__main__":
    main()
