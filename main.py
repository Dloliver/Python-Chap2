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

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for x in my_list:
    counter = counter + x

print(counter)
