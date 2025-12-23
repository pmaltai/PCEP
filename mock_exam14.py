def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 2 - Entry Level Python\n")
    
    def q1():
        """What's the output?
        
        x = 10
        y = 3
        print(x % y, x ** y)
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "1 1000"
    
    def q2():
        """What's printed?
        
        text = "Hello"
        print(text[-1:-4:-1])
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "oll"
    
    def q3():
        """Result of:
        
        numbers = [1, 2, 3]
        numbers *= 2
        print(numbers)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 1, 2, 3]"
    
    def q4():
        """Output?
        
        a = 5
        b = 3
        if a > b: print(a)
        else: print(b)
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "5"
    
    def q5():
        """What prints?
        
        count = 0
        while count < 3:
            count += 1
            if count == 2:
                continue
            print(count, end=' ')
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "1 3"
    
    def q6():
        """Result?
        
        def greeting(name='World'):
            return f'Hello {name}!'
        print(greeting())
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "Hello World!"
    
    def q7():
        """Output?
        
        text = 'Python'
        print(len(text), text.index('n'))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "6 5"
    
    def q8():
        """What prints?
        
        nums = list(range(1, 4))
        nums.reverse()
        print(nums)
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 2, 1]"
    
    def q9():
        """Result?
        
        def calc(a, b=2):
            return a * b
        print(calc(3))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "6"
    
    def q10():
        """Output?
        
        word = 'hello'
        print(word.replace('l', 'L', 1))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "heLlo"

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
    
    if score >= 9:
        print("Excellent! Ready for PCEP!")
    elif score >= 7:
        print("Good job! Almost ready!")
    elif score >= 5:
        print("Keep practicing!")
    else:
        print("Review fundamentals!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
