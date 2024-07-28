def getAsciiSum(string):
    ascii = 0
    for i in string:
        ascii += ord(i)
    return ascii

def recursion(ind1,ind2,string1,string2):
    if(ind1 < 0):
        return getAsciiSum(string2[0:ind2+1])
    if(ind2 < 0):
        return getAsciiSum(string1[0:ind1+1])

    if(string1[ind1] == string2[ind2]):
        return recursion(ind1-1,ind2-1,string1,string2) 
    else:
        ans1 = recursion(ind1-1,ind2,string1,string2) + ord(string1[ind1])
        ans2 = recursion(ind1,ind2-1,string1,string2) + ord(string2[ind2])
        return min(ans1,ans2)

string1 = "delete"
string2 = "leet"
ind1 = len(string1)
ind2 = len(string2)
# ans = 0
# for i in string1:
#     ans += ord(i)
# for i in string2:
#     ans += ord(i)
k = recursion(ind1-1,ind2-1,string1,string2)
# print(ans - k)
print(k)