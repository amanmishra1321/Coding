x = input()
newNum = ""
for index in range(len(x)):
    if int(x[index]) < 5 or index == 0 and x[index] == '9':
        newNum += x[index]
    else:
        newNum += str(9- int(x[index]))
print(newNum)