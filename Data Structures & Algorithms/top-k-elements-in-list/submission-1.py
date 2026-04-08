class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for i in nums:
            if i in freq: 
                tmp = freq[i]
                tmp+=1
                freq[i] = tmp
            else:
                freq[i] = 1
        
        element = []
        frequency = []
        # Bucket logic now
        for key, value in freq.items(): 
            element.append(key)
            frequency.append(value)

        bucket = [[] for _ in range(len(nums) + 1)]
        
        for i in range(len(element)): 
            tmp = bucket[frequency[i]]
            tmp.append(element[i])
            bucket[frequency[i]] = tmp

        ans = []
        index = len(bucket) -1
        while len(ans) != k: 
            if not bucket[index]:
                index-= 1
                continue 
            ans.append(bucket[index].pop())
            
        return ans
            