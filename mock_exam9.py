def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 10\n")
    
    def q1():
        """What will be printed?
        
        x = [1, 2, 3]
        y = x
        x = x + [4]
        print(y)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q2():
        """What will be printed?
        
        d = {"a": 1, "b": 2}
        e = d
        d.clear()
        print(len(e))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "0"
    
    def q3():
        """What will be printed?
        
        x = [[0]] * 3
        x[0][0] = 1
        print(x)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[[1], [1], [1]]"
    
    def q4():
        """What will be printed?
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 & s2))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "1"
    
    def q5():
        """What will be printed? Note the spaces.
        
        for i in range(5):
            if i == 3:
                continue
            print(i, end=' ')
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "0 1 2 4"
    
    def q6():
        """What will be printed?
        
        lst = [1, 2, 3, 4]
        print(lst[:-3:-1])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 3]"
    
    def q7():
        """What will be printed?
        
        def func(x, y=None):
            if y is None:
                y = []
            y.append(x)
            return y
        print(func(1))
        print(func(2))
        """
        answer = input("\nQ7: What will be printed? (write both lines with space between) ").strip()
        return answer == "[1] [2]"
    
    def q8():
        """What will be printed?
        
        a = [1, 2]
        b = [3, 4]
        print(a + b * 2)
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 3, 4]"
    
    def q9():
        """What will be printed?
        
        x = [1, 2, 3]
        y = x.copy()
        y.append(4)
        print(x)
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q10():
        """What will be printed?
        
        x = {1, 2, 3}
        y = {3, 4, 5}
        print(x | y)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{1, 2, 3, 4, 5}"
    
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
        print("Excellent! You're well prepared!")
    elif score >= 7:
        print("Good job! More practice needed!")
    elif score >= 5:
        print("Keep studying! Review missed concepts!")
    else:
        print("More practice needed. Focus on fundamentals!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
