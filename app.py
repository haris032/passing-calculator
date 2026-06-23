import streamlit as st

# Website ka Title
st.title("🎯 Exam Marks & Passing Calculator")
st.markdown("Apne marks enter karein aur check karein ke Finals mein kitne number chahiye!")
st.write("---")

# UI ko do hisson mein divide karne ke liye columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Quizzes & Assignments")
    q1 = st.number_input("Quiz 1 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=3.0)
    q2 = st.number_input("Quiz 2 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=4.0)
    q3 = st.number_input("Quiz 3 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0)
    
    as1 = st.number_input("Assignment 1 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0)
    as2 = st.number_input("Assignment 2 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0)
    as3 = st.number_input("Assignment 3 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=9.0)

with col2:
    st.subheader("📊 Mid-Term & Target")
    mid_marks = st.number_input("Mid-Term Marks (Out of 25)", min_value=0.0, max_value=25.0, value=10.0)
    passing_target = st.number_input("Target Passing Percentage (%)", min_value=0.0, max_value=100.0, value=50.0)

# --- Calculations ---
quiz_weightage = ((q1 + q2 + q3) / 30) * 15
assignment_weightage = ((as1 + as2 + as3) / 30) * 20
mid_weightage = (mid_marks / 25) * 25
current_total_percentage = quiz_weightage + assignment_weightage + mid_weightage

needed_percentage = passing_target - current_total_percentage
required_final_marks = (needed_percentage / 40) * 50

# --- Results Display ---
st.write("---")
st.subheader("📊 Aapka Result:")

st.info(f"**Ab tak ka Total Score (Out of 60%):** {current_total_percentage:.2f}%")

if required_final_marks <= 0:
    st.success("🎉 Mubarak ho! Aap Finals se pehle hi overall paas ho chuke hain!")
elif required_final_marks > 50:
    st.error(f"❌ Sorry! {passing_target}% target tak pohnchna ab possible nahi hai.")
else:
    st.warning(f"🎯 Paas hone ke liye Final Exam (50 marks) mein se kam az kam **{required_final_marks:.2f} Marks** chahiye hain.")

# Breakdown detail (optional)
with st.expander("🔍 Detailed Weightage Breakdown Check Karein"):
    st.write(f"• Quizzes Weightage: {quiz_weightage:.2f}% / 15%")
    st.write(f"• Assignments Weightage: {assignment_weightage:.2f}% / 20%")
    st.write(f"• Mid-Term Weightage: {mid_weightage:.2f}% / 25%")
