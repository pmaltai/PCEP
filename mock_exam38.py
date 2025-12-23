def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set 4\n")
    
    def q1():
        """What's the output?
        
        t = (1, 2, [3, 4])
        t[2][0] = 5
        print(t[2])
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[5, 4]"
    
    def q2():
        """What prints?
        
        text = "hello world"
        print(text.title())
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "Hello World"
    
    def q3():
        """Result?
        
        x = [1, 2, 3]
        print(x.pop(), x.pop(0))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3 1"
    
    def q4():
        """Output?
        
        x = set('hello')
        y = set('world')
        print(x & y)
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{'l', 'o'}"
    
    def q5():
        """What's printed?
        
        d = {'a': 1, 'b': 2}
        d.setdefault('c', 3)
        print(d['c'])
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "3"
    
    def q6():
        """Result?
        
        nums = [1, [2, 3], [4, 5]]
        print(sum(n[0] for n in nums[1:]))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "6"
    
    def q7():
        """What prints?
        
        x = 'abc'
        print(list(enumerate(x)))
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[(0, 'a'), (1, 'b'), (2, 'c')]"
    
    def q8():
        """Output?
        
        def f(x=1, y=2):
            return x + y
        print(f(y=3))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "4"
    
    def q9():
        """What's the result?
        
        x = ['a', 'b', 'c']
        y = [1, 2, 3]
        print(dict(zip(x, y)))
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{'a': 1, 'b': 2, 'c': 3}"
    
    def q10():
        """Result?
        
        s = 'python'
        print(s.center(8, '*'))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "*python*"
    
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
