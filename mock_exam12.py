def run_mock_exam():
    score = 0
    total_questions = 10
    
    print("Advanced Python Mock Exam\n")
    
    def q1():
        """What's the output? Consider metaclass behavior:
        
        class Meta(type):
            def __new__(cls, name, bases, dict):
                dict['x'] = 42
                return super().__new__(cls, name, bases, dict)
                
        class A(metaclass=Meta):
            pass
            
        print(A.x)
        """
        answer = input("\nQ1: What will be printed? ").strip()
        return answer == "42"
    
    def q2():
        """Result of decorator chain:
        
        def d1(f): return lambda: f() + 1
        def d2(f): return lambda: f() * 2
        
        @d1
        @d2
        def func(): return 5
        
        print(func())
        """
        answer = input("\nQ2: What will be printed? ").strip()
        return answer == "11"
    
    def q3():
        """Output of context manager:
        
        class Context:
            def __enter__(self): return self
            def __exit__(self, *args): print('exit')
            
        with Context() as c:
            print('in', end=' ')
        """
        answer = input("\nQ3: What will be printed? ").strip()
        return answer == "in exit"
    
    def q4():
        """What prints? Understand descriptors:
        
        class Desc:
            def __get__(self, obj, type=None):
                return 'get'
            def __set__(self, obj, val):
                print('set', val)
                
        class C:
            d = Desc()
            
        c = C()
        c.d = 1
        print(c.d)
        """
        answer = input("\nQ4: What will be printed? ").strip()
        return answer == "set 1\nget"
    
    def q5():
        """Generator behavior:
        
        def gen():
            try:
                yield 1
            finally:
                print('fin', end=' ')
                
        g = gen()
        next(g)
        try:
            g.throw(ValueError)
        except ValueError:
            print('caught', end=' ')
        """
        answer = input("\nQ5: What will be printed? ").strip()
        return answer == "fin caught"
    
    def q6():
        """MRO resolution:
        
        class A: x = 1
        class B(A): pass
        class C(A): x = 2
        class D(B, C): pass
        
        print(D.x)
        """
        answer = input("\nQ6: What will be printed? ").strip()
        return answer == "2"
    
    def q7():
        """Coroutine behavior:
        
        async def coro():
            return 'result'
            
        from types import coroutine
        @coroutine
        def run(coro):
            return coro.send(None)
            
        print(run(coro()))
        """
        answer = input("\nQ7: What will be printed? ").strip()
        return answer == "StopIteration: result"
    
    def q8():
        """Slots and descriptors:
        
        class Slotted:
            __slots__ = ['x']
            def __init__(self):
                self.x = 1
                
        s = Slotted()
        s.y = 2
        print(s.x)
        """
        answer = input("\nQ8: What will happen? ").strip()
        return answer == "AttributeError: 'Slotted' object has no attribute 'y'"
    
    def q9():
        """Metaclass inheritance:
        
        class MetaA(type):
            def __new__(cls, name, bases, dict):
                dict['a'] = 1
                return super().__new__(cls, name, bases, dict)
                
        class MetaB(type):
            def __new__(cls, name, bases, dict):
                dict['b'] = 2
                return super().__new__(cls, name, bases, dict)
                
        class A(metaclass=MetaA): pass
        class B(metaclass=MetaB): pass
        
        try:
            class C(A, B): pass
            print("Success")
        except TypeError:
            print("Error")
        """
        answer = input("\nQ9: What will be printed? ").strip()
        return answer == "Error"
    
    def q10():
        """Descriptor priority:
        
        class Desc:
            def __get__(self, obj, type=None): return 'desc'
            
        class Prop:
            @property
            def x(self): return 'prop'
            x = Desc()
            
        print(Prop().x)
        """
        answer = input("\nQ10: What will be printed? ").strip()
        return answer == "desc"

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
