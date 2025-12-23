def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 7\n")
    
    def q1():
        """What prints? (Multiple string methods)
        
        text = "Python123"
        print(text.isalnum(), text.isalpha())
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "True False"
    
    def q2():
        """List modification:
        
        lst = [1, [2, 3], 4]
        lst[1].extend([5])
        print(lst)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, [2, 3, 5], 4]"
    
    def q3():
        """Dictionary comprehension with condition:
        
        d = {x: x**2 for x in range(5) if x % 2 == 0}
        print(sorted(d.values()))
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[0, 4, 16]"
    
    def q4():
        """Function args and scope:
        
        x = 1
        def func(x=[]):
            x.append(1)
            return x
        print(func([2]))
        print(func())
        """
        answer = input("\nQ4: What will be printed? (write both lines) ").strip()
        return answer == "[2, 1] [1]"
    
    def q5():
        """Set operations:
        
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        print(sorted(s1 ^ s2))
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 4, 5]"
    
    def q6():
        """String formatting with f-strings:
        
        name = "Bob"
        score = 95.5
        print(f"{name:>10} got {score:.1f}%")
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "       Bob got 95.5%"
    
    def q7():
        """List slicing:
        
        numbers = list(range(1, 6))
        print(numbers[3:0:-2])
        """
        answer = input("\nQ7: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 2]"
    
    def q8():
        """Exception handling in loop:
        
        total = 0
        for i in ['1', '2', 'three', '4']:
            try:
                total += int(i)
            except ValueError:
                continue
        print(total)
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "7"
    
    def q9():
        """Nested loops with break:
        
        result = 0
        for i in range(3):
            for j in range(i):
                result += 1
                if result > 2:
                    break
            print(result, end='')
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "012"
    
    def q10():
        """Dictionary methods:
        
        d = {'a': 1, 'b': 2}
        print(d.get('c', 3), d.setdefault('c', 4))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "3 4"

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
