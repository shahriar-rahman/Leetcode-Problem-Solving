# Runtime 97ms
# Memory 16.55mb

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        concat = nums1 + nums2

        concat.sort()        
        mid = len(concat) // 2
        median = (concat[mid] + concat[~mid]) / 2

        return median