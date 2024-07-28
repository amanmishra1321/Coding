matrix= []
for i in range(5):
    temp = list(map(int,input().split()))
    matrix.append(temp)
operation = 0
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 1:
            operation = abs(2-row)+abs(2-col)
            break
print(operation)
