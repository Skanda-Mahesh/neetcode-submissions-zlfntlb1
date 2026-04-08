class Solution {
    public int[] productExceptSelf(int[] nums) {
        // We need to first make a prefix array, then a postifix array
        // The product of both these arrays form the answers 
        // THe prefix array is the product of all the numbers, not including it itself 

        int end = nums.length - 1;

        int [] ans = new int[nums.length]; 

        ans[0] = 1; 
        for (int i = 1; i < nums.length; i++) {
            // Prefix time
            ans[i] = ans[i-1] * nums[i-1]; 
        }
        // The end of the array is just the prefix till then 
        // So i dont need to put a 1 
        // Just continue calculating the postfix
        int postfix = 1; 
        for (int i = end; i >= 0; i--) {
            ans[i] = ans[i] * postfix; 
            postfix = nums[i] * postfix;

        }
        return ans;
    }
}  
