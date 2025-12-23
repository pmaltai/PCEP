def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 8\n")
    
    def q1():
        """What's the output? (String methods)
        
        text = "Programming"
        print(text[::2].swapcase())
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "pORMIG"
    
    def q2():
        """Tuple operations:
        
        t1 = (1, 2)
        t2 = tuple([3, 4])
        print(t1 + t2[:-1])
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "(1, 2, 3)"
    
    def q3():
        """List operations:
        
        lst = [1, 2, 3]
        lst.extend([lst.pop()])
        print(lst)
        """
        answer = input("\nQ3: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"
    
    def q4():
        """Dictionary methods:
        
        d = dict(a=1, b=2)
        d.update([('c', 3), ('a', 4)])
        print(d['a'])
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "4"
    
    def q5():
        """Loop with conditional:
        
        x = [1, 2, 3]
        y = [sum(x[:i]) for i in range(1, len(x)+1)]
        print(y)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3, 6]"
    
    def q6():
        """Function with mutable default:
        
        def add_item(item, lst=None):
            if lst is None:
                lst = []
            lst.append(item)
            return lst
        print(add_item(1))
        print(add_item(2))
        """
        answer = input("\nQ6: What will be printed? (write both lines) ").strip()
        return answer == "[1] [2]"
    
    def q7():
        """Set operations:
        
        s = set('hello')
        print(''.join(sorted(s)))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "ehlo"
    
    def q8():
        """String formatting:
        
        x = 123.456
        print("{:.1e}".format(x))
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "1.2e+02"
    
    def q9():
        """List comprehension:
        
        matrix = [[1,2], [3,4]]
        print([j for i in matrix for j in i if j % 2 == 0])
        """
        answer = input("\nQ9: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[2, 4]"
    
    def q10():
        """Multiple assignment:
        
        a, *b, c = range(5)
        print(b)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3]"

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
