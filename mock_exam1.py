def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 2\n")
    
    def q1():
        """What will be the output of this code?
        
        x = 5
        y = 2
        print(x // y, x / y)
        """
        answer = input("\nQ1: What will be printed? (separate numbers with space) ").strip()
        return answer == "2 2.5"
    
    def q2():
        """What's the result of this operation?
        
        text = "hello"
        text = text.upper()[:3]
        print(text)
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "HEL"
    
    def q3():
        """What will this code produce?
        
        numbers = (1, 2, 3)
        numbers[0] = 4
        print(numbers)
        """
        answer = input("\nQ3: What will happen? ").strip().lower()
        return "error" in answer or "exception" in answer or "typeerror" in answer
    
    def q4():
        """What's the output of:
        
        d = dict(a=1, b=2)
        d['c'] = 3
        print(d.keys())
        """
        answer = input("\nQ4: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "dict_keys(['a', 'b', 'c'])"
    
    def q5():
        """What will be printed?
        
        lst = [1, 2, 3, 4]
        print(lst[-2::-2])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[3, 1]"
    
    def q6():
        """What's the output of this code?
        
        a = 2
        b = 1
        print(a > b and b > 0 or a < 5)
        """
        answer = input("\nQ6: What will be printed? (True/False) ").strip()
        return answer.lower() == "true"
    
    def q7():
        """What value will this return?
        
        text = "Python"
        count = 0
        for char in text:
            if char.lower() in "aeiou":
                count += 1
        print(count)
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "1"
    
    def q8():
        """What will this print?
        
        numbers = [1, 2, 3]
        result = [str(n) * 2 for n in numbers]
        print(result)
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "['11', '22', '33']"
    
    def q9():
        """What's the output of:
        
        def func(a, b=2, c=3):
            return a + b + c
            
        print(func(1, c=5))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "8"
    
    def q10():
        """What happens in this code?
        
        try:
            print(int("abc"))
        except ValueError:
            print("Value")
        except TypeError:
            print("Type")
        else:
            print("OK")
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "Value"
    
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
        print("Excellent! You're ready for the exam!")
    elif score >= 7:
        print("Good job! Just a bit more practice needed!")
    elif score >= 5:
        print("Keep practicing! Review the topics you missed.")
    else:
        print("More study recommended. Focus on Python basics!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
