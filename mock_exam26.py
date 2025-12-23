def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 12\n")
    
    def q1():
        """What's printed?
        
        nums = [1, 2, 3]
        nums.insert(1, nums.pop())
        print(nums)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3, 2]"
    
    def q2():
        """Output?
        
        def func(x, y=[]):
            y.append(x)
            return y
        print(func(1), func(2))
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2] [1, 2]"
    
    def q3():
        """Result?
        
        s = set('hello')
        s.add('h')
        print(len(s))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "4"
    
    def q4():
        """What prints?
        
        x = 'Python'
        print(x[1:4:2])
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "yh"
    
    def q5():
        """Dictionary operations:
        
        d = {'a': 1, 'b': 2}
        x = d.setdefault('c', 3)
        print(x, d['c'])
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "3 3"
    
    def q6():
        """List operations:
        
        a = [1, 2]
        b = [3, 4]
        print(a + b * 2)
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 3, 4]"
    
    def q7():
        """String methods:
        
        text = 'Python'
        print(text.replace('n', 'N').lower())
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "python"
    
    def q8():
        """Function scope:
        
        def outer(x):
            def inner():
                return x + 1
            return inner()
        print(outer(5))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "6"
    
    def q9():
        """List comprehension:
        
        matrix = [[1,2], [3,4]]
        print([j for i in matrix for j in i if j < 3])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q10():
        """Exception handling:
        
        try:
            print(1/0)
        except:
            print('error')
        else:
            print('ok')
        finally:
            print('done')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "error done"

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
