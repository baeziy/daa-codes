def foo(L, p, r):
    if (p==r):
        if L[p] % 7 == 0:
            return L[p]
        else:
            return 1

    else:
        mid = (p+r)//2
        left = foo(L, p, mid)
        right = foo(L, mid + 1, r)

    return left * right

print(foo([2,7,3,14,21], 0, 4))