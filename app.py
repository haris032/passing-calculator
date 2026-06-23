import streamlit as st

st.set_page_config(page_title="Universal Passing Calculator", page_icon="🎯", layout="centered")

st.title("🎯 Universal Exam & Passing Calculator")
st.markdown("Customize your sessional activities and enter your marks to find out what you need in your Final Exam!")
st.write("---")

# --- CUSTOM WEIGHTAGES (Expander settings) ---
with st.expander("⚙️ Click here to Customize University Criteria / Weightages"):
    st.markdown("##### Adjust Final & Mid-Term Settings:")
    final_max_marks = st.number_input("Final Exam Total Marks (e.g., 50 or 100)", min_value=1.0, value=50.0)
    mid_max_possible = st.number_input("Mid-Term Total Marks", min_value=1.0, value=25.0)
    
    st.markdown("---")
    st.markdown("##### Percentage Weightages (Total must sum up to 100%):")
    w_quiz = st.number_input("Quizzes Weightage (%)", min_value=0.0, max_value=100.0, value=15.0)
    w_mid = st.number_input("Mid-Term Weightage (%)", min_value=0.0, max_value=100.0, value=25.0)
    w_assign = st.number_input("Assignments Weightage (%)", min_value=0.0, max_value=100.0, value=20.0)
    w_final = st.number_input("Final Exam Weightage (%)", min_value=0.0, max_value=100.0, value=40.0)
    
    # Validation check for 100% total
    total_w_check = w_quiz + w_mid + w_assign + w_final
    if total_w_check != 100.0:
        st.error(f"⚠️ Warning: Your total weightage sums up to {total_w_check}%. It should be exactly 100%!")

st.write("---")

# --- USER SELECTION FOR ACTIVITIES ---
st.subheader("🛠️ Select Conducted Sessional Activities")
st.markdown("Tick the activities your teacher actually conducted this semester:")

col_sel1, col_sel2, col_sel3, col_sel4 = st.columns(4)
with col_sel1:
    has_quizzes = st.checkbox("Quizzes 📝", value=True)
with col_sel2:
    has_assignments = st.checkbox("Assignments 📁", value=True)
with col_sel3:
    has_presentations = st.checkbox("Presentations 🎤", value=False)
with col_sel4:
    has_projects = st.checkbox("Projects 💻", value=False)

st.write("---")

# --- MARKS INPUT COLUMNS ---
col1, col2 = st.columns(2)

current_total_percentage = 0.0
breakdown_dict = {}

with col1:
    # 1. QUIZZES SECTION
    if has_quizzes:
        st.subheader("📝 Quizzes (Total: 25 Marks)")
        num_quizzes = st.selectbox("How many quizzes were conducted?", [1, 2, 3], index=2, key="num_q")
        q1 = st.number_input("Quiz 1 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=3.0, key="q1")
        q2 = 0.0; q3 = 0.0
        if num_quizzes >= 2:
            q2 = st.number_input("Quiz 2 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=4.0, key="q2")
        if num_quizzes == 3:
            q3 = st.number_input("Quiz 3 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0, key="q3")
        
        # Scaling total obtained to 25 marks
        q_obtained = ((q1 + q2 + q3) / (num_quizzes * 10)) * 25
        quiz_w_score = (q_obtained / 25) * w_quiz
        current_total_percentage += quiz_w_score
        breakdown_dict["Quizzes"] = (quiz_w_score, w_quiz)

    # 2. ASSIGNMENTS SECTION
    if has_assignments:
        if has_quizzes: st.write("---")
        st.subheader("📁 Assignments (Total: 25 Marks)")
        num_assignments = st.selectbox("How many assignments were conducted?", [1, 2, 3], index=2, key="num_as")
        as1 = st.number_input("Assignment 1 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0, key="as1")
        as2 = 0.0; as3 = 0.0
        if num_assignments >= 2:
            as2 = st.number_input("Assignment 2 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=10.0, key="as2")
        if num_assignments == 3:
            as3 = st.number_input("Assignment 3 Marks (Out of 10)", min_value=0.0, max_value=10.0, value=9.0, key="as3")
        
        # Scaling total obtained to 25 marks
        as_obtained = ((as1 + as2 + as3) / (num_assignments * 10)) * 25
        as_w_score = (as_obtained / 25) * w_assign
        current_total_percentage += as_w_score
        breakdown_dict["Assignments"] = (as_w_score, w_assign)

with col2:
    # 3. PRESENTATIONS SECTION
    if has_presentations:
        st.subheader("🎤 Presentation (Total: 25 Marks)")
        pres_marks = st.number_input("Presentation Obtained Marks (Out of 25)", min_value=0.0, max_value=25.0, value=20.0)
        # Assuming presentation uses assignment weightage or a shared split. For simplicity, handled as part of sessional.
        pres_w_score = (pres_marks / 25) * w_assign  
        current_total_percentage += pres_w_score
        breakdown_dict["Presentation"] = (pres_w_score, w_assign)

    # 4. PROJECTS SECTION
    if has_projects:
        if has_presentations: st.write("---")
        st.subheader("💻 Project (Total: 25 Marks)")
        proj_marks = st.number_input("Project Obtained Marks (Out of 25)", min_value=0.0, max_value=25.0, value=22.0)
        proj_w_score = (proj_marks / 25) * w_assign
        current_total_percentage += proj_w_score
        breakdown_dict["Project"] = (proj_w_score, w_assign)

    # MID-TERM & TARGET (Hamesha show hoga)
    if has_presentations or has_projects: st.write("---")
    st.subheader("📊 Mid-Term & Target")
    mid_marks = st.number_input(f"Mid-Term Obtained Marks (Out of {int(mid_max_possible)})", min_value=0.0, max_value=mid_max_possible, value=10.0)
    mid_w_score = (mid_marks / mid_max_possible) * w_mid
    current_total_percentage += mid_w_score
    breakdown_dict["Mid-Term"] = (mid_w_score, w_mid)
    
    st.write("---")
    passing_target = st.number_input("Target Passing Percentage (%)", min_value=0.0, max_value=100.0, value=50.0)

# --- FINAL TARGET CALCULATION ---
needed_percentage = passing_target - current_total_percentage
required_final_marks = (needed_percentage / w_final) * final_max_marks

# --- RESULTS DISPLAY ---
st.write("---")
st.subheader("📊 Your Result:")

st.info(f"**Current Total Internal Score Earned:** {current_total_percentage:.2f}%")

if required_final_marks <= 0:
    st.success("🎉 Congratulations! You have already reached your passing target before the Final Exam!")
elif required_final_marks > final_max_marks:
    st.error(f"❌ Sorry! It is no longer possible to reach your target of {passing_target}% even if you get full marks.")
else:
    st.warning(f"🎯 To pass, you need at least **{required_final_marks:.2f} Marks** out of {int(final_max_marks)} in the Final Exam.")

with st.expander("🔍 Check Detailed Weightage Breakdown"):
    for activity, scores in breakdown_dict.items():
        st.write(f"• {activity} Weightage Contribution: {scores[0]:.2f}% / {scores[1]}%")
    st.write(f"• Final Exam Weightage: {w_final:.2f}%")
