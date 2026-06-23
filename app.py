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

# Ginte hain ke kitni cheezein select huin
selected_components = [has_quiz, has_assign, has_pres, has_proj]
active_count = sum(selected_components)

st.write("---")

# --- STEP 2: Base Weightages Settings ---
# Default distribution of the 15% sessional marks
base_mid_weightage = 25.0
base_final_weightage = 40.0
total_sessional_pool = 15.0

if active_count > 0:
    # Agar kuch sessional items select huin, to 15% unme barabar baant dete hain
    weight_per_item = total_sessional_pool / active_count
    dynamic_mid_weightage = base_mid_weightage
else:
    # AGAR KUCH BHI SELECT NAHI HUA (Sessional tha hi nahi):
    # To poora 15% uth kar Mid-term mein chala jayega (Mid-term = 25% + 15% = 40%)
    weight_per_item = 0.0
    dynamic_mid_weightage = base_mid_weightage + total_sessional_pool

# --- STEP 3: Inputs and Marks Collection ---
col1, col2 = st.columns(2)

sessional_obtained_percentage = 0.0

with col1:
    st.subheader("🎯 Internal Marks")
    
    if active_count == 0:
        st.info("ℹ️ No sessional components selected. Their weightage is shifted to Mid-Terms!")
    
    # Dynamically har active item ka input box show hoga
    if has_quiz:
        q_max = st.number_input("Total Quiz Marks (e.g., 10 or 20)", min_value=1.0, value=10.0, key="q_max")
        q_obt = st.number_input(f"Obtained Quiz Marks (Out of {int(q_max)})", min_value=0.0, max_value=q_max, value=7.0, key="q_obt")
        sessional_obtained_percentage += (q_obt / q_max) * weight_per_item
        
    if has_assign:
        a_max = st.number_input("Total Assignment Marks", min_value=1.0, value=10.0, key="a_max")
        a_obt = st.number_input(f"Obtained Assignment Marks (Out of {int(a_max)})", min_value=0.0, max_value=a_max, value=8.0, key="a_obt")
        sessional_obtained_percentage += (a_obt / a_max) * weight_per_item
        
    if has_pres:
        p_max = st.number_input("Total Presentation Marks", min_value=1.0, value=10.0, key="p_max")
        p_obt = st.number_input(f"Obtained Presentation Marks (Out of {int(p_max)})", min_value=0.0, max_value=p_max, value=8.0, key="p_obt")
        sessional_obtained_percentage += (p_obt / p_max) * weight_per_item
        
    if has_proj:
        pr_max = st.number_input("Total Project Marks", min_value=1.0, value=50.0, key="pr_max")
        pr_obt = st.number_input(f"Obtained Project Marks (Out of {int(pr_max)})", min_value=0.0, max_value=pr_max, value=40.0, key="pr_obt")
        sessional_obtained_percentage += (pr_obt / pr_max) * weight_per_item

with col2:
    st.subheader("📊 Mid-Term & Final Settings")
    mid_max = st.number_input("Mid-Term Total Marks", min_value=1.0, value=25.0)
    mid_obtained = st.number_input(f"Mid-Term Obtained Marks (Out of {int(mid_max)})", min_value=0.0, max_value=mid_max, value=15.0)
    
    st.write("---")
    final_max = st.number_input("Final Exam Total Marks", min_value=1.0, value=50.0)
    passing_target = st.number_input("Target Passing Percentage (%)", min_value=0.0, max_value=100.0, value=50.0)

# --- STEP 4: Calculations ---
# Mid term dynamic percentage calculation
mid_weightage_earned = (mid_obtained / mid_max) * dynamic_mid_weightage

# Total earned percentage till now
current_total_percentage = sessional_obtained_percentage + mid_weightage_earned

# Final Exam takes the remaining weightage to make it 100% total
# (If sessionals are active: 15 + 25 + 60 = 100. If sessionals are 0: 40 + 60 = 100)
actual_final_weightage = 100.0 - ( (total_sessional_pool if active_count > 0 else 0.0) + dynamic_mid_weightage )
if actual_final_weightage == 0: 
    actual_final_weightage = base_final_weightage # Safeguard baseline

needed_percentage = passing_target - current_total_percentage
required_final_marks = (needed_percentage / base_final_weightage) * final_max

# --- STEP 5: Results Display ---
st.write("---")
st.subheader("📊 Your Result:")

total_sessional_allocated = (total_sessional_pool if active_count > 0 else 0.0)
st.info(f"**Current Total Score (Out of {int(total_sessional_allocated + dynamic_mid_weightage)}%):** {current_total_percentage:.2f}%")

if required_final_marks <= 0:
    st.success("🎉 Congratulations! You have already reached your passing target before the Final Exam!")
elif required_final_marks > final_max:
    st.error(f"❌ Sorry! It is no longer possible to reach your target of {passing_target}% even if you get full marks.")
else:
    st.warning(f"🎯 To pass, you need at least **{required_final_marks:.2f} Marks** out of {int(final_max)} in the Final Exam.")

# Breakdown Details
with st.expander("🔍 Check Detailed Weightage Breakdown"):
    if active_count > 0:
        st.write(f"• Total Sessional Weightage (Active Tasks): {sessional_obtained_percentage:.2f}% / {total_sessional_pool}%")
        st.write(f"  *(Each active task holds {weight_per_item:.2f}% weightage)*")
    else:
        st.write(f"• Total Sessional Weightage: 0.00% (Shifted to Mid-Term)")
    st.write(f"• Mid-Term Weightage: {mid_weightage_earned:.2f}% / {dynamic_mid_weightage}%")
    st.write(f"• Final Exam Weightage: {base_final_weightage}%")
