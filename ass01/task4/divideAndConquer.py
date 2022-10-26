def foo(L, p, r):
    if (p==r):
        if L[p] == 9:
            return 1
        else:
            return 0

    else:
        mid = (p+r)//2
        left = foo(L, p, mid)
        right = foo(L, mid + 1, r)

    return left + right

print(foo([8, 8, 8, 9, 9, 10 , 10, 10, 10], 0, 8))