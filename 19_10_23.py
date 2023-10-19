# cond = int(input('do you want to quit it y/n'))
# for i in range(1,11):
#     print(i)
#     if i == cond:
#         break


# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
        
# function
# def add_two_number(num1,num2):

#     print('we are going to add two numbers')
#     return num1 + num2







# sumision = add_two_number(10,10)
# print(sumision)
# print()
# sumision2 = add_two_number(20,10)
# print(sumision2)



# def find_even(lst):
#     even = []
#     for item in lst:
#         if item % 2==0:
#             even.append(item)
#     print(even)

# lst = [5,8,7,4,6,9,8,5,2,3,56,85,47,6,30]
# find_even(lst)


# name = 'jaipur rajsthan'
# d = {}
# for char in name:
#     d[char] = name.count(char)
# print(d)


# def greeting():
#     print('hello jecrc')

def string_count(string_var,fun):
    d = {}
    fun()
    for char in name:
        d[char] = name.count(char)
    print(d)

# name = 'jaipur '
# string_count(name,greeting)



# pwer = lambda x: x**2

# a = pwer(20)
# print(a)

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(6))

