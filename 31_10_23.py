class Student:
    #class variable
    name = 'Rajesh'
    roll = 1
    #constructor
    def __init__(self,college,city):
        #instance variable
        self.college = college
        self.city = city
        print('Hello Student')
    
    #instance method
    def show_info(self):
        print(self.name)
        print(self.college)
        #class method
    @classmethod
    def show_class_prop(cls):
        print(cls.name)
        print(cls.roll)

    @staticmethod
    def Demo_stat():
        print('hello static method')

obj = Student('jecrc','city')
# obj.Demo_stat()
# Student.Demo_stat()
# Student.show_info()
# obj.show_info()


