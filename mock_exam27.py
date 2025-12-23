def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 13\n")
    
    def q1():
        """What's printed?
        
        lst = [1, 2, 3] * 2
        lst[0] = 4
        print(lst)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 2, 3, 1, 2, 3]"
    
    def q2():
        """Output of:
        
        data = dict(zip('abc', range(3)))
        print(data.get('d', -1))
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "-1"
    
    def q3():
        """Result?
        
        def modify(x=[]):
            x.append(1)
            return x
        print(modify())
        print(modify([2]))
        """
        answer = input("\nQ3: What will be printed? (write both lines) ").strip()
        return answer == "[1] [2, 1]"
    
    def q4():
        """What's displayed?
        
        text = "Python"
        print(text.find('n'), text.index('n'))
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "5 5"
    
    def q5():
        """List slicing:
        
        nums = range(1, 6)
        print(list(nums)[::2])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 3, 5]"
    
    def q6():
        """Set operations:
        
        x = {1, 2, 3}
        y = {3, 4, 5}
        print(sorted(x | y))
        """
        answer = input("\nQ6: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 5]"
    
    def q7():
        """Dictionary methods:
        
        d = {'a': 1, 'b': 2}
        d.update([('a', 3), ('c', 4)])
        print(sum(d.values()))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "9"
    
    def q8():
        """String formatting:
        
        name = "Python"
        print(f"|{name:^8}|")
        """
        answer = input("\nQ8: What will be printed? ").strip()
        return answer == "| Python |"
    
    def q9():
        """List operations:
        
        a = [[1], [2]]
        b = a[:]
        a[0][0] = 3
        print(b[0][0])
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "3"
    
    def q10():
        """Function args:
        
        def func(*args, **kwargs):
            return len(args) + len(kwargs)
        print(func(1, 2, a=3, b=4))
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "4"

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
