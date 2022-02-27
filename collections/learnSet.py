
# Empty curly braces is considered as Dict
seta = {}
print("Empty {} -> type", type(seta))

#Initialise a set
st = {'Selenium', 'UFT', 'Robot', 'RestAssured', 'Excel'}
print("Set values: ", st)
print("1D {} -> type", type(st))

#Add method
# if we wanted to add much more items to list we use append
print("Before Add", st)
st.add('HTTPClient')
print("After Add", st)

#Update method
# if we wanted to add a list/set/tuple
st1 = {'JMeter'}
print("Before update", st)
st.update(st1)
print("After update", st)

#Copy method
#Copy a list to another list
newSt = st.copy()
print("Copied set", newSt)

#Remove method
#Remove given items - doesnot have return value
print("Before remove", st)
st.remove('HTTPClient')
print("After remove", st)

#Discord method
#Remove items from the list
print("Before discard", st)
st.discard('HTTPClient')
st.discard('UFT')
print("After discard", st)

#Pop method - deletes randomly and returns the removed value
# Remove last item in list
print("Before pop", st)
print(st.pop())
print("After pop", st)

#Clear method
#Remove items from the list
print("Before clear", st1)
st1.clear()
print("After clear", st1)

#Sorted method
#Sorted List/Tuple/Set/Dict and not store in existing memory location
print("Before sorted -> names", st)
newNames = sorted(st)
print("After sorted -> names", st)
print("After sorted -> newNames", newNames)

#Len method
# To get count of any collection
print("Length of collection =>", len(newNames))

#Min method
# To get minimum value of any collection
intSet = {5, 15, 25, 88, 1, -5}
print("Minimum of collection =>", min(intSet))

#Max method
# To get maximum value of any collection
print("Maximum of collection =>", max(intSet))

#Sum method
# To get Sum value of any collection
print("Sum of collection =>", sum(intSet))

#In Operator
#To find whether a given value is present in list
print("In operator", ('Gopi' in st))
print("In operator", (1 in st))

#Not in Operator
#To find whether a given value is not present in list
print("Not In operator", ('Gopi' not in intSet))
print("Not In operator", (-5 not in intSet))

#Union
#Intersection
#Difference
#Symmetri_difference
#difference_update
#intersection_update
#symmetri_difference_update
#issubset
#issuperset
#isdisjoint