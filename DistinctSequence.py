
def recursion(n,s,t,string):
    if n < 0:
        print(string)
        return int(t == string)
    string1 = recursion(n-1,s,t,string)
    string2 = recursion(n-1,s,t,s[n]+string) 
    if string == t:
        string2+=1
    return (string1+string2)

def numDistinct(s,t):
    return recursion(len(s)-1,s,t,'')
print(numDistinct("rabbbit","rabbit"))