def subArraywithSizek(arr,k,s):
    submission = sum(arr[0:(k+1)])
    index = k
    start = 0
    n = len(arr)
    while(index<n):
        while(submission != s):
            submission = submission -arr[start]+arr[index]
            start += 1
            index += 1
        if(submission == s):
            return True
    return False
    
    
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4 
sum = 18
print(subArraywithSizek(arr,k,sum))