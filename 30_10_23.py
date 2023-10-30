# class Student:
#     name = 'Rajesh'
#     roll = 1
#     age = 21
#     branch = 'CSE'

# class Teacher:
#     name = 'MOhit'
#     roll = 1
#     age =45
#     branch = 'CSE'

# obj = Student()
# teacher_obj = Teacher()
# print(obj.name)
# print(teacher_obj.name)





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




    # Nested class
    class Teacher:
        hello = 'hello'
        def __init__(self):
            print('hello Teacher')



# obj1 = Student('IET AGRA','AGRA ')
# obj2 = Student('JECRC','jaipur')

# print(obj1.college)
# print(obj1.city)
# obj1.show_info()
# print()
# obj2.show_info()

student_obj = Student('jecrc','jaipur')

# teacher_obj = student_obj.Teacher()

# student_obj.show_class_prop()

# Student.show_class_prop()
Student.show_info()
# 


        