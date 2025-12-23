def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Python Mock Exam\n")
    
    def q1():
        """What's the output?
        
        x = "hello"
        y = x.replace('l', 'L', 1)
        print(y)
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "heLlo"
    
    def q2():
        """What's printed?
        
        d = {'x': 1, 'y': 2}
        d.update([('x', 3), ('z', 4)])
        print(d['x'], len(d))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "3 3"
    
    def q3():
        """Result of:
        
        lst = [1, 2, 3, 4]
        print(lst[-3::-1])
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 1]"
    
    def q4():
        """Output of:
        
        def f(lst=[]):
            lst.append(1)
            return lst
        print(f())
        print(f())
        """
        answer = input("\nQ4: What will be printed? (write both lines) ").strip()
        return answer == "[1] [1, 1]"
    
    def q5():
        """What prints?
        
        s = {1, 2, 3}
        s.update([3, 4], {5, 6})
        print(len(s))
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "6"
    
    def q6():
        """Result?
        
        x = [(1,2), (3,4)]
        print(x[0][1])
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "2"
    
    def q7():
        """Output?
        
        words = ['ab', 'cd', 'ef']
        print(''.join(sorted(words)[-2]))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "cd"
    
    def q8():
        """What's printed?
        
        for x in range(3):
            if x == 1:
                break
            print(x, end='')
        else:
            print('done')
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "0"
    
    def q9():
        """Result of:
        
        d = {'a': 1, 'b': 2}
        print(list(d.items())[0][1])
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "1"
    
    def q10():
        """Output?
        
        x = [[]] * 3
        x[0].append(1)
        print(x)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[[1], [1], [1]]"

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
        print("Excellent!")
    elif score >= 7:
        print("Good job!")
    elif score >= 5:
        print("Keep practicing!")
    else:
        print("More review needed!")
    
    return score

if __name__ == "__main__":
    run_mock_exam()
