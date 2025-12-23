def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 7\n")
    
    def q1():
        """What will be the output of this code?
        
        lst = [1, 2, 3]
        lst.extend([4, 5])
        lst.append([6, 7])
        print(len(lst))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "6"
    
    def q2():
        """What's the result of:
        
        x = "hello"
        y = x.replace('l', 'L', 1)
        print(y)
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "heLlo"
    
    def q3():
        """What will this output?
        
        d = {'x': 1}
        d['y'] = 2
        d.update(y=3)
        print(d['y'])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """What happens here?
        
        text = "Python"
        print(text[::-1].upper())
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "NOHTYP"
    
    def q5():
        """What's the output?
        
        nums = [1, 2, 3]
        squares = [x*x for x in nums]
        print(squares[-2])
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "4"
    
    def q6():
        """What will be printed?
        
        a = {1, 2}
        b = {2, 3}
        print(len(a ^ b))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "2"
    
    def q7():
        """Result of this operation?
        
        for i in range(3):
            if i == 1:
                continue
            print(i, end='')
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "02"
    
    def q8():
        """What happens in this code?
        
        def f(x, y=2):
            return x * y
            
        print(f(3))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "6"
    
    def q9():
        """What's printed?
        
        t = (1, 2, [3, 4])
        t[2][0] = 5
        print(t[2])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[5, 4]"
    
    def q10():
        """What's the output?
        
        s = "Python"
        for i in range(len(s)-1, -1, -2):
            print(s[i], end='')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "nhy"
    
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
        print("Excellent! You're well prepared!")
    elif score >= 7:
        print("Good job! Just a few topics to review!")
    elif score >= 5:
        print("Keep practicing! Focus on weak points!")
    else:
        print("More study needed. Review the basics!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
