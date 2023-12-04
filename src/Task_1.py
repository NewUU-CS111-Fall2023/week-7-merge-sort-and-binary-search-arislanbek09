def remaining_sum_after_operations(T, testCases):
    results = []

    for t in range(T):
        N = testCases[t][0]
        A = testCases[t][1]

        medians = []
        for i in range(1, N - 1, 2):
            subarray = A[i - 1:i + 2]
            subarray.sort()
            medians.append(subarray[1])

        min_median = min(medians)
        A.remove(min_median)

        remaining_sum = sum(A)
        results.append(remaining_sum)

    return results


T = 2
testCases = [
    (4, [2, 5, 3, 2]),
    (4, [1, 1, 1, 1])
]

output = remaining_sum_after_operations(T, testCases)

for result in output:
    print(result)

#
