#1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and tuple which contains every number.
# input: 25,87,54,10,20
# output: List -['25', '87', '54', '10', 20]
#          Tuple -('25', '87', '54', '10', 20)

inputStr = input("Enter csv string : ")
lst = []

for i in inputStr.split(','):
    lst.append(i)

tpl = tuple(lst)

print ("List :", lst)
print ("\n Tuple :", tpl)