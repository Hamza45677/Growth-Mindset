import streamlit as st
import random
from datetime import date

# Daily Affirmations
affirmations = [
    "I am capable of achieving great things.",
    "Challenges help me grow and improve.",
    "Every failure is a step towards success.",
    "I embrace learning and new opportunities.",
    "My mindset shapes my future."
]

def get_daily_affirmation():
    random.seed(date.today().toordinal())  
    return random.choice(affirmations)


st.set_page_config(layout="wide")
st.title("🌱 Growth Mindset App")
st.subheader("Boost Your Mindset Every Day")
st.markdown("*🌱 Developed by Hamza Sohail using Streamlit.*")



with st.sidebar:
    st.header("💡 Daily Affirmation")
    st.info(get_daily_affirmation())
    
    st.header("🎯 Set Your Goal")
    goal = st.text_input("Enter your goal for today:")
    if goal:
        st.success(f"Your goal: {goal}")
    
    st.header("📖 Daily Journal")
    journal_entry = st.text_area("Write about your progress, challenges, or lessons learned today:")
    if journal_entry:
        st.success("Journal saved! Reflecting helps with growth.")
    
    st.header("🤝 Community Motivation")
    user_message = st.text_input("Share a motivational message with the community:")
    if st.button("Post Message"):
        if user_message:
            st.write(f"📝 {user_message}")
            st.success("Your message has been shared!")
        else:
            st.warning("Please enter a message before posting.")
    
    st.header("🧘‍♂️ Mindfulness & Reflection")
    st.write("Take a deep breath, stay present, and focus on the positives!")
