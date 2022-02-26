# Create List
names = ['Praveen', 'Srikanth', 'Aswin', 'Vel', 'Ela']
print("Type of names", type(names))

#Fetch an item from list
print("Fetched item", names[2])

#Append method
# if we wanted to add much more items to list we use append
print("Before Append", names)
names.append('Gopi')
print("After Append", names)

#Extend method
#Add another list at end we use extend method
print("Before Extend", names)
names.extend(['Muralee', 'Chitti'])
print("After Extend", names)

#Insert method
#Insert item at a desired position
print("Before Insert", names)
names.insert(0, 'Babu')
print("After Insert", names)

# '+' Operator
#Add another list at end we use extend method
print("Before +", names)
names = names + ['Anil', 'Aamai', 'Muralee']
print("After +", names)

#Index method
#To find first matching index of an item
print("Index ", names.index('Muralee'))

#Copy method
#Copy a list to another list
newNames = names.copy()
print("Copied list", newNames)

#Count method
#Count method returns count of given item
print("Count of Muralee", names.count('Muralee'))

#Remove method
#Remove given items - doesnot have return value
print("Before remove", names)
names.remove('Chitti')
print("After remove", names)

#Pop method - returns the removed value
# Remove last item in list
print("Before pop", names)
names.pop()
print("After pop", names)
#Remove desired item on specified index
print("Before pop index", names)
names.pop(4)
print("After pop index", names)


#Clear method
#Remove items from the list
print("Before clear", names)
#names.clear()
print("After clear", names)

#Sort method
#Sort list based on ascending order and stored in same variable
print("Before sort", names)
names.sort()
print("After sort", names)

#Reverse method
# Reverse list and stored in same variable
print("Before Reverse", names)
names.reverse()
print("After Reverse", names)

#Reversed method
#Reverse List/Tuple/Set/Dict and not store in existing memory location
print("Before Reversed", names)
newNames = names.__reversed__()
print("After Reversed Old", names)
print("After Reversed New", list(newNames))

#Sorted method
#Sorted List/Tuple/Set/Dict and not store in existing memory location
print("Before sorted -> names", names)
newNames = sorted(names)
print("After sorted -> names", names)
print("After sorted -> newNames", newNames)