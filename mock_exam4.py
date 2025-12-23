def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 5\n")
    
    def q1():
        """What will be the output of this code?
        
        x = "hello"
        print(x[-2:] * 2)
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "lolo"
    
    def q2():
        """What's the result of:
        
        d = {'a': 1, 'b': 2}
        print(list(d.values()))
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q3():
        """What will be printed?
        
        nums = set([1, 2, 2, 3, 3, 3])
        print(len(nums))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """What's the output of:
        
        x = [[0]] * 3
        x[0][0] = 1
        print(x)
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[[1], [1], [1]]"
    
    def q5():
        """What happens here?
        
        text = "Python"
        print(''.join(sorted(text.lower())))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "hnopy"
    
    def q6():
        """Result of this operation?
        
        a = True
        b = False
        c = True
        print(not a or b and c)
        """
        answer = input("\nQ6: What will be printed? (True/False) ").strip()
        return answer.lower() == "false"
    
    def q7():
        """What's printed?
        
        x = [1, 2, 3]
        y = x.copy()
        y.append(4)
        print(x)
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q8():
        """What will this code output?
        
        def func(a, b=2, c=3):
            return a + b + c
        
        print(func(b=4, c=5, a=1))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "10"
    
    def q9():
        """What's the result?
        
        lst = [1, 2, 3, 4]
        print(lst[:-3:-1])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 3]"
    
    def q10():
        """What happens in this code?
        
        for i in range(5):
            if i == 3:
                continue
            print(i, end=' ')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "0 1 2 4"
    
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
        print("Excellent! You're very well prepared!")
    elif score >= 7:
        print("Good job! Keep practicing specific areas!")
    elif score >= 5:
        print("You're making progress. Focus on weak points!")
    else:
        print("More practice needed. Review core concepts!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
