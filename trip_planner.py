import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = st.secrets["openai"]["api_key"]

# App title
st.title("🌍 AI Trip Planner")
st.markdown("Create a personalized travel itinerary powered by OpenAI GPT.")

# User inputs
destination = st.text_input("Where are you traveling to?", "Paris")
days = st.slider("How many days is your trip?", 1, 14, 5)
interests = st.text_area("What are your interests? (e.g., culture, food, adventure)")

if st.button("Generate Itinerary"):
    with st.spinner("Planning your trip..."):
        prompt = (
            f"Create a detailed {days}-day travel itinerary for a trip to {destination}. "
            f"The user is interested in: {interests}. "
            f"Include day-wise activities, landmarks, and suggestions for each day."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or gpt-4 if your account supports it
                messages=[
                    {"role": "system", "content": "You are a helpful travel planner."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )

            itinerary = response.choices[0].message.content
            st.success("Here's your personalized itinerary:")
            st.markdown(itinerary)

        except Exception as e:
            st.error(f"An error occurred: {e}")
