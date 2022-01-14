#Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

#Isolate the item in some_list
#Check to see if the item matches any other items in some_list
#If there is a duplicate pop into a new_list and move to next items
#Print out the new_list

#Creates new list for duplicates
duplicates = []

#function checks list for duplicates
for value in some_list:

#this part of the function checks to see if the count of values is greater than 1
    if some_list.count(value) > 1:

#If count is greater then one it checks to see if it exist in dupllicates if it doesnt it adds it to duplicates list.
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
