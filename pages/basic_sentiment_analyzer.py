import streamlit as st

# Set page title and subtitle
st.title("Sentiment Analyzer")
st.subheader("Enter your name and how you feel today")

# Sidebar for input fields
st.sidebar.header("Input Information")
name = st.sidebar.text_input("What's your name?")
message = st.sidebar.text_area("Tell me what you feel today")

# Lists of positive and negative words
positive_words = ['good', 'excited', 'happy', 'great', 'fantastic', 'wonderful']
negative_words = ['bad', 'sad', 'angry', 'terrible', 'awful', 'miserable']

# Function to analyze sentiment and display result
def sayFeeling():
    if name and message:
        st.markdown("---")  # Horizontal line for separation
        st.write(f"Hi, {name}!")

        # Convert message to lowercase and split into words
        words = message.lower().split()

        # Check for positive and negative words
        positive_count = sum(word in positive_words for word in words)
        negative_count = sum(word in negative_words for word in words)

        # Determine sentiment based on counts
        if positive_count > negative_count:
            st.markdown("---")
            st.markdown("<span style='color:green; font-size: 1.2em;'>That's good! 😊</span>", unsafe_allow_html=True)
        elif negative_count > positive_count:
            st.markdown("---")
            st.markdown("<span style
