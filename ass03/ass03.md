##Q1)
####A)

> The problem of finding the closest value in an unsorted array to a given input number can be solved using a _**divide and conquer**_ approach. The basic idea is to divide the array into smaller subarrays and recursively find the closest value in each subarray.

```python
def foo(array, key):
    if len(array) == 1:
        return array[0]

    middle = len(array) // 2
    leftArray = array[:middle]
    rightArray = array[middle:]

    leftClosest = foo(leftArray, key)
    rightClosest = foo(rightArray, key)

    closest = leftClosest
    if abs(key - rightClosest) < abs(key - leftClosest):
        closest = rightClosest

    return closest
```

####B)
The best strategy to solve this problem is divide and conquer. We can divide the array into smaller subproblems, find the middle element, check if the missing number is in the left or right subarray, and recursively call the function until we find the missing number. This approach has a time complexity of O(log n). If we know the common ratio of the progression we can solve it in O(1) time.

```python
def findMissingNumber(arr, start, end):
    # base case
    if (end - start) == 1:
        return (arr[start] * 2) - arr[end]

    # find middle index
    mid = (start + end) / 2

    # check if the missing number is in the left or right subarray
    if (arr[mid] == arr[start] * (r ** (mid - start))):
        return findMissingNumber(arr, mid, end)
    else:
        return findMissingNumber(arr, start, mid)

```

####C)
To find a key in a 2-D matrix where the data is sorted row-wise and column-wise, the best approach is divide and conquer. We can use a binary search algorithm by dividing the matrix into smaller submatrices and repeatedly find the middle element until the key is found or it is determined that it doesn't exist in the matrix.

```python
def searchKey(matrix, key):
    rows = len(matrix)
    cols = len(matrix[0])
    start_row, end_row, start_col, end_col = 0, rows-1, 0, cols-1
    while start_row <= end_row and start_col <= end_col:
        mid_row = start_row + (end_row - start_row)//2
        mid_col = start_col + (end_col - start_col)//2
        if matrix[mid_row][mid_col] == key:
            return True
        elif matrix[mid_row][mid_col] < key:
            start_row = mid_row + 1
            start_col = mid_col + 1
        else:
            end_row = mid_row - 1
            end_col = mid_col - 1
    return False

```

####D)
To find the value of continuous function F(n) = F (n/2 ^ n/3) + ceil (n/2) for first 100 values, the best approach is dynamic programming. We can create an array to store the values of F(n) for different n and fill it in using the recursive definition of the function.

```python
def findF(n):
    # create an array to store the values of F(n)
    F = [0] * (n + 1)
    for i in range(1, n + 1):
        if (i == 1):
            F[i] = 1
        else:
            F[i] = F[i // 2 ** (i // 3)] + (i + 1) // 2
    return F[n]

```

####E)
To find the first unique (not duplicated) element in a sorted array, the best approach is divide and conquer. We can divide the array into smaller subarrays and repeatedly find the middle element of the subarrays. Comparing the middle element to its neighbours will allow us to determine if it is the first unique element, if not, we can discard one half of the subarray, until the first unique element is found.

```python
def findFirstUnique(arr, left, right):
    # base case
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    if (arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]):
        return arr[mid]
    elif (arr[mid] == arr[mid-1]):
        if ((mid - left) % 2 == 0):
            return findFirstUnique(arr, mid+1, right)
        else:
            return findFirstUnique(arr, left, mid-1)
    else:
        return findFirstUnique(arr, left, mid) or findFirstUnique(arr, mid+1, right)

```

---

##Q2)

Dynamic programming can be used to solve the Ackerman's function problem, by creating a 2D table and filling it with the function values for different m and n, based on the recursive definition of the function and smaller subproblems values. However, this approach is not efficient as the function is complex and not primitive recursive, its value grows quickly and the size of the table will be too large to fit in memory, also the time complexity of the algorithm will be high.

