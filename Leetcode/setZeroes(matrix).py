def setZeroes(matrix):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if( matrix[i][j] == 0):
                    tempi,tempj = i,j
                    #for downward section
                    while(tempi<n):
                        matrix[tempi][j] = -1
                        tempi+=1
                    tempi = i
                    print(matrix)
                    #for rightward section
                    while(tempj<m):
                        matrix[i][tempj] = -1
                        tempj+=1
                    tempj = j
                    print(matrix)
                    #for upward section
                    while(tempi>=0):
                        matrix[tempi][j] = -1
                        tempi-=1
                    print(matrix)
                    #for leftward section
                    while(tempj>=0):
                        matrix[i][tempj] = -1
                        tempj -= 1
                    print(matrix)
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == -1):
                    matrix[i][j] = 0
        return matrix

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(setZeroes(matrix))