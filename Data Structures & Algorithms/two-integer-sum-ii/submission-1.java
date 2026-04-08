class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Keep two pointers, moving from the LHS, one on the RHS
        // If the sum is greater, move Right pointer --
        // If the sum is lesser, move the left pointer ++; 


        int lower = 0; 
        int right = numbers.length - 1; 
        int sum = 0; 
        int [] ans = new int[2]; 
        while (lower < right) {
            sum = numbers[lower] + numbers[right]; 
            if (sum == target) {
                ans[0] = ++lower; 
                ans[1] = ++right;  
                break; 
            }
            
            else if (sum > target) {
                right--;
            }
            else if (sum < target) {
                lower++; 
            }
            
        
        }
        return ans; 
    }
}

