class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dist = {}
        for num in nums:
            if num in dist.keys():
                return True
            else:
                dist[num]=1
        return False
        