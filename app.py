# --- User Inputs (Aapke Marks) ---
# Quizzes (Total: 10 marks each)
q1, q2, q3 = 3, 4, 10

# Assignments (Total: 10 marks each)
as1, as2, as3 = 10, 10, 9

# Mid-Term (Total: 25 marks)
mid_marks = 10

# Target Passing Percentage (E.g., 50%)
passing_target = 50

# --- Weightage Calculations ---
# 1. Quizzes (15% Weightage)
total_quiz_obtained = q1 + q2 + q3
quiz_weightage = (total_quiz_obtained / 30) * 15

# 2. Assignments (20% Weightage)
total_as_obtained = as1 + as2 + as3
assignment_weightage = (total_as_obtained / 30) * 20

# 3. Mid-Term (25% Weightage)
mid_weightage = (mid_marks / 25) * 25

# Total Sessional Weightage (Out of 60%)
current_total_percentage = quiz_weightage + assignment_weightage + mid_weightage

# --- Finals Target Calculation ---
# Final exam 50 marks ka hai aur weightage 40% hai
needed_percentage = passing_target - current_total_percentage
required_final_marks = (needed_percentage / 40) * 50

# --- Output Results ---
print("="*40)
print("       MARKS & WEIGHTAGE REPORT       ")
print("="*40)
print(f"Quizzes Weightage (Out of 15%):     {quiz_weightage:.2f}%")
print(f"Assignments Weightage (Out of 20%): {assignment_weightage:.2f}%")
print(f"Mid-Term Weightage (Out of 25%):    {mid_weightage:.2f}%")
print("-"*40)
print(f"Ab tak ka Total Score (Out of 60%): {current_total_percentage:.2f}%")
print("="*40)

if required_final_marks <= 0:
    print("Mubarak ho! Aap Finals se pehle hi overall paas ho chuke hain!")
elif required_final_marks > 50:
    print("Sorry! 50% target tak pohnchna ab possible nahi hai.")
else:
    print(f"Paas hone ke liye Final Exam (50 marks) mein se kam az kam:")
    print(f"👉 {required_final_marks:.2f} Marks chahiye hain.")
print("="*40)
