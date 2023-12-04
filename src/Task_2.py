def max_beautifulness(n, Y):
    sorted_Y = sorted(enumerate(Y, 1), key=lambda x: x[1])

    beautifulness = sum(abs(index - value) for index, value in sorted_Y)

    return beautifulness

n = 5
Y = [1, 4, 2, 3, 5]

result = max_beautifulness(n, Y)

print(result)

#O(n) where n = number of elements
