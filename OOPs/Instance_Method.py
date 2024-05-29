class Student:
    def __init__(self,name):
        self.name = name
        
    def greeting(self):
        print(f"Hello I am {self.name}")
        
    def name_length(self):
        return len(self.name)
        
student1 = Student('John')
student1.greeting()
length = student1.name_length()
print(length)