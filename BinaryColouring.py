def continous1(string):
    newString = ""
    p1,n = 0,len(string)
    while(p1<n):
        if string[p1] == '1':
            newString += " -1"
            while(p1<n and string[p1] == '1'):
                newString += " 0"
                p1 += 1
            newString += " 1"
        else:
            newString += " 0"
            p1+=1
    print(newString)
    
for _ in range(int(input())):
    n = int(input())
    binaryString = bin(n)[2:][::-1]
    print(binaryString,n)
    continous1(binaryString)