```python
def ackerman(m, n):
    table = create_table(m, n)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                table[i][j] = j+1
            elif j == 0:
                table[i][j] = ackerman(i-1, 1)
            else:
                table[i][j] = ackerman(i-1, ackerman(i, j-1))
    return table[m][n]
```

---

##Q3)

```
   |   | S | T | A | R |
---|---|---|---|---|---|
   | 0 | 1 | 2 | 3 | 4 |
---|---|---|---|---|---|
 T | 1 | 1 | 2 | 3 | 4 |
---|---|---|---|---|---|
 R | 2 | 2 | 3 | 4 | 5 |
---|---|---|---|---|---|
 E | 3 | 3 | 4 | 5 | 6 |
---|---|---|---|---|---|
 K | 4 | 4 | 5 | 6 | 7 |
```

• E(1,1) = min(E(0,1) + 2, E(1, 0) + 1, E(0, 0) + cost) = min(2, 1, 1) = 1
• E(2,1) = min(E(1,1) + 2, E(2, 0) + 1, E(1, 0) + cost) = min(3, 2, 2) = 2
• E(3,1) = min(E(2,1) + 2, E(3, 0) + 1, E(2, 0) + cost) = min(4, 3, 3) = 3
• E(4,1) = min(E(3,1) + 2, E(4, 0) + 1, E(3, 0) + cost) = min(5, 4, 4) = 4
• E(1,2) = min(E(0,2) + 2, E(1, 1) + 1, E(0, 1) + cost) = min(3, 2, 2) = 2
• E(2,2) = min(E(1,2) + 2, E(2, 1) + 1, E(1, 1) + cost) = min(4, 3, 1) = 3
• E(3,2) = min(E(2,2) + 2, E(3, 1) + 1, E(2, 1) + cost) = min(5, 4, 2) = 4
• E(4,2) = min(E(3,2) + 2, E(4, 1) + 1, E(3, 1) + cost) = min(6, 5, 3) = 5
• E(1,3) = min(E(0,3) + 2, E(1, 2) + 1, E(0, 2) + cost) = min(4, 3, 3) = 3
• E(2,3) = min(E(1,3) + 2, E(2, 2) + 1, E(1, 2) + cost) = min(5, 4, 2) = 4
• E(3,3) = min(E(2,3) + 2, E(3, 2) + 1, E(2, 2) + cost) = min(6, 5, 1) = 5
• E(4,3) = min(E(3,3) + 2, E(4, 2) + 1, E(3, 2) + cost) = min(7, 6,5) = 6

###B)
The optimal path to minimize the transformation cost between the two strings "STAR" and "TREK" is to perform the following sequence of operations:

- Replace the first character 'S' with 'T', which costs 1
- Replace the second character 'T' with 'R', which costs 1
- Replace the third character 'A' with 'E', which costs 1
- Replace the fourth character 'R' with 'K', which costs 2
- Total cost = 1 + 1 + 1 + 2 = 5

---

##Q4
To find the frequency of a specific key value in a matrix where the number of rows is equal to the number of columns and is in some power of 4, two approaches can be used: divide and conquer, and dynamic programming.

**Divide and Conquer**: This approach divides the matrix into smaller sub-matrices and searches for the key value in each sub-matrix. This process is repeated recursively until the key value is found. The time complexity of this approach is O(n log n), as the matrix is divided into smaller sub-matrices and the key value is searched in each sub-matrix.

**Dynamic Programming**: This approach creates a 2D table where each cell represents the frequency of the key value in the sub-matrix defined by the cell's coordinates. The table is then filled in by using the frequency of the key value in the sub-matrices defined by the cell's coordinates. The time complexity of this approach is O(n^2) as we are iterating through each cell of the matrix.

In this case, the **divide and conquer** approach is more efficient as it has a better time complexity of O(n log n) when compared to the dynamic programming approach which has a time complexity of O(n^2).
