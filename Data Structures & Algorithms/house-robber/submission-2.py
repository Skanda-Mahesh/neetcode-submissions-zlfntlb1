class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[1], nums[0])

        for index in range(2, len(nums)):
            val = nums[index]
            arr[index] = max(arr[index-2] + val, arr[index-1])

        return arr[-1]

            
            

