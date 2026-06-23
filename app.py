import streamlit as st

st.set_page_config(page_title="Exam Passing Calculator", page_icon="🎯", layout="centered")

st.title("🎯 Exam Marks & Passing Calculator")
st.markdown("Enter your total internal marks to calculate the minimum marks required in your Final Exam!")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Internal / Sessional Marks")
    st.markdown("*(Includes all Quizzes, Assignments, Presentations, and Projects combined)*")
    
    # User se pucha ke sessional total kitne marks ka tha (e.g., 15 ya 30)
    sessional_max = st.number_input("Total Sessional Marks (as per syllabus)", min_value=1.0, value=15.0)
    # User ne usme se kitne marks liye
    sessional_obtained = st.number_input(f"Your Obtained Marks (Out of {int(sessional_max)})", min_value=0.0, max_value=sessional_max, value=10.0)
    
    # Sessional ka weightage percentage (Aapke case mein 15%)
    w_sessional = st.number_input("Sessional Weightage Percentage (%)", min_value=0.0, max_value=100.0, value=15.0)

with col2:
    st.subheader("📊 Mid-Term & Final Settings")
    # Mid-term marks input
    mid_max = st.number_input("Mid-Term Total Marks", min_value=1.0, value=25.0)
    mid_obtained = st.number_input(f"Mid-Term Obtained Marks (Out of {int(mid_max)})", min_value=0.0, max_value=mid_max, value=10.0)
    w_mid = st.number_input("Mid-Term Weightage Percentage (%)", min_value=0.0, max_value=100.0, value=25.0)
    
    st.write("---")
    # Final exam settings
    final_max = st.number_input("Final Exam Total Marks", min_value=1.0, value=50.0)
    passing_target = st.number_input("Target Passing Percentage (%)", min_value=0.0, max_value=100.0, value=50.0)

# --- Calculations ---
# Weightages calculation based on formulas
sessional_weightage = (sessional_obtained / sessional_max) * w_sessional
mid_weightage = (mid_obtained / mid_max) * w_mid

current_total_percentage = sessional_weightage + mid_weightage

# Baqi bacha hua weightage automatic Final Exam ko chala jayega (e.g., 100 - 15 - 25 = 60%)
w_final = 100.0 - (w_sessional + w_mid)

needed_percentage = passing_target - current_total_percentage
required_final_marks = (needed_percentage / w_final) * final_max

# --- Results Display ---
st.write("---")
st.subheader("📊 Your Result:")

st.info(f"**Current Total Score (Out of {int(w_sessional + w_mid)}%):** {current_total_percentage:.2f}%")

if required_final_marks <= 0:
    st.success("🎉 Congratulations! You have already reached your passing target before the Final Exam!")
elif required_final_marks > final_max:
    st.error(f"❌ Sorry! It is no longer possible to reach your target of {passing_target}% even if you get full marks.")
else:
    st.warning(f"🎯 To pass, you need at least **{required_final_marks:.2f} Marks** out of {int(final_max)} in the Final Exam.")

with st.expander("🔍 Check Detailed Weightage Breakdown"):
    st.write(f"• Sessional Weightage (Quizzes/Projects etc.): {sessional_weightage:.2f}% / {w_sessional}%")
    st.write(f"• Mid-Term Weightage: {mid_weightage:.2f}% / {w_mid}%")
    st.write(f"• Final Exam Weightage: {w_final:.2f}%")
