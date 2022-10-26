def foo(L, p, r):
    if (p==r):
            return L[p]
    if(r+1== p):
            return 1 
    
    
    else:
        mid = (p+r)//2
        leftmid = (p +mid)//2
        rightmid = (mid+ r)//2

        first = foo(L, p, leftmid)
        second = foo(L, leftmid+1, mid)
        third = foo(L, mid + 1, rightmid)
        fourth = foo(L, rightmid+1, r)

    return first * second * third * fourth


print(foo([3,4,5,7,7,5,3,2,9,1], 0, 9))