class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        arr = nums
        left = 0; 
        right = 0; 
        for i in range(len(nums)-2): 
            if i != 0 and arr[i] == arr[i-1]:
                continue
            
            left = i+1
            right = len(arr)-1

            total = -arr[i]

            while left < right: 
                ltotal = arr[left] + arr[right]

                if ltotal == total: 
                    answer.append([arr[i], arr[left], arr[right]])
                    left+=1
                    right -= 1

                    while left < right and arr[left-1] == arr[left]:
                        left+= 1
                        continue

                    while left < right and arr[right+1] == arr[right]:
                        right-= 1
                        continue


                elif ltotal < total:
                    left+=1; 
                elif ltotal > total: 
                    right-=1;


        return answer
                
                

                 

                    
                

            