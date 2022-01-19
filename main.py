# is_magician = True
# is_expert = False
#
# # check if a magician AND expert: "you are a master magician"
#
# if is_expert and is_magician:
#     print("you are a master magician")
#
# # check if magician but not expert "at least you're getting there"
#
# elif is_magician and not is_expert:
#     print("at least you're getting there")
#
# # check if you're not a magician: "You need magic powers"
#
# if not is_magician:
#     print("You need magic powers")

# #For Loops
# for item in (1,2,3,4,5):
#     for x in ['a', 'b', 'c']:
#         print(item, x)

#Looping over a dictionary

# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swim': False
# }
#
# for key, value in user.items():
#     print(key,value)
#
# #for item in user.items():
# #    print(item)
#
# for item in user.values():
#     print(item)
#
# for item in user.keys():
#     print(item)


# Simple Counter

# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# counter = 0
# for x in my_list:
#     counter = counter + x
#
# print(counter)

# #enumerate()
# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'index of 50 is: {i}')

#while Loops
# i = 1
# while i < 40:
#     print(i)
#     i += 1
# else:
#     print('done with all the work')
#
# my_list = [1,2,3]
# for item in my_list:
#     print(item)
#
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1


#WHile loops are really good for task where you dont know how long you might need it to work.
# while True:
#     response = input('say something: ')
#     if (response == 'bye'):
#         break

#Functions

# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1 + n2
#     return another_func(num1, num2)
#
# total = sum(10, 20)
# print(total)

# *args **kwargs
#
# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
#
# print(super_func(1,2,3,4,5, num1=5, num2=10))

#walrus operator

# a = 'helloooooooooooooo'
#
# if (len(a) > 10):
#     print(f"too long {len(a)} elements")
#
# #same problem with walrus operator
#
# if ((n:= len(a)) > 10):
#     print(f"too long {n} elements")
#
# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
#
# print(a)

#OOP
# clss BigObject: #Class
#     #code
#     pass
# obj1 = BigObject() #instanciate
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))

class PlayerCharacter:
    def __init__(self, name, age):  #__init__ constructor Method
        self.name = name
        self.age = age

    def run(self):
        print('run')

player1 = PlayerCharacter('Dennis', 32)
player2 = PlayerCharacter('Christina', 29)

print(player1.name)
print(player2.age)
