def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Entry Level Python\n")
    
    def q1():
        """What's the output?
        
        x = 5
        y = 2
        print(x // y, x / y)
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "2 2.5"
    
    def q2():
        """What prints?
        
        x = [1, 2, 3]
        print(x[:-1])
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q3():
        """Result of:
        
        text = "Python"
        print(text[1:4])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "yth"
    
    def q4():
        """Output?
        
        x = True
        y = False
        print(x and y or x)
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "True"
    
    def q5():
        """What prints?
        
        for i in range(3):
            print(i, end=' ')
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "0 1 2"
    
    def q6():
        """Result?
        
        x = 10
        while x > 5:
            x -= 2
            if x == 6:
                continue
            print(x, end=' ')
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "8 4"
    
    def q7():
        """Output?
        
        def func(x=1, y=2):
            return x + y
        print(func(y=3))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "4"
    
    def q8():
        """What prints?
        
        lst = [1, 2, 3]
        lst.append(4)
        lst.insert(1, 5)
        print(lst)
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 5, 2, 3, 4]"
    
    def q9():
        """Result?
        
        text = "Hello"
        print(text.lower().count('l'))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "2"
    
    def q10():
        """Output?
        
        x = input("Enter: ")
        print(type(x))
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "<class 'str'>"

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(question.__doc__)
        if question():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    
    print(f"\nFinal Score: {score}/{total_questions}")
    print(f"Percentage: {(score/total_questions)*100}%")
    
    if score >= 9:
        print("Excellent! Ready for PCEP!")
    elif score >= 7:
        print("Good job! Review a few concepts!")
    elif score >= 5:
        print("More practice needed!")
    else:
        print("Focus on Python fundamentals!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
