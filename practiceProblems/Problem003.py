

inputTpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Input tuple: ", inputTpl)
inputLst = list(inputTpl)
x = len(inputLst)/2 +1
outputLst1 = inputLst[0:x]
outputTpl1 = tuple(outputLst1)
print("\nOutput tuple 1: ", outputTpl1)
outputLst2 = inputLst[x-1 :]
outputTpl2 = tuple(outputLst2)
print("\nOutput tuple 2: ", outputTpl2)