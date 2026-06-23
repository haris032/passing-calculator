import streamlit as st

st.title("🎯 Exam Marks & Passing Calculator")
st.markdown("Enter your marks below to calculate the minimum marks required in your Final Exam!")
st.write("---")

# Checkbox agar assignments nahi huin
no_assignments = st.checkbox("❌ Tick this if NO assignments were conducted this semester")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Quizzes")
    num_quizzes = st.selectbox("How many quizzes were conducted?", [1, 2, 3], index=2)
    
    q1 = st.number_input("Quiz 1 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=3.0)
    q2 = 0.0
    q3 = 0.0
    if num_quizzes >= 2:
        q2 = st.number_input("Quiz 2 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=4.0)
    if num_quizzes == 3:
        q3 = st.number_input("Quiz 3 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0)

    # Agar assignments huin hain tabhi inputs nazar aayenge
    if not no_assignments:
        st.write("---")
        st.subheader("📁 Assignments")
        num_assignments = st.selectbox("How many assignments were conducted?", [1, 2, 3], index=2)
        
        as1 = st.number_input("Assignment 1 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0)
        as2 = 0.0
        as3 = 0.0
        if num_assignments >= 2:
            as2 = st.number_input("Assignment 2 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0)
        if num_assignments == 3:
            as3 = st.number_input("Assignment 3 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=9.0)

with col2:
    st.subheader("📊 Mid-Term & Target")
    mid_marks = st.number_input("Mid-Term Marks (Out of 25)", min_value=0.0, max_value=25.0, value=10.0)
    passing_target = st.number_input("Target Passing Percentage (%)", min_value=0.0, max_value=100.0, value=50.0)

# --- Dynamic Calculations ---
total_quiz_obtained = q1 + q2 + q3
max_quiz_marks = num_quizzes * 10
quiz_weightage = (total_quiz_obtained / max_quiz_marks) * 15

mid_weightage = (mid_marks / 25) * 25

if no_assignments:
    # Agar assignment nahi hui to sessional sirf Quiz (15%) + Mid (25%) = 40% ka hai
    current_total_percentage = quiz_weightage + mid_weightage
    final_weightage = 60.0  # Final ka weightage 40% se barh kar 60% ho gaya
    assignment_weightage = 0.0
else:
    # Normal routine
    total_as_obtained = as1 + as2 + as3
    max_as_marks = num_assignments * 10
    assignment_weightage = (total_as_obtained / max_as_marks) * 20
    current_total_percentage = quiz_weightage + assignment_weightage + mid_weightage
    final_weightage = 40.0

needed_percentage = passing_target - current_total_percentage
# Final exam 50 marks ka hi hai lekin weightage ab dynamically change hoga
required_final_marks = (needed_percentage / final_weightage) * 50

# --- Results Display ---
st.write("---")
st.subheader("📊 Your Result:")

sessional_limit = 40.0 if no_assignments else 60.0
st.info(f"**Current Total Score (Out of {int(sessional_limit)}%):** {current_total_percentage:.2f}%")

if required_final_marks <= 0:
    st.success("🎉 Congratulations! You have already passed the course before the Final Exam!")
elif required_final_marks > 50:
    st.error(f"❌ Sorry! It is no longer possible to reach your target of {passing_target}%.")
else:
    st.warning(f"🎯 To pass, you need at least **{required_final_marks:.2f} Marks** out of 50 in the Final Exam.")

with st.expander("🔍 Check Detailed Weightage Breakdown"):
    st.write(f"• Quizzes Weightage: {quiz_weightage:.2f}% / 15%")
    if not no_assignments:
        st.write(f"• Assignments Weightage: {assignment_weightage:.2f}% / 20%")
    st.write(f"• Mid-Term Weightage: {mid_weightage:.2f}% / 25%")
    st.write(f"• Final Exam Weightage: {final_weightage:.2f}%")
