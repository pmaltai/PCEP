def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Advanced Mock Exam 6\n")
    
    def q1():
        """Complex string operations:
        
        text = "Python3.9"
        print(''.join(sorted(text.lower().replace('.', ''))))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "39hnopty"
    
    def q2():
        """List comprehension with nested conditions:
        
        nums = range(10)
        result = [x for x in nums if x > 2 if x % 2 == 0 if x < 8]
        print(result)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 6]"
    
    def q3():
        """Function with keyword arguments and default values:
        
        def func(a, b=2, *, c=3):
            return a + b + c
        print(func(1, c=5))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "8"
    
    def q4():
        """Dictionary and set operations combined:
        
        d = {'a': 1, 'b': 2, 'c': 1}
        s = set(d.values())
        print(len(d), len(s))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "3 2"
    
    def q5():
        """String alignment and formatting:
        
        num = 42.1234
        print(f"|{num:^10.2f}|")
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "|  42.12   |"
    
    def q6():
        """List slicing with multiple operations:
        
        lst = [1, 2, 3, 4, 5]
        lst[1::2] = [10, 20]
        print(lst)
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 10, 3, 20, 5]"
    
    def q7():
        """Multiple exception handling:
        
        def divide(x, y):
            try:
                result = x / y
            except ZeroDivisionError:
                result = 'zero'
            except TypeError:
                result = 'type'
            return result
        print(divide(1, '2'))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "type"
    
    def q8():
        """Nested dictionary operations:
        
        d = {'x': {'y': 2}}
        d['x']['y'] = 3
        d['x']['z'] = 4
        print(sum(d['x'].values()))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "7"
    
    def q9():
        """String methods chaining:
        
        s = ' Python Programming '
        print(s.strip().replace('P', 'p').count('p'))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "2"
    
    def q10():
        """Generator expression and sum:
        
        data = [{'x': i} for i in range(3)]
        total = sum(item['x'] for item in data)
        print(total)
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "3"

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
