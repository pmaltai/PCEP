def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set 6\n")
    
    def q1():
        """What's the output?
        
        a = [1, 2, 3]
        print(a[::-1].copy())
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 2, 1]"
    
    def q2():
        """What prints?
        
        d = {'a': 1, 'b': 2}
        e = {'b': 3, 'c': 4}
        d.update(e)
        print(d['b'])
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "3"
    
    def q3():
        """Result?
        
        words = ['cat', 'dog', 'bird']
        print(sorted(words, key=len))
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "['cat', 'dog', 'bird']"
    
    def q4():
        """Output?
        
        s = set('hello')
        s.add('w')
        s.remove('h')
        print(len(s))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "4"
    
    def q5():
        """What's printed?
        
        def outer():
            x = 1
            def inner():
                nonlocal x
                x = 2
            inner()
            return x
        print(outer())
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "2"
    
    def q6():
        """Result?
        
        nums = [1, 2, 3, 4]
        print([num if num % 2 == 0 else 0 for num in nums])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[0, 2, 0, 4]"
    
    def q7():
        """What prints?
        
        x = 'python'
        print(x.rjust(8, '*'))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "**python"
    
    def q8():
        """Output?
        
        t = ([1, 2], [3, 4])
        t[0][0] = 5
        print(t[0])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[5, 2]"
    
    def q9():
        """What's the result?
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(s1.intersection(s2))
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{3}"
    
    def q10():
        """Result?
        
        def f(**kwargs):
            return len(kwargs)
        print(f(a=1, b=2))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "2"
    
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
