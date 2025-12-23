def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set 2\n")
    
    def q1():
        """What's the output?
        
        x = (1, 2, 3)
        y = list(x)
        y[0] = 4
        print(x[0])
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "1"
    
    def q2():
        """What prints?
        
        s = 'python'
        print(s.capitalize())
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "Python"
    
    def q3():
        """Result?
        
        d1 = {'a': 1}
        d2 = {'b': 2}
        d1.update(d2)
        print(d1)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{'a': 1, 'b': 2}"
    
    def q4():
        """Output?
        
        nums = [1, 2, 3, 4]
        print([x if x % 2 == 0 else 0 for x in nums])
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[0, 2, 0, 4]"
    
    def q5():
        """What's printed?
        
        def f(a, b=2):
            return a * b
        print(f(3))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "6"
    
    def q6():
        """Result?
        
        s = set([1, 2, 2, 3, 3, 3])
        print(len(s))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "3"
    
    def q7():
        """What prints?
        
        x = [1, 2, 3]
        y = x
        y += [4]
        print(x)
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4]"
    
    def q8():
        """Output?
        
        text = "hello"
        print(text[-2:] * 2)
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "lolo"
    
    def q9():
        """What's the result?
        
        d = dict(a=1, b=2)
        print(list(d.values()))
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q10():
        """Result?
        
        print(bool([]), bool([0]))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "False True"
    
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
