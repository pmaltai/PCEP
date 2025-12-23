def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 15\n")
    
    def q1():
        """What's printed?
        
        nums = [1, 2, 3]
        result = map(lambda x: x*2, nums)
        print(list(result))
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 4, 6]"
    
    def q2():
        """String slicing:
        
        text = "Hello World"
        print(text[::2])
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "HloWrd"
    
    def q3():
        """List operations:
        
        x = [[1], [2]]
        y = x.copy()
        x[0][0] = 3
        print(y[0][0])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """What's the output?
        
        d = {'a': 1, 'b': 2}
        print(d.pop('a'), d)
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "1 {'b': 2}"
    
    def q5():
        """Function args:
        
        def f(*args, **kwargs):
            return len(args) + len(kwargs)
        print(f(1, x=2, y=3))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "3"
    
    def q6():
        """List comprehension:
        
        x = ['a', 'bb', 'ccc']
        print([len(i) for i in x if len(i) > 1])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 3]"
    
    def q7():
        """String methods:
        
        s = 'hello'
        print(s.upper().count('L'))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "2"
    
    def q8():
        """Set operations:
        
        a = {1, 2}
        b = {2, 3}
        print(sorted(a ^ b))
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3]"
    
    def q9():
        """Dictionary methods:
        
        d = dict(a=1, b=2)
        d.update([('b', 3), ('c', 4)])
        print(sum(d.values()))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "8"
    
    def q10():
        """Loop with else:
        
        for i in range(3):
            if i == 3:
                break
            print(i, end='')
        else:
            print('!')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "012!"

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
