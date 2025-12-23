def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Institute PCEP Mock Exam - Set 6\n")
    
    def q1():
        """What will be the output of this code?
        
        x = 2
        y = 1
        x, y = y, x + y
        print(x, y)
        """
        answer = input("\nQ1: What will be printed? (separate numbers with space) ").strip()
        return answer == "1 3"
    
    def q2():
        """What's the result of:
        
        text = "hello"
        print(text[::2] + text[1::2])
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "hloel"
    
    def q3():
        """What will this output?
        
        a = [1, 2]
        b = a
        a += [3]
        print(b)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q4():
        """What happens here?
        
        d = {"a": 1, "b": 2}
        e = d
        d.clear()
        print(len(e))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "0"
    
    def q5():
        """What's the output?
        
        def func(x, y):
            return x if x > y else y
            
        print(func(3, 4))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "4"
    
    def q6():
        """What will be printed?
        
        s = "Python"
        t = reversed(s)
        print(''.join(t))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "nohtyP"
    
    def q7():
        """Result of this operation?
        
        x = {1, 2, 3}
        y = {3, 4, 5}
        print(x | y)
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{1, 2, 3, 4, 5}"
    
    def q8():
        """What happens in this code?
        
        x = [i * 2 for i in range(3)]
        print(x[1:] + x[:1])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 4, 0]"
    
    def q9():
        """What's printed?
        
        def f(lst=[]):
            for i in range(len(lst)):
                lst[i] += 1
            return lst
            
        print(f([1, 2, 3]))
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 3, 4]"
    
    def q10():
        """What's the output?
        
        a = {'x': 1, 'y': 2}
        b = dict(x=1, y=2)
        print(a == b)
        """
        answer = input("\nQ10: What will be printed? (True/False) ").strip()
        return answer.lower() == "true"
    
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
        print("Excellent! You're ready for PCEP!")
    elif score >= 7:
        print("Good job! Review the topics you missed!")
    elif score >= 5:
        print("Keep practicing! Focus on weak areas!")
    else:
        print("More study needed. Review the basics!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
