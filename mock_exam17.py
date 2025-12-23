def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Advanced Mock Exam 3\n")
    
    def q1():
        """What's the output? (String methods)
        
        text = "Python"
        print(text.center(8, '*'))
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "*Python*"
    
    def q2():
        """Loop control:
        
        x = 0
        while x < 5:
            x += 1
            if x == 3:
                continue
            if x == 4:
                break
            print(x, end='')
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "12"
    
    def q3():
        """List operations:
        
        a = [1, 2]
        b = a
        a += [3, 4]
        print(b)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4]"
    
    def q4():
        """Function scope:
        
        x = 1
        def change():
            x = 2
            return x
        change()
        print(x)
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "1"
    
    def q5():
        """List comprehension:
        
        words = ['hi', 'hello', 'bye']
        print([len(w) for w in words if 'h' in w])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 5]"
    
    def q6():
        """Dictionary methods:
        
        d = {'a': 1, 'b': 2}
        print(d.pop('a'), d)
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "1 {'b': 2}"
    
    def q7():
        """String formatting:
        
        num = 42.1234
        print(f"{num:.2f}")
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "42.12"
    
    def q8():
        """Nested loops:
        
        for i in range(2):
            for j in range(2):
                if i + j == 2:
                    break
                print(i+j, end='')
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "011"
    
    def q9():
        """Function arguments:
        
        def func(a, b=2, *args):
            return a + b + sum(args)
        print(func(1, 3, 4, 5))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "13"
    
    def q10():
        """String slicing:
        
        word = "Programming"
        print(word[::2].lower())
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "pormig"

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
