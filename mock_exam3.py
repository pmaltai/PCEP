def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 4\n")
    
    def q1():
        """What will be the output of this code?
        
        nums = [1, [2, 3], 4]
        nums[1][0] = 5
        print(nums[1])
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[5, 3]"
    
    def q2():
        """What's the output of:
        
        text = "Hello"
        count = 0
        for letter in text:
            if letter.lower() in "aeiou":
                count += 1
        print(count)
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "2"
    
    def q3():
        """What will this produce?
        
        x = (1, 2, 3)
        y = list(x)
        y[1] = 5
        print(x)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "(1, 2, 3)"
    
    def q4():
        """What's the result of:
        
        d = {'a': 1, 'b': 2}
        d.update({'a': 3, 'c': 4})
        print(d['a'], len(d))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "3 3"
    
    def q5():
        """What happens here?
        
        x = [1, 2, 3]
        y = x
        x += [4]
        print(y)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4]"
    
    def q6():
        """What will be printed?
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(len(s1 & s2))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "1"
    
    def q7():
        """What's the output?
        
        lst = [1, 2, 3, 4]
        print(lst[-3::-1])
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 1]"
    
    def q8():
        """Result of this operation?
        
        print(2 ** 3 ** 2)
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "512"
    
    def q9():
        """What's printed?
        
        def func(x, y=None):
            if y is None:
                y = []
            y.append(x)
            return y
            
        print(func(1))
        print(func(2))
        """
        answer = input("\nQ9: What will be printed? (write both lines with space between) ").strip()
        return answer == "[1] [2]"
    
    def q10():
        """What happens in this code?
        
        try:
            x = [1, 2]
            print(x[3])
        except IndexError:
            print("Index")
        except Exception:
            print("Error")
        else:
            print("OK")
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "Index"
    
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
        print("Excellent! You're mastering Python fundamentals!")
    elif score >= 7:
        print("Good job! Just a few concepts to review!")
    elif score >= 5:
        print("You're making progress. Keep practicing!")
    else:
        print("More practice needed. Focus on Python basics!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
