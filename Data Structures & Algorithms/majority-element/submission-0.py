class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for ele in nums: 
            if ele in map: 
                map[ele] += 1
            else: 
                map[ele] =1 
        
        for ele in map: 
            if map[ele] > (len(nums)/2):
                return ele
                
