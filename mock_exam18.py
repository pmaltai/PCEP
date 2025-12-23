def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 4\n")
    
    def q1():
        """What's the output?
        
        x = [1, 2, 3]
        y = x.copy()
        y[0] = 10
        print(x)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q2():
        """What prints?
        
        text = "Hello World"
        print(text.swapcase())
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "hELLO wORLD"
    
    def q3():
        """Result of:
        
        def func(x=[]):
            x.append(1)
            return x
        print(func())
        print(func())
        """
        answer = input("\nQ3: What will be printed? (write each line) ").strip()
        return answer == "[1] [1, 1]"
    
    def q4():
        """Output?
        
        nums = range(1, 5)
        print(list(map(lambda x: x**2, nums)))
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 4, 9, 16]"
    
    def q5():
        """What prints?
        
        d = {'a': 1, 'b': 2}
        for k, v in sorted(d.items()):
            print(k + str(v), end='')
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "a1b2"
    
    def q6():
        """Result?
        
        numbers = [1, 2, 3, 4]
        print(numbers[-2::-2])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 1]"
    
    def q7():
        """Output of:
        
        def divide(a, b=2):
            try:
                return a/b
            except:
                return 0
        print(divide(10, 0))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "0"
    
    def q8():
        """What's printed?
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 | s2))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "5"
    
    def q9():
        """Result of:
        
        x = [[1, 2], [3, 4]]
        print([i[0] for i in x])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3]"
    
    def q10():
        """Output?
        
        import math
        print(round(math.pi, 2))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "3.14"

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
    
    return score

if __name__ == "__main__":
    run_mock_exam()
