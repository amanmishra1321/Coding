# 3 4 5 10 8 100 3 1
n,k,l,c,d,p,nl,np = map(int,input().split())
totalSlice = c*d
totalMilli = k*l
saltReq = p//np
eachFriendLitre = totalMilli//nl
print(min(eachFriendLitre,totalSlice,saltReq)//n)


# 1 7 4 5 5 8 3 2
# totalMilli = 7*4 = 28
# totalSlice = 
