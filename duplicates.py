#Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#Isolate the item in some_list
#Check to see if the item matches any other items in some_list
#If there is a duplicate pop into a new_list and move to next items
#Print out the new_list

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)



# new_list = []
# i = 0
# item = some_list[i]
# while i < len(some_list):
#     if item == i:
#         new_list.append(item)
#     i+= 1
#
# print(new_list)
