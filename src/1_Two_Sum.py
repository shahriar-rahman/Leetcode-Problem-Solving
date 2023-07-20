#  Hashing
# Runtime: 84ms
# Memory: 17.72mb

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)

        # Construct the hash table
        for i in range(n):
            hash_map[nums[i]] = i

        # Locate the complement
        for i in range(n):
            comp = target - nums[i]
            if comp in hash_map and hash_map[comp] != i:
                return [i, hash_map[comp]]

        return []