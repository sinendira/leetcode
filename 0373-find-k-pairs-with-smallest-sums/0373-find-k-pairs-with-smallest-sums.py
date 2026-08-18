from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()

        while len(ans) < k:
            sm, ind1, ind2 = heappop(heap)
            ans.append([nums1[ind1], nums2[ind2]])

            if ind2 + 1 < len(nums2) and (ind1, ind2 + 1) not in visited:
                heappush(heap, (nums1[ind1] + nums2[ind2 + 1], ind1, ind2 + 1))
                visited.add((ind1, ind2 + 1))

            if ind1 + 1 < len(nums1) and (ind1 + 1, ind2) not in visited:
                heappush(heap, (nums1[ind1 + 1] + nums2[ind2], ind1 + 1, ind2))
                visited.add((ind1 + 1, ind2))

            if ind1 + 1 < len(nums1) and ind2 + 1 < len(nums2) and (ind1 + 1, ind2 + 1) not in visited:
                heappush(heap, (nums1[ind1 + 1] + nums2[ind2 + 1], ind1 + 1, ind2 + 1))
                visited.add((ind1 + 1, ind2 + 1))

        return ans