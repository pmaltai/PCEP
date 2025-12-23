def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("PCEP Advanced Mock Exam - Entry Level Python\n")
    
    def q1():
        """What's the output? (List comprehension)
        
        nums = [1, 2, 3, 4, 5]
        result = [x * 2 for x in nums if x % 2 == 0]
        print(result)
        """
        answer = input("\nQ1: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 8]"
    
    def q2():
        """Nested loop output:
        
        for i in range(2):
            for j in range(2):
                if i == j:
                    print(i, end='')
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "01"
    
    def q3():
        """Function with multiple returns:
        
        def check_number(x):
            if x > 0:
                return "Positive"
            elif x < 0:
                return "Negative"
            return "Zero"
            
        print(check_number(0))
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "Zero"
    
    def q4():
        """String formatting:
        
        name = "Alice"
        age = 25
        print(f"{name:>10} is {age:<5} years old")
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "     Alice is 25    years old"
    
    def q5():
        """List slicing with stride:
        
        numbers = [0, 1, 2, 3, 4, 5]
        print(numbers[4:0:-2])
        """
        answer = input("\nQ5: What will be printed? (write exactly as Python would display) ").strip()
        return answer == "[4, 2]"
    
    def q6():
        """Nested dictionary manipulation:
        
        data = {'user': {'name': 'John', 'age': 30}}
        print(data.get('user', {}).get('city', 'Unknown'))
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "Unknown"
    
    def q7():
        """Functi
