## CONDITIONS ##
# Available conditions: If
#Indendations
#In python after conditions, there will be a space which are called indentations which tells the life cycle of if condition
print ("\n Condition :")
if(True):
    print('true')
else:
    print ('false')

print ("\n Odd/Even :")
i = 5
if(i == 0):
    print("Zero number")
elif (i%2 == 0):
    print("Even number")
else:
    print ("Odd number")

#Greater of two numbers
#In python input() is used to get the value
#a = int(input("Enter value of a:"))
#b = int(input("Enter value of b:"))
a, b = 1, 2
#By default input value is string
#Type casting is done by int(variable name)
print ("\n Greatest of two : ")
if(a == b):
    print("Equal")
elif (a > b):
    print("a is greater")
else:
    print ("b is greater")

## LOOPING ##
#Available loops for, while

#for variablename in collection:
    # <body of for loop>
    # <body of for loop>
# exit loop body and continue

#Collection can be
#List
#Tuple
#Set
#Dict
#String

#Range -> normal for iterator till any range

roles = ['SDET', 'Automation tester', 'Manual tester', 'Developer', 'Devops', 'Support']
print("\nList values : ")
for i in roles:
    print(i)

print("\nTuple values : ")
for j in (100, 200, 300, 400):
    print(j)

print("\nString values : ")
for k in 'Star':
    print(k)

print("\nUsing range : ")
for iter in range(5):
    print(iter)

print("\nUsing range within boundaries 10 15 : ")
for iter1 in range(10, 15):
    print(iter1)

print("\nUsing range within boundaries 11 20 and step 2: ")
for iter2 in range(11, 20, 2):
    print(iter2)
