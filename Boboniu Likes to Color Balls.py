for _ in range(int(input())):
    r,g,b,w = map(int,input().split())
    twice = 2
    flag = False
    while(twice):
        if ((r%2 == 1 and g%2 == 0 and b%2 ==0  and w%2 == 0) 
        or (r%2 == 0 and g%2 == 1 and b%2 ==0  and w%2 == 0) or 
        (r%2 == 0 and g%2 == 0 and b%2 ==1  and w%2 == 0) or 
        (r%2 == 0 and g%2 == 0 and b%2 ==0  and w%2 == 1) or
        (r%2 == 0 and g%2 == 0 and b%2 ==0  and w%2 == 0)
        ):
            print("YES")
            flag = True
            break
        elif(r != 0 and g != 0 and b != 0):
            r -= 1
            g -= 1
            b -= 1
            w += 3
        twice -= 1
    if not flag:
        print("NO")