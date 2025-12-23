def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 16\n")
    
    def q1():
        """Output?
        
        s = "python"
        print(s[::-2].upper())
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "NHY"
    
    def q2():
        """What prints?
        
        a = [1, 2]
        a.extend([3] * 2)
        print(a)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 3]"
    
    def q3():
        """Result?
        
        x = {"a": 1, "b": 2}
        y = x
        y["a"] = 3
        print(x["a"])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """Output of:
        
        def f(x=[]):
            x.append(1)
            return len(x)
        print(f(), f())
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "1 2"
    
    def q5():
        """List operations:
        
        lst = [1, 2, 3, 4]
        print(lst[1::2])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 4]"
    
    def q6():
        """Set methods:
        
        s = {1, 2, 3}
        s.update([3, 4], {5})
        print(len(s))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "5"
    
    def q7():
        """Function scope:
        
        x = 1
        def f():
            global x
            x = 2
        f()
        print(x)
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "2"
    
    def q8():
        """List comprehension:
        
        words = ['hi', 'hello', 'bye']
        print([w[0] for w in words])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "['h', 'h', 'b']"
    
    def q9():
        """String format:
        
        x = 42
        print(f"{x:03}")
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "042"
    
    def q10():
        """Loop control:
        
        i = 0
        while i < 5:
            i += 1
            if i == 3:
                continue
            if i == 4:
                break
            print(i, end='')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "12"

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
