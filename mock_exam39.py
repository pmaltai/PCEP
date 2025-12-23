def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set 5\n")
    
    def q1():
        """What's the output?
        
        lst = [1, 2, 3] * 2
        lst[0] = 4
        print(lst)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 2, 3, 1, 2, 3]"
    
    def q2():
        """What prints?
        
        s = "Hello"
        print(''.join(reversed(s)))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "olleH"
    
    def q3():
        """Result?
        
        d = {'a': 1, 'b': 2}
        x = d.get('c', 3)
        print(d.get('c', x))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """Output?
        
        def f(x):
            return x * 2
        print(list(map(f, filter(lambda x: x > 0, [-1, 0, 1, 2]))))
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 4]"
    
    def q5():
        """What's printed?
        
        x = {1, 2}
        y = {2, 3}
        print(x ^ y)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{1, 3}"
    
    def q6():
        """Result?
        
        x = 'abc'
        y = 123
        print(dict(zip(x, str(y))))
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{'a': '1', 'b': '2', 'c': '3'}"
    
    def q7():
        """What prints?
        
        def f(*args):
            return sum(args)
        print(f(1,2,3))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "6"
    
    def q8():
        """Output?
        
        s = "python"
        print(s[1:4:2])
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "yh"
    
    def q9():
        """What's the result?
        
        x = [[]] * 3
        x[0].append(1)
        print(x)
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[[1], [1], [1]]"
    
    def q10():
        """Result?
        
        d = {'x': 1, 'y': 2}
        print(sorted(d.items()))
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[('x', 1), ('y', 2)]"
    
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
