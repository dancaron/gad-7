import streamlit as st

st.title('GAD-7 Calculator')

# Define the questions and answer choices
questions = [
    "Feeling nervous, anxious, or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it's hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid as if something awful might happen",
]

choices = [
    "Not at all", 
    "Several days", 
    "More than half the days", 
    "Nearly every day",
]

# Create a sidebar with a select box for each question
scores = []
for i, question in enumerate(questions):
    scores.append(st.sidebar.selectbox(question, choices, index=0, key=i))

# Define the scoring system
score_mapping = {
    "Not at all": 0,
    "Several days": 1,
    "More than half the days": 2,
    "Nearly every day": 3,
}

# Calculate the total score
total_score = sum(score_mapping[score] for score in scores)

# Display the total score
st.write(f'Your GAD-7 score is: {total_score}')

# Provide information about the score interpretation
if total_score < 5:
    st.write("Minimal anxiety")
elif total_score < 10:
    st.write("Mild anxiety")
elif total_score < 15:
    st.write("Moderate anxiety")
else:
    st.write("Severe anxiety")
