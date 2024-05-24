class Student:
    
    Category = 'student'
    
    def __init__(self,name):
        self.name = name
        
    def greeting(self):
        print(f"Hello I am {self.name}")
        
    def name_length(self):
        return len(self.name)
    
    @classmethod
    def info(cls):
        print(f"This is a method of the class {cls.Category}")
        
    @staticmethod
    def add(a,b):
        print(a+b)
        
Student.add(2,4)
        
