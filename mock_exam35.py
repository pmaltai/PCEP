def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam - Practice Set\n")
    
    def q1():
        """What's the output?
        
        x = [1, 2, 3]
        y = x.copy()
        y[0] = 10
        print(x)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q2():
        """What prints?
        
        text = "Hello World"
        print(text.swapcase())
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "hELLO wORLD"
    
    def q3():
        """What's printed?
        
        d = {"x": 1, "y": 2}
        d["x"] = d.get("z", 3)
        print(d["x"])
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "3"
    
    def q4():
        """Output?
        
        nums = range(1, 5)
        print(list(map(lambda x: x**2, nums)))
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 4, 9, 16]"
    
    def q5():
        """What's the result?
        
        def func(a, b=[]): 
            b.append(a)
            return b
        print(func(1), func(2))
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2] [1, 2]"
    
    def q6():
        """What prints?
        
        nums = [1, 2, 3, 4, 5]
        print(nums[::2])
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3, 5]"
    
    def q7():
        """Result?
        
        a = {1, 2, 3}
        b = {2, 3, 4}
        print(a & b)
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{2, 3}"
    
    def q8():
        """What's printed?
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 | s2))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "5"
    
    def q9():
        """Output?
        
        lst = [[1, 2], [3, 4]]
        print([x[0] for x in lst])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3]"
    
    def q10():
        """String slicing:
        
        word = "Programming"
        print(word[::2].lower())
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "prgamg"
    
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
