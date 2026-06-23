import streamlit as st

st.set_page_config(page_title="Exam Passing Calculator", page_icon="🎯", layout="centered")

st.title("🎯 Exam Marks & Passing Calculator")
st.markdown("Select what components were included in your course to dynamically calculate your passing target!")
st.write("---")

# --- STEP 1: Checkbox Selection ---
st.subheader("📋 Select Included Course Components:")
st.markdown("*Tick the components that your teacher actually conducted this semester:*")

col_cb1, col_cb2, col_cb3, col_cb4 = st.columns(4)
with col_cb1:
    has_quiz = st.checkbox("📝 Quizzes", value=True)
with col_cb2:
    has_assign = st.checkbox("📁 Assignments", value=True)
with col_cb3:
    has_pres = st.checkbox("🎤 Presentations", value=True)
with col_cb4:
    has_proj = st.checkbox("💻 Projects", value=True)

# Weightages allocation logic
base_mid_weightage = 25.0
shifted_weightage = 0.0

quiz_base_w = 6.0       
assign_base_w = 3.0     
pres_base_w = 3.0
proj_base_w = 3.0

if not has_quiz: shifted_weightage += quiz_base_w
if not has_assign: shifted_weightage += assign_base_w
if not has_pres: shifted_weightage += pres_base_w
if not has_proj: shifted_weightage += proj_base_w

dynamic_mid_weightage = base_mid_weightage + shifted_weightage

st.write("---")

# --- STEP 2: Inputs and Marks Collection ---
col1, col2 = st.columns(2)

sessional_obtained_percentage = 0.0

with col1:
    st.subheader("🎯 Internal Marks")
    
    # 1. QUIZZES (Dropdown with 1 to 6 options)
    if has_quiz:
        st.markdown("##### 📝 Quiz Details")
        num_quizzes = st.selectbox("How many quizzes were conducted?", [1, 2, 3, 4, 5, 6], index=2)
        
        # 6 individual quiz inputs initialize kar rahe hain
        quiz_marks = []
        for i in range(num_quizzes):
            q_val = st.number_input(f"Quiz {i+1} Marks (Out of 10)", min_value=0.0, max_value=10.0, value=5.0, key=f"q_{i}")
            quiz_marks.append(q_val)
            
        # Total obtained and max calculation
        total_quiz_obtained = sum(quiz_marks)
        max_quiz_marks = num_quizzes * 10
        
        # Final weightage scale to 6%
        quiz_weightage_earned = (total_quiz_obtained / max_quiz_marks) * quiz_base_w
        sessional_obtained_percentage += quiz_weightage_earned
        
    # 2. ASSIGNMENTS
    if has_assign:
        st.write("---")
        st.markdown("##### 📁 Assignment Details")
        a_max = st.number_input("Total Assignment Marks", min_value=1.0, value=10.0, key="a_max")
        a_obt = st.number_input(f"Obtained Assignment Marks (Out of {int(a_max)})", min_value=0.0, max_value=a_max, value=8.0, key="a_obt")
        sessional_obtained_percentage += (a_obt / a_max) * assign_base_w
        
    # 3. PRESENTATIONS
    if has_pres:
        st.write("---")
        st.markdown("##### 🎤 Presentation Details")
        p_max = st.number_input("Total Presentation Marks", min_value=1.0, value=10.0, key="p_max")
        p_obt = st.number_input(f"Obtained Presentation Marks (Out of {int(p_max)})", min_value=0.0, max_value=p_max, value=8.0, key="p_obt")
        sessional_obtained_percentage += (p_obt / p_max) * pres_base_w
        
    # 4. PROJECTS
    if has_proj:
        st.write("---")
        st.markdown("##### 💻 Project Details")
        pr_max = st.number_input("Total Project Marks", min_value=1.0, value=50.0, key="pr_max")
        pr_obt = st.number_input(f"Obtained Project Marks (Out of {int(pr_max)})", min_value=0.0, max_value=pr_max, value=40.0, key="pr_obt")
        sessional_obtained_percentage += (pr_obt / pr_max) * proj_base_w

with col2:
    st.subheader("📊 Mid-Term & Final Settings")
    mid_max = st.number_input("Mid-Term Total Marks", min_value=1.0, value=25.0)
    mid_obtained = st.number_input(f"Mid-Term Obtained Marks (Out of {int(mid_max)})", min_value=0.0, max_value=mid_max, value=15.0)
    
    st.write("---")
    final_max = st.number_input("Final Exam Total Marks", min_value=1.0, value=50.0)
    passing_target = st.number_input("Target Passing Percentage (%)", min_value=0.0, max_value=100.0, value=50.0)

# --- STEP 3: Calculations ---
mid_weightage_earned = (mid_obtained / mid_max) * dynamic_mid_weightage
current_total_percentage = sessional_obtained_percentage + mid_weightage_earned
base_final_weightage = 40.0

needed_percentage = passing_target - current_total_percentage
required_final_marks = (needed_percentage / base_final_weightage) * final_max

# --- STEP 4: Results Display ---
st.write("---")
st.subheader("📊 Your Result:")

total_allocated_now = (15.0 - shifted_weightage) + dynamic_mid_weightage
st.info(f"**Current Total Score (Out of {int(total_allocated_now)}%):** {current_total_percentage:.2f}%")

if required_final_marks <= 0:
    st.success("🎉 Congratulations! You have already reached your passing target before the Final Exam!")
elif required_final_marks > final_max:
    st.error(f"❌ Sorry! It is no longer possible to reach your target of {passing_target}% even if you get full marks.")
else:
    st.warning(f"🎯 To pass, you need at least **{required_final_marks:.2f} Marks** out of {int(final_max)} in the Final Exam.")

# Breakdown Details
with st.expander("🔍 Check Detailed Weightage Breakdown"):
    if has_quiz: st.write(f"• Quizzes Weightage: {quiz_weightage_earned:.2f}% / {quiz_base_w}%")
    if has_assign: st.write(f"• Assignments Weightage: {(a_obt/a_max)*assign_base_w:.2f}% / {assign_base_w}%")
    if has_pres: st.write(f"• Presentations Weightage: {(p_obt/p_max)*pres_base_w:.2f}% / {pres_base_w}%")
    if has_proj: st.write(f"• Projects Weightage: {(pr_obt/pr_max)*proj_base_w:.2f}% / {proj_base_w}%")
    st.write(f"• Mid-Term Weightage: {mid_weightage_earned:.2f}% / {dynamic_mid_weightage}% *(Base 25% + {shifted_weightage}% shifted)*")
    st.write(f"• Final Exam Weightage: {base_final_weightage}%")
