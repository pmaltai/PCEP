def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 3\n")
    
    def q1():
        """What will be the output of this code?
        
        x = "Hello"
        print(x[1:-1:2])
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "el"
    
    def q2():
        """What's the result of this operation?
        
        a = [1, 2]
        b = [3, 4]
        print(a + b * 2)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 3, 4]"
    
    def q3():
        """What will this code produce?
        
        x = {1: 'one', 2: 'two'}
        x[1] = 'ONE'
        x[3] = 'three'
        print(len(x))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """What's the output of:
        
        text = "python"
        print(text[::-2].upper())
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "NHY"
    
    def q5():
        """What will be printed?
        
        def func(x=[]):
            x.append(1)
            return x
        
        print(func())
        print(func())
        """
        answer = input("\nQ5: What will be printed? (write both lines with space between) ").strip()
        return answer == "[1] [1, 1]"
    
    def q6():
        """What's the output of this code?
        
        x = 1
        y = 0
        print(bool(x) or bool(y))
        """
        answer = input("\nQ6: What will be printed? (True/False) ").strip()
        return answer.lower() == "true"
    
    def q7():
        """What will this return?
        
        nums = {1, 2, 3}
        nums.add(2)
        nums.add(4)
        print(len(nums))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "4"
    
    def q8():
        """What will this code output?
        
        a = ((1, 2), [3, 4])
        a[1][0] = 5
        print(a)
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "((1, 2), [5, 4])"
    
    def q9():
        """What's printed by this code?
        
        i = 5
        while i > 0:
            if i == 2:
                break
            print(i, end=' ')
            i -= 1
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "5 4 3"
    
    def q10():
        """What happens in this code?
        
        lst = ['a', 'b', 'c']
        print(lst.pop(1), lst)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "b ['a', 'c']"
    
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
        print("Outstanding! You're well prepared for PCEP!")
    elif score >= 7:
        print("Good work! Just need to polish a few concepts!")
    elif score >= 5:
        print("Getting there! Focus on the topics you missed.")
    else:
        print("Keep studying! Review Python fundamentals.")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
