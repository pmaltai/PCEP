def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 9\n")
    
    def q1():
        """What will be the output of this code?
        
        x = "Hello"
        y = list(x)
        y[0] = 'h'
        print(''.join(y))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "hello"
    
    def q2():
        """What's the result of:
        
        x = {1: 'one', 2: 'two'}
        y = x.copy()
        y[1] = 'ONE'
        print(x[1])
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "one"
    
    def q3():
        """What will this output?
        
        nums = [1, 2, 3]
        nums.extend([4, [5, 6]])
        print(len(nums))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "5"
    
    def q4():
        """What will be printed?
        
        def modify(lst):
            lst += [4, 5]
            
        numbers = [1, 2, 3]
        modify(numbers)
        print(numbers)
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 5]"
    
    def q5():
        """What's the output of:
        
        s = set('hello')
        s.add('H')
        print(len(s))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "5"
    
    def q6():
        """What happens here?
        
        x = 'Python'
        print(x[::-2])
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "nhy"
    
    def q7():
        """Result of this operation?
        
        d = {'a': 1, 'b': 2}
        print('c' in d.keys())
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "False"
    
    def q8():
        """What's printed?
        
        for i in range(3):
            try:
                if i == 1:
                    raise ValueError
                print(i, end='')
            except ValueError:
                continue
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "02"
    
    def q9():
        """What happens in this code?
        
        x = [(1, 2), (3, 4)]
        y = x[:]
        y[0] = (5, 6)
        print(x[0])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "(1, 2)"
    
    def q10():
        """What's the output?
        
        def f(a=[], b={}):
            print(len(a) + len(b))
            
        f([1,2], {'x': 1})
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "3"
    
    # All questions
    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(question.__doc__)
        if question():
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    
    # Final score
    print(f"\nFinal Score: {score}/{total_questions}")
    print(f"Percentage: {(score/total_questions)*100}%")
    
    # Feedback based on score
    if score >= 9:
        print("Excellent! You're well prepared for PCEP!")
    elif score >= 7:
        print("Good job! Just a bit more practice needed!")
    elif score >= 5:
        print("Keep studying! Review the concepts you missed!")
    else:
        print("More practice needed. Focus on Python fundamentals!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
