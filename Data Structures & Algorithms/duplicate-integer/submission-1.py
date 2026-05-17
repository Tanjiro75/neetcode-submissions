class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dist = set()
        for num in nums:
            if num in dist:
                return True
            dist.add(num)
        return False
        