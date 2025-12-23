def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Mock Exam 5\n")
    
    def q1():
        """Result of string operations:
        
        s = 'python'
        print(s.title()[::2])
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "Pto"
    
    def q2():
        """List operations:
        
        a = [1, 2, 3]
        b = [4, 5]
        print(a + b * 2)
        """
        answer = input("\nQ2: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[1, 2, 3, 4, 5, 4, 5]"
    
    def q3():
        """Function output:
        
        def modify(x, y=[]):
            y.append(x)
            return y
        print(modify(1))
        print(modify(2))
        """
        answer = input("\nQ3: What will be printed? (write both lines) ").strip()
        return answer == "[1] [1, 2]"
    
    def q4():
        """Dictionary comprehension:
        
        x = [1, 2, 3]
        d = {n: n**2 for n in x}
        print(d[2])
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "4"
    
    def q5():
        """Set operations:
        
        a = {1, 2, 3}
        b = {3, 4, 5}
        print(a - b)
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "{1, 2}"
    
    def q6():
        """Nested loop with break:
        
        for i in range(3):
            for j in range(3):
                if i == j:
                    break
                print(j, end='')
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "012"
    
    def q7():
        """String format:
        
        name = "Bob"
        age = 25
        print("Name: {1}, Age: {0}".format(age, name))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "Name: Bob, Age: 25"
    
    def q8():
        """List slicing:
        
        nums = [1, 2, 3, 4, 5]
        print(nums[-2:1:-1])
        """
        answer = input("\nQ8: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 3]"
    
    def q9():
        """Function with multiple returns:
        
        def compare(a, b):
            if a > b: return 1
            if a < b: return -1
            return 0
        print(compare(1, 1))
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "0"
    
    def q10():
        """List methods:
        
        list1 = [1, 2, 3]
        list2 = list1
        list1[:] = [4, 5, 6]
        print(list2)
        """
        answer = input("\nQ10: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 5, 6]"

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
