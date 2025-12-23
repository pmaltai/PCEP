def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 18\n")
    
    def q1():
        """What prints?
        
        x = {"a": 1, "b": 2}
        y = dict(x)
        y["a"] = 3
        print(x["a"])
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "1"
    
    def q2():
        """Output?
        
        lst = [1, [2, 3], 4]
        lst[1][0] = 5
        print(lst)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, [5, 3], 4]"
    
    def q3():
        """Result?
        
        def f(x, y=[]):
            y.append(x)
            return y
        print(f(1), f(2))
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2] [1, 2]"
    
    def q4():
        """String format:
        
        num = 42.1234
        print(f"{num:.2f}")
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "42.12"
    
    def q5():
        """Set operation:
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 | s2))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "5"
    
    def q6():
        """List slice:
        
        nums = [1, 2, 3, 4]
        print(nums[-2::-2])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 1]"
    
    def q7():
        """Dict method:
        
        d = {'a': 1, 'b': 2}
        print(d.pop('a', 0), d.pop('c', 0))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "1 0"
    
    def q8():
        """List comprehension:
        
        print([i*2 for i in range(4) if i > 1])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 6]"
    
    def q9():
        """String methods:
        
        s = ' Python '
        print(s.strip().replace('P', 'p'))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "python"
    
    def q10():
        """Function scope:
        
        def outer(x):
            def inner():
                return x
            return inner()
        print(outer(5))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "5"

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
