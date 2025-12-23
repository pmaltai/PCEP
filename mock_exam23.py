def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 9\n")
    
    def q1():
        """What's the output?
        
        text = "Hello123"
        print(text.rstrip('123').upper())
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "HELLO"
    
    def q2():
        """List operations:
        
        a = [1, 2]
        a *= 2
        a[0] = 3
        print(a)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 2, 1, 2]"
    
    def q3():
        """Function scope:
        
        x = 1
        def outer():
            x = 2
            def inner():
                nonlocal x
                x = 3
            inner()
            return x
        print(outer(), x)
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3 1"
    
    def q4():
        """Dictionary comprehension:
        
        keys = ['a', 'b']
        values = [1, 2]
        d = {k:v for k, v in zip(keys, values)}
        print(d['b'])
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "2"
    
    def q5():
        """List slicing:
        
        nums = list(range(1, 6))
        print(nums[-2:1:-1])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 3]"
    
    def q6():
        """Function with *args:
        
        def sum_all(*args, extra=0):
            return sum(args) + extra
        print(sum_all(1, 2, extra=3))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "6"
    
    def q7():
        """Set operations:
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 | s2))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "5"
    
    def q8():
        """String formatting:
        
        name = "Python"
        version = 3.9
        print(f"{name:>10} {version:.1f}")
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "    Python 3.9"
    
    def q9():
        """List comprehension:
        
        x = [[1,2], [3,4]]
        print([elem for row in x for elem in row if elem > 2])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 4]"
    
    def q10():
        """Exception handling:
        
        try:
            x = int('a')
        except ValueError:
            x = -1
        finally:
            x += 1
        print(x)
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "0"

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
