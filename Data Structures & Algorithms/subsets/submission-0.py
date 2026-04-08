class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmplist = []

        def helper(i, tmplist, ans, nums):
            if i >= len(nums):
                ans.append(tmplist.copy())
                return
            
            # Adding value 
            tmplist.append(nums[i])
            helper(i+1, tmplist, ans, nums)
            tmplist.pop()

            # Dont select val 
            helper(i+1, tmplist, ans, nums)

        helper(0,tmplist,ans, nums)
        return ans