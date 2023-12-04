def recursivePow(x, n):
    if n == 0:
        return 1
    else:
        return x * recursivePow(x, n - 1)

result = recursivePow(12, 2)

print(result)
#O(n) where n = number of items in the array
