def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 10\n")
    
    def q1():
        """What will be printed?
        
        x = set('hello')
        y = list(x)
        y.sort()
        print(''.join(y))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "ehlo"
    
    def q2():
        """Output?
        
        lst = ['a', 'b', 'c']
        print(lst.pop(1), lst)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "b ['a', 'c']"
    
    def q3():
        """Result?
        
        d = {'a': 1, 'b': 2}
        d.update({'a': 3, 'c': 4})
        print(d['a'], len(d))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3 3"
    
    def q4():
        """What's printed?
        
        def outer(x):
            def inner(y):
                return x + y
            return inner
        print(outer(5)(3))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "8"
    
    def q5():
        """Output of:
        
        nums = [1, 2, 3, 4]
        print(nums[1:-1:2])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2]"
    
    def q6():
        """Print result:
        
        x = lambda a, b=2: a * b
        print(x(3))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "6"
    
    def q7():
        """What's shown?
        
        for i in range(1, 4):
            for j in range(i):
                print(i, end='')
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "122333"
    
    def q8():
        """Result of:
        
        a = [1, 2, 3]
        b = a
        a[1] = 4
        print(b)
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 4, 3]"
    
    def q9():
        """What prints?
        
        def f(x=[]):
            x.append(1)
            return sum(x)
        print(f())
        print(f())
        """
        answer = input("\nQ9: What will be printed? (write both lines) ").strip()
        return answer == "1 2"
    
    def q10():
        """Output?
        
        text = "Hello"
        print(text.replace('l', 'L', 1).lower())
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "heLlo"

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
