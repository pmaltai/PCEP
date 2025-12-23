def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 20\n")
    
    def q1():
        """Output?
        
        x = [1, 2] * 2
        x[0] = 3
        print(x)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 2, 1, 2]"
    
    def q2():
        """Result?
        
        def f(lst=[]):
            lst.append(1)
            return lst
        print(f())
        print(f([2]))
        """
        answer = input("\nQ2: What will be printed? (write both lines) ").strip()
        return answer == "[1] [2, 1]"
    
    def q3():
        """What prints?
        
        d = {"x": 1, "y": 2}
        d.update(y=3, z=4)
        print(sum(d.values()))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "8"
    
    def q4():
        """String methods:
        
        text = "Python"
        print(text.lower().replace('p', 'P', 1))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "Python"
    
    def q5():
        """List operations:
        
        a = [1, [2, 3]]
        b = a.copy()
        b[1][0] = 4
        print(a[1][0])
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "4"
    
    def q6():
        """Set methods:
        
        s = set('hello')
        s.add('H')
        print(len(s))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "5"
    
    def q7():
        """Comprehension:
        
        d = {x: x**2 for x in range(3)}
        print(d[2])
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "4"
    
    def q8():
        """Function scope:
        
        x = 1
        def f():
            x = 2
            return x
        f()
        print(x)
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "1"
    
    def q9():
        """List slice:
        
        nums = range(1, 6)
        print(list(nums)[::2])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3, 5]"
    
    def q10():
        """String format:
        
        age = 25
        print(f"Age: {age:03d}")
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "Age: 025"

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
