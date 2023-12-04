def find_kth_missing(arr, n, k):
    missing_count = 0
    current_number = 1

    for num in arr:
        while current_number < num:
            missing_count += 1
            if missing_count == k:
                return current_number
            current_number += 1

        current_number += 1

    while missing_count < k:
        missing_count += 1
        current_number += 1

    return current_number - 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = find_kth_missing(arr, n, k)

print(result)

#O(n+k), where n = length of the given array arr and k = given integer k
