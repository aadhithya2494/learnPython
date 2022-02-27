
#Create Tuple

names = ('Manager', 'Dev', 'Test', 'Devops', 'Support', 'SDET', 'SDET')
print("Tuple values", names)
print("Tuple type", type(names))
# Even for a single item tuple, we need to add ","
singleTuple = ('AB')
print("Values", singleTuple)
print("Type", type(singleTuple))
singleTuple = ('AB',)
print("Values", singleTuple)
print("Type", type(singleTuple))
#Without "()" paranthesis, by default python considers as Tuple
withoutBraces = 'abc', 'cde', 'fgh'
print("Values", withoutBraces)
print("Type", type(withoutBraces))

#Since Tuple is immutable, there is no append, extend, insert, remove, pop, clear, reverse, sort functions

#Index method
#To find first matching index of an item
print("Index of SDET ", names.index('SDET'))

#Count method
#Count method returns count of given item
print("Count of SDET", names.count('SDET'))

#Reversed method
#Reverse List/Tuple/Set/Dict and not store in existing memory location
print("Before Reversed", names)
reversed = reversed(names)
print("After Reversed Old", names)
print("After Reversed New", tuple(reversed))

#Sorted method
#Sorted List/Tuple/Set/Dict and not store in existing memory location
print("Before sorted -> names", names)
newNames = sorted(names)
print("After sorted -> names", names)
print("After sorted -> newNames", newNames)


#Len method
# To get count of any collection
print("Length of collection =>", len(newNames))

#Min method
# To get minimum value of any collection
intTuple = (5, 15, 25, 88, 1, -5)
print("Minimum of collection =>", min(intTuple))

#Max method
# To get maximum value of any collection
print("Maximum of collection =>", max(intTuple))

#Sum method
# To get Sum value of any collection
print("Sum of collection =>", sum(intTuple))

#In Operator
#To find whether a given value is present in list
print("In operator", ('Gopi' in  names))
print("In operator", (1 in  names))

#Not in Operator
#To find whether a given value is not present in list
print("Not In operator", ('Gopi' not in intTuple))
print("Not In operator", (-5 not in intTuple))

#Del method
#To delete the entire collection from list
#del(intTuple)
#print("After deleting list =>", intList)