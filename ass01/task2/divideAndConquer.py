def foo(L, p, r):
    if (p==r):
        if (L[p] > len(L)- 100) and (L[p] < len(L) + 100):
            return L[p]

    else:
        mid = (p+r)//2
        left = foo(L, p, mid)
        right = foo(L, mid + 1, r)

    return left + right


print(foo([3,4,5,7], 0, 3))