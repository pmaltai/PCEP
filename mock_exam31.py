def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 17\n")
    
    def q1():
        """What's printed?
        
        text = "Python"
        print(text.center(8, '*'))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "*Python*"
    
    def q2():
        """Result?
        
        x = [1, 2]
        y = x
        x += [3]
        print(y)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q3():
        """Output?
        
        def f(a=[], b={}):
            print(len(a) + len(b))
        f([1,2], {'x': 1})
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """What's shown?
        
        d = {"x": 1, "y": 2}
        print(list(d.items())[0][1])
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "1"
    
    def q5():
        """List operations:
        
        nums = [0, 1, 2, 3]
        print(nums[-3::-1])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 0]"
    
    def q6():
        """String methods:
        
        s = "hello world"
        print(s.title().swapcase())
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "hELLO wORLD"
    
    def q7():
        """Comprehension:
        
        x = {i for i in range(5) if i % 2}
        print(sorted(x))
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3]"
    
    def q8():
        """Function output:
        
        def f(x, y=5):
            return x + y
        print(f(3, y=2))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "5"
    
    def q9():
        """Dict operations:
        
        d = {'a': 1, 'b': 2}
        print(d.get('c', 0) + d['b'])
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "2"
    
    def q10():
        """Loop control:
        
        x = 0
        while x < 3:
            x += 1
            if x == 2:
                continue
            print(x, end='')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "13"

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
