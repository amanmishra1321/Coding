def MakeZeros(matrix):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    noOfRow = len(matrix)
    noOfCol = len(matrix[0])
    for row in range(noOfRow):
        for col in range(noOfCol):
            if(matrix[row][col] == 0 ):
                sums = 0
                for direct in directions:
                    if(((direct[0]+row)>= 0 and (direct[0]+row) < noOfRow) and 
                    ((direct[1]+col)>=0 and (direct[1]+col) < noOfCol)):
                        sums += abs(matrix[(direct[0]+row)][(direct[1]+col)])
                        if(matrix[(direct[0]+row)][(direct[1]+col)] > 0):
                            matrix[(direct[0]+row)][(direct[1]+col)] = - matrix[(direct[0]+row)][(direct[1]+col)]
                        print(matrix)
                matrix[row][col] = sums
    for row in range(noOfRow):
        for col in range(noOfCol):
            if(matrix[row][col] < 0):
                matrix[row][col] = 0
    return matrix
# 4 6
# 0 16 0 9 6 18
# 4 4 7 8 8 0
# 11 4 17 12 0 18
# 6 14 12 12 4 3
matrix = [
[0 ,16 ,0 ,9 ,6, 18],
[ 4, 4, 7 ,8 ,8 ,0],
[11 ,4 ,17 ,12 ,0 ,18],
[6 ,14 ,12 ,12 ,4 ,3]
]
print(MakeZeros(matrix))