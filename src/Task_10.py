def kth_factor(n, k):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    if k <= len(factors):
        return factors[k - 1]
    else:
        return -1

n, k = map(int, input().split())

result = kth_factor(n, k)

print(result)

# O(n) where n = number of elements since in the loop the code has to go through each element, in total n times
