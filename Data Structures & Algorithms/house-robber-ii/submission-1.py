class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            r1, r2 = 0, 0
            for n in arr:
                tmp = max(r1+n, r2)
                r1 = r2
                r2 = tmp
            return r2
        print(nums[:-1])
        print(nums[1:])
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))