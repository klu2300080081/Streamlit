import streamlit as st

# Set the title of the Streamlit application
st.title("Hello, Streamlit!")

# Display a simple text message
st.write("Welcome to your first Streamlit app.")

# Add a text input widget
user_input = st.text_input("What's your name?", "World")

# Display a personalized greeting based on the input
st.write(f"Hello, {user_input}!")

# To run this application:
# 1. Save the code above as a Python file (e.g., app.py).
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: streamlit run app.py
