import streamlit as st

# Set page title and subtitle
st.title("Sentiment Analyzer")
st.subheader("Enter your name and how you feel today")

# Input fields for name and message
name = st.text_input("What's your name?")
message = st.text_area("Tell me what you feel today")

# Lists of positive and negative words
positive_words = ['good', 'excited', 'happy', 'great', 'fantastic', 'wonderful']
negative_words = ['bad', 'sad', 'angry', 'terrible', 'awful', 'miserable']

# Function to analyze sentiment and display result
def analyze_sentiment():
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
            st.write("That's good! 😊")
        elif negative_count > positive_count:
            st.write("I hope you feel better soon. 😞")
        else:
            st.write("Keep going! 😐")
    else:
        st.warning("Please enter both your name and how you feel today.")

# Button to trigger sentiment analysis
if st.button('Analyze Sentiment'):
    analyze_sentiment()

# Additional content or features can be added below
