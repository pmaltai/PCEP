def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam\n")
    
    def q1():
        """What will be the output of this code?
        
        x = [1, 2, 3]
        y = x
        y.append(4)
        print(x)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4]"
    
    def q2():
        """What is the output of:
        
        for i in range(-2, 3, 2):
            print(i, end=' ')
        """
        answer = input("\nQ2: What numbers will be printed? (space-separated) ").strip()
        return answer == "-2 0 2"
    
    def q3():
        """What will this code produce?
        
        def func(x, y=10):
            return x + y
            
        print(func(5))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "15"
    
    def q4():
        """What's the output of this code?
        
        text = "Python"
        print(text[-4:-2])
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "th"
    
    def q5():
        """What will this list comprehension produce?
        
        numbers = [x**2 for x in range(4) if x % 2 == 0]
        print(numbers)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[0, 4]"
    
    def q6():
        """What's the output of:
        
        d = {"a": 1, "b": 2}
        print(d.get("c", 3))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "3"
    
    def q7():
        """What will be printed?
        
        try:
            x = 1 / 0
        except ZeroDivisionError:
            print("A")
        finally:
            print("B")
        """
        answer = input("\nQ7: What will be printed? (space-separated) ").strip()
        return answer.upper() == "A B"
    
    def q8():
        """What's the result of this operation?
        
        x = True
        y = False
        z = False
        print(x or y and z)
        """
        answer = input("\nQ8: What will be printed? (True/False) ").strip()
        return answer.lower() == "true"
    
    def q9():
        """What will this code output?
        
        def greet(name="Guest"):
            return f"Hello, {name}!"
            
        print(greet())
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "Hello, Guest!"
    
    def q10():
        """What's the output of:
        
        fruits = ['apple', 'banana', 'cherry']
        print(fruits[:-2:-1])
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "['cherry']"
    
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
        print("Excellent! You're well prepared!")
    elif score >= 7:
        print("Good job! Keep practicing!")
    elif score >= 5:
        print("You're on the right track, but need more practice.")
    else:
        print("More study needed. Focus on the basics!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
