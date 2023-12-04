from typing import List
import heapq
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequency_map = Counter(nums)

    min_heap = [(-freq, num) for num, freq in frequency_map.items()]
    heapq.heapify(min_heap)

    result = []
    for _ in range(k):
        result.append(heapq.heappop(min_heap)[1])

    return result

n = int(input())
nums = list(map(int, input().split()))
k = int(input())

result = topKFrequent(nums, k)

print(*result)
