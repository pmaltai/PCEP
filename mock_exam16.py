def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Advanced Mock Exam 2\n")
    
    def q1():
        """What's the output? (Multiple assignment)
        
        a, b = [1, 2]
        a, b = b, a
        print(a, b)
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "2 1"
    
    def q2():
        """List operations sequence:
        
        lst = [1, 2, 3]
        lst.append(4)
        lst[1:3] = [5, 6]
        print(lst)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 5, 6, 4]"
    
    def q3():
        """String operations:
        
        text = "Python"
        print(text.find('y'), text.count('p'))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "1 0"
    
    def q4():
        """Loop with else:
        
        for i in range(3):
            if i == 3:
                break
            print(i, end='')
        else:
            print('!', end='')
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "012!"
    
    def q5():
        """Dictionary operations:
        
        d = {'a': 1, 'b': 2}
        d.update({'a': 3, 'c': 4})
        print(sorted(d.values()))
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 3, 4]"
    
    def q6():
        """Function with variable arguments:
        
        def sum_all(*args):
            return sum(args)
        print(sum_all(1, 2, 3))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "6"
    
    def q7():
        """String formatting:
        
        x = 42
        print(f"{x:03d} {x:>5}")
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "042   42"
    
    def q8():
        """List comprehension with condition:
        
        print([x for x in range(5) if x % 2 == 0 if x > 0])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 4]"
    
    def q9():
        """Nested data structures:
        
        data = [{'x': 1}, {'x': 2}]
        print([d['x'] for d in data])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2]"
    
    def q10():
        """Function default arguments:
        
        def greet(name, greeting='Hello'):
            return f"{greeting}, {name}!"
        print(greet(greeting='Hi', name='Bob'))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "Hi, Bob!"

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
