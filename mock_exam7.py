def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 8\n")
    
    def q1():
        """What will be the output of this code?
        
        x = [1, 2, 3]
        y = x[1:]
        y[0] = 5
        print(x)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q2():
        """What's the result of:
        
        s = 'hello'
        print(s.find('l'), s.rfind('l'))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "2 3"
    
    def q3():
        """What will this output?
        
        d = {'a': 1, 'b': 2}
        x = d.setdefault('c', 3)
        print(x)
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """What will be printed?
        
        a = [1, 2]
        b = a * 2
        b[0] = 3
        print(a)
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q5():
        """What's the output of:
        
        def f(x):
            x += 2
            return x
        
        y = 5
        f(y)
        print(y)
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "5"
    
    def q6():
        """What happens here?
        
        nums = set([1, 2, 3])
        nums.update([3, 4])
        print(len(nums))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "4"
    
    def q7():
        """Result of this operation?
        
        x = "Python"
        print(x[1:4:2])
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "yh"
    
    def q8():
        """What's printed?
        
        i = 0
        while i < 3:
            i += 1
            if i == 2:
                continue
            print(i, end='')
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "13"
    
    def q9():
        """What happens in this code?
        
        t = ([1, 2], [3, 4])
        t[0].append(5)
        print(t[0])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 5]"
    
    def q10():
        """What's the output?
        
        nums = [1, 2, 3, 4]
        print(nums[-3:][::-1])
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 3, 2]"
    
    # All questions
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(question.__doc__)
        if question():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    
    # Final score
    print(f"\nFinal Score: {score}/{total_questions}")
    print(f"Percentage: {(score/total_questions)*100}%")
    
    # Feedback based on score
    if score >= 9:
        print("Excellent! Keep up the great work!")
    elif score >= 7:
        print("Good job! Review the topics you missed!")
    elif score >= 5:
        print("Keep practicing! Focus on understanding each concept!")
    else:
        print("More practice needed. Review Python fundamentals!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
