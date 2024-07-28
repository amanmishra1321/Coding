arr = [1 , 2 , 3 , 4 , 5 , 5]
# arr = [ 4, 1, 2, 3]
n = len(arr)
left,right = 0,n-1
leftSum,rightSum = 0,0
while(left<=right):
    if(leftSum == rightSum and ((left)+ (n-1-right)) == n):
        break
    if(leftSum > rightSum):
        rightSum += arr[right]
        right -= 1
    elif(rightSum > leftSum):
        leftSum += arr[left]
        left += 1
    else:
        leftSum += arr[left]
        rightSum += arr[right]
        left += 1
        right -= 1
    # print(leftSum,rightSum,left,right)
    
if(leftSum == rightSum and ((left)+ (n-1-right)) == n):
    print("left Index",left, "Right Index",right,"Left Sum",leftSum,"Right Sum",rightSum)
else:
    print("Not possible")
    
    
    
    