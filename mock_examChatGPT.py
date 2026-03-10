
# 🔹 PCEP 50-Tricky Mock Exam (Interactive)
# Usage: Run in Jupyter Notebook or any Python IDE to test yourself

questions = [
    {"q": "What is the output of sum([True, False])?",
     "options": ["0", "1", "1", "2"],
     "answer": 1,
     "explanation": "True=1, False=0 → sum([True, False]) = 1"},

    {"q": "What is the output of the following code?\nfor i in range(2):\n    for j in range(2):\n        if j==1: break\n        else: print(i)",
     "options": ["0 1", "1 0", "0\n1", "1\n0"],
     "answer": 2,
     "explanation": "Break exits inner loop only. Outer loop continues. Output: 0\n1"},

    {"q": "What is the result of True + True?",
     "options": ["1", "2", "True", "False"],
     "answer": 1,
     "explanation": "True=1, so True + True = 2"},

    {"q": "What is the output of len([1,2,3][0:2])?",
     "options": ["2", "3", "0", "1"],
     "answer": 0,
     "explanation": "Slicing gives [1,2] → length = 2"},

    # ... Continue for all 50 questions ...
]

score = 0

for idx, q in enumerate(questions, 1):
    print(f"Q{idx}: {q['q']}")
    for i, option in enumerate(q['options']):
        print(f"  {i+1}) {option}")
    ans = input("Your answer (1-4): ")
    try:
        ans_idx = int(ans)-1
        if ans_idx == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['options'][q['answer']]}\n💡 {q['explanation']}")
    except:
        print(f"Invalid input. Correct answer: {q['options'][q['answer']]}\n💡 {q['explanation']}")
    print("---")

print(f"Your final score: {score}/{len(questions)}")
if score/len(questions) >= 0.7:
    print("🎉 You passed the PCEP mock exam!")
else:
    print("😢 You did not pass. Review tricky points and try again.")
