import streamlit as st
import random

# Configure page
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")
st.title("🎲 Number Guessing Game by ZeeJay 🙅‍♂️")

# Initialize session state
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)
    st.session_state.game_over = False
    st.session_state.message = ""

# Game logic
def check_guess():
    guess = st.session_state.guess_input
    if guess < st.session_state.random_number:
        st.session_state.message = "📉 Too low! Try again!"
    elif guess > st.session_state.random_number:
        st.session_state.message = "📈 Too high! Try again!"
    else:
        st.session_state.message = f"🎉 Correct! The number was {st.session_state.random_number}!"
        st.session_state.game_over = True

# Reset game
def reset_game():
    st.session_state.random_number = random.randint(1, 10)
    st.session_state.game_over = False
    st.session_state.message = ""

# Game interface
st.write("### Guess a number between 1 and 10")

if not st.session_state.game_over:
    # Input and button in columns
    col1, col2 = st.columns([3, 1])
    with col1:
        st.number_input(
            "Your guess:", 
            min_value=1, 
            max_value=10, 
            key="guess_input",
            label_visibility="collapsed"
        )
    with col2:
        st.button("Check", on_click=check_guess, use_container_width=True)

# Display messages and play again button
if st.session_state.message:
    st.write(st.session_state.message)

if st.session_state.game_over:
    st.balloons()
    st.button("Play Again 🕹️", on_click=reset_game)

# Optional: Display rules in expander
with st.expander("ℹ️ Game Rules"):
    st.write("""
    1. The computer randomly selects a number between 1 and 10
    2. You try to guess the number
    3. You'll get hints if your guess is too high or too low
    4. Game continues until you guess correctly
    5. Click 'Play Again' to start a new game
    """)