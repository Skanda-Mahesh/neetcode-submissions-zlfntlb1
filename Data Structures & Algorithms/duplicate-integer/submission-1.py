class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setof = set(nums)
        if len(setof) < len(nums):
            return True
        else:
            return False