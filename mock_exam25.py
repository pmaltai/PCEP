def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 11\n")
    
    def q1():
        """What's the output?
        
        text = "Python3.9"
        print(''.join(sorted(text.lower().replace('.', ''))))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "3hnopy9"
    
    def q2():
        """Output?
        
        a = [1, 2, 3]
        b = a.copy()
        b.append(4)
        print(sum(a))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "6"
    
    def q3():
        """Result?
        
        d = {'one': 1, 'two': 2}
        print(list(d.keys())[0])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "one"
    
    def q4():
        """What prints?
        
        def func(x, y=5):
            return x * y
        print(func(2))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "10"
    
    def q5():
        """List slicing:
        
        lst = [1, 2, 3, 4, 5]
        print(lst[-3::-1])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 2, 1]"
    
    def q6():
        """String methods:
        
        s = 'hello WORLD'
        print(s.swapcase())
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "HELLO world"
    
    def q7():
        """List comprehension:
        
        nums = range(5)
        print([x*2 for x in nums if x > 2])
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[6, 8]"
    
    def q8():
        """Set operations:
        
        s1 = {1, 2, 3}
        s2 = {2, 3, 4}
        print(len(s1 & s2))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "2"
    
    def q9():
        """Function scope:
        
        x = 1
        def f():
            x = 2
            return x
        f()
        print(x)
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "1"
    
    def q10():
        """Dictionary methods:
        
        d = {'a': 1, 'b': 2}
        print(d.get('c', 3))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "3"

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
