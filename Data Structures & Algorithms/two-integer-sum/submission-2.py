class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, value in enumerate(nums):
            dict[value] = index
        
        ans = [0] * 2
        for index, value in enumerate(nums):
            other = target - value
            if other in dict and index != dict[other]: 
                ans[0] = index
                ans[1] = dict[other]
                return ans