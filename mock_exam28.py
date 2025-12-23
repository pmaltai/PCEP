def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 14\n")
    
    def q1():
        """Output?
        
        x = [1, 2, 3]
        y = list(x)
        y[0] = 10
        print(x)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q2():
        """Result?
        
        d = {'a': 1, 'b': 2}
        print('c' in d.keys())
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "False"
    
    def q3():
        """What prints?
        
        for i in range(3):
            try:
                if i == 1:
                    raise ValueError
                print(i, end='')
            except ValueError:
                continue
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "02"
    
    def q4():
        """List operation:
        
        nums = [1, 2, 3, 4, 5]
        print(nums[-2:1:-1])
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 3]"
    
    def q5():
        """String methods:
        
        text = "programming"
        print(text.capitalize().replace('m', 'M', 1))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "PrograMming"
    
    def q6():
        """Function output:
        
        def f(a, b=2, c=3):
            return a + b + c
        print(f(1, c=4))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "7"
    
    def q7():
        """Set operations:
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 & s2))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "1"
    
    def q8():
        """Dictionary methods:
        
        d = {'a': 1, 'b': 2}
        d.update({'a': 3, 'c': 4})
        print(sorted(d.values()))
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 3, 4]"
    
    def q9():
        """List comprehension:
        
        nums = range(5)
        print([x*2 for x in nums if x > 2])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[6, 8]"
    
    def q10():
        """Function scope:
        
        x = 1
        def change():
            x = 2
            return x
        change()
        print(x)
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "1"

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
