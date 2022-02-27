#2. Write a program to generate and print another tuple whose valus are even numbers in the given tuple.
       # input  (1,2,3,4,5,6,7,8,9,10)
       # output (2,4,6,8,10)

inputTpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tempLst = []
print("Input tuple: ", inputTpl)

for i in inputTpl:
    if(i%2 == 0):
        tempLst.append(i)

outputTpl = tuple(tempLst)
print("\nOutput tuple: ", outputTpl)