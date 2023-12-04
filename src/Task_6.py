def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return 1, mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, left

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

found, index = search_insert(nums, target)

print(found, index)
