def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Mock Exam - Advanced Concepts\n")
    
    def q1():
        """What's the output?
        
        a = {1, 2, 3}
        b = {3, 4, 5}
        print(a ^ b)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{1, 2, 4, 5}"
    
    def q2():
        """Result of:
        
        x = [1, [2, 3], 4]
        y = x.copy()
        y[1][0] = 5
        print(x[1][0])
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "5"
    
    def q3():
        """Output?
        
        d = dict(zip('abc', range(3)))
        print(d.get('d', -1))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "-1"
    
    def q4():
        """What prints?
        
        def f(x=[]):
            x.extend([1])
            return x
        print(f())
        print(f([2]))
        print(f())
        """
        answer = input("\nQ4: What will be printed? (write each line) ").strip()
        return answer == "[1] [2, 1] [1, 1]"
    
    def q5():
        """Result?
        
        s = 'python'
        print(s.find('n'), s.index('n'))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "5 5"
    
    def q6():
        """Output of:
        
        lst = [1, 2, 3, 4, 5]
        print(lst[::2][-2:])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 5]"
    
    def q7():
        """What's printed?
        
        x = {1: 'one', 2: 'two'}
        y = dict(x.items())
        y[1] = 'ONE'
        print(x[1])
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "one"
    
    def q8():
        """Result of:
        
        def gen():
            for i in range(3):
                yield i
        print(list(gen())[1:])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q9():
        """Output?
        
        a = 'hello'
        b = 'world'
        print(''.join(sorted(set(a) & set(b))))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "lo"
    
    def q10():
        """What prints?
        
        x = [[], [], []]
        x[1].append(1)
        print(x)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[[], [1], []]"

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
