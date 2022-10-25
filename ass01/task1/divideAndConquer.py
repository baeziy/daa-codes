def foo(L, p, r):
    if (p == r):
        if(p%2!=0):
            if L[p] == 1:
                L[p] = 0
            else:
                L[p] = 1
        return L
    else:    
        mid = (p+r)//2
        left = foo(L, p, mid)
        right = foo(L, mid + 1, r)
    return L




print(foo([0,1,1,0,0,1,0,0,1], 0, 8))