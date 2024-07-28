row = int(input())
for i in range(row*2+1):
    n = 0
    for j in range(row*2+1):
        if(i <= row and ((row - i) <= j) and (j < (row+i))):
            print(n,end=" ")
            if j < row:
                n += 1
            else:
                n -= 1 
        elif((i <= row) and j == (row+i)):
            print(n,end="")
            if j < row:
                n += 1
            else:
                n -= 1
            break
        elif(i <= row):
            print(" ",end=" ")
            
        elif( (i<=row*2) and ((i-row) <= j) and ((row*2+row)-i) > j ):
            print(n,end=" ")
            if j < row:
                n += 1
            else:
                n -= 1
        elif((i<=row*2) and (j == ((row*2+row)-i))):
            print(n,end="")
            if j < row:
                n += 1
            else:
                n -= 1
            break
        else:
            print(" ",end=" ")
    print()