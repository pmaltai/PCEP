def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 19\n")
    
    def q1():
        """What prints?
        
        text = "Python3.9"
        print(''.join(sorted(text.lower())))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == ".39hnopy"
    
    def q2():
        """Output?
        
        a = [1, 2]
        b = [3, 4]
        a.extend(b * 2)
        print(a)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 3, 4]"
    
    def q3():
        """Result?
        
        d = {"a": 1, "b": 2}
        x = d.setdefault("c", 3)
        print(x, d["c"])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3 3"
    
    def q4():
        """List comp output?
        
        nums = [1, 2, 3, 4]
        print([x for x in nums if x % 2])
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3]"
    
    def q5():
        """What's the result?
        
        s = {1, 2}
        s.update([2, 3], {4})
        print(sorted(s))
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4]"
    
    def q6():
        """Function output:
        
        def f(a, b=None):
            if b is None:
                b = []
            b.append(a)
            return b
        print(f(1), f(2))
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1] [2]"
    
    def q7():
        """String methods:
        
        s = "hello WORLD"
        print(s.swapcase().capitalize())
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "Hello world"
    
    def q8():
        """List slice:
        
        nums = list(range(1, 6))
        print(nums[::2])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3, 5]"
    
    def q9():
        """Dict operations:
        
        d = {"a": 1, "b": 2}
        print(d.get("c", 3) + d.get("b", 0))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "5"
    
    def q10():
        """Loop with break:
        
        for i in range(5):
            if i > 2:
                break
            print(i, end='')
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "012"

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
