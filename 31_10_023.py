# # inheritence
# # 1. SINGLE inheritence
# # 2.MULTIPLE 
# # 3.MULTI LEVEL
# # 4.HIERARCHICAL
# # 5.HYBRID  


# # single inheritence
# class Parent:
#     name = 'mohan singh'
#     age = 45
#     income = '25 LPA'
#     def __init__(self,father_name,mother_name):
#         self.father_name = father_name
#         self.mother_name = mother_name

#     def work(self):
#         print(self.father_name)
#         print(self.mother_name)



# class Child(Parent):
#     name = 'Pappu'
#     age = 18

#     def __init__(self,child_name,child_job,father_name,mother_name):
#         self.child_name = child_name
#         self.child_job = child_job
#         super().__init__(father_name= father_name,mother_name=mother_name)

#     def child_info(self):
#         print(self.child_name)
#         print(self.child_job)



# child_obj = Child('Papu','lofer','mohan singh','mamta devi')
# # child_obj.child_info()
# # print(child_obj.income)

# child_obj.work()
# print()
# child_obj.child_info()

# multiple inheritence

class Parent:
    name = 'mohan singh'
    age = 45
    income = '25 LPA'
    def __init__(self,father_name,mother_name):
        self.father_name = father_name
        self.mother_name = mother_name

    def work(self):
        print(self.father_name)
        print(self.mother_name)
class Parent2:
    name = 'jagat singh'
    age = 36
    income = '15 LPA'
    def __init__(self,parent_name2,parent_job2):
        self.parent_name2 = parent_name2
        self.parent_job2 = parent_job2

    def work2(self):
        print(self.parent_job2)
        print(self.parent_name2)


class Child(Parent,Parent2):
    name = 'Pappu'
    age = 18

    def __init__(self,child_name,child_job,father_name,mother_name,parent_name2,parent_job2):
        self.child_name = child_name
        self.child_job = child_job
        Parent.__init__(self,father_name= father_name,mother_name=mother_name)
        Parent2.__init__(self,parent_name2=parent_name2,parent_job2=parent_job2)


    def child_info(self):
        print(self.child_name)
        print(self.child_job)


# child_obj = Child('papu','lofer','jagat singh','mamta devi','rakesh','Data entry operator')
# child_obj.work()
# print()
# child_obj.work2()
# print()
# child_obj.child_info()

