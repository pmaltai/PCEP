def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set 3\n")
    
    def q1():
        """What's the output?
        
        def fun(x, y=[]):
            y.extend([x])
            return y
        print(fun(1), fun(2))
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2] [1, 2]"
    
    def q2():
        """What prints?
        
        x = "hello"
        print(x.find('l'), x.rfind('l'))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "2 3"
    
    def q3():
        """Result?
        
        a = [1, 2, [3, 4]]
        b = list(a)
        b[2][0] = 5
        print(a[2][0])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "5"
    
    def q4():
        """Output?
        
        print({x: x**2 for x in range(3)})
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{0: 0, 1: 1, 2: 4}"
    
    def q5():
        """What's printed?
        
        s1 = {1, 2, 3}
        s2 = {2, 3, 4}
        print(s1 - s2)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{1}"
    
    def q6():
        """Result?
        
        x = [1, 2, 3]
        x.extend([4])
        x.append([5])
        print(len(x))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "5"
    
    def q7():
        """What prints?
        
        d = {'a': 1, 'b': 2}
        print(list(d.items())[0])
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "('a', 1)"
    
    def q8():
        """Output?
        
        text = "Python"
        print(text[::-2])
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "nhy"
    
    def q9():
        """What's the result?
        
        def f(x):
            return x > 2
        print(list(filter(f, [1,2,3,4])))
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 4]"
    
    def q10():
        """Result?
        
        x = [1, 2, 3]
        y = reversed(x)
        print(list(y))
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 2, 1]"
    
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
