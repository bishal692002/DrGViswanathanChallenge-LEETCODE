import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :type k: int
        # :rtype: List[List[int]]

        output = []

        choiceheap = []
        heapq.heappush(choiceheap, (nums1[0] + nums2[0], (0, 0)))

        visited = set()
        visited.add((0, 0))
        while len(output) != k:
            smallest = heapq.heappop(choiceheap)[1]
            output.append([nums1[smallest[0]], nums2[smallest[1]]])

            if smallest[0] + 1 < len(nums1):
                neighbor1 = (smallest[0] + 1, smallest[1])
                if neighbor1 not in visited:
                    visited.add(neighbor1)
                    heapq.heappush(choiceheap, (nums1[neighbor1[0]] + nums2[neighbor1[1]], neighbor1))

            if smallest[1] + 1 < len(nums2):
                neighbor2 = (smallest[0], smallest[1] + 1)
                if neighbor2 not in visited:
                    visited.add(neighbor2)
                    heapq.heappush(choiceheap, (nums1[neighbor2[0]] + nums2[neighbor2[1]], neighbor2))

        return output

