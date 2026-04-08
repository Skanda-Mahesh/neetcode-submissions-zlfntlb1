class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curset = []

        def backtrack(i, nums, ans, curset, target, cursum):
            if cursum > target or i >= len(nums):
                return

            if cursum == target:
                ans.append(curset.copy())
                return 
            
            # Choose that eleemnt, or dont 
            curset.append(nums[i])
            cursum += nums[i]
            backtrack(i, nums, ans, curset, target, cursum)
            curset.pop()
            cursum -= nums[i]
            backtrack(i+1, nums, ans, curset, target, cursum)

        backtrack(0, nums, ans, curset, target,0 )
        return ans
