def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set 7\n")
    
    def q1():
        """What's the output?
        
        x = "Hello"
        y = "World"
        print(min(x.lower(), y.lower()))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "hello"
    
    def q2():
        """What prints?
        
        d = {'a': [1, 2], 'b': [3, 4]}
        d['a'].append(5)
        print(sum(d['a']))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "8"
    
    def q3():
        """Result?
        
        def f(x):
            return len(str(x))
        nums = [100, 2, 35]
        print(sorted(nums, key=f))
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 35, 100]"
    
    def q4():
        """Output?
        
        s = {1, 2, 3}
        s.update([3, 4], {4, 5})
        print(len(s))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "5"
    
    def q5():
        """What's printed?
        
        x = [1, 2, 3]
        y = x[:]
        y.reverse()
        print(x)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q6():
        """Result?
        
        text = "Python"
        print(''.join(sorted(text.lower())))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "hnopy"
    
    def q7():
        """What prints?
        
        def f(a, b, c=3):
            return a + b + c
        print(f(c=1, a=2, b=3))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "6"
    
    def q8():
        """Output?
        
        print(list(range(5, 0, -2)))
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[5, 3, 1]"
    
    def q9():
        """What's the result?
        
        a = [1, 2]
        b = [3, 4]
        print([*a, *b])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4]"
    
    def q10():
        """Result?
        
        d = dict.fromkeys(['a', 'b'], 0)
        d['a'] += 1
        print(d)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{'a': 1, 'b': 0}"
    
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
