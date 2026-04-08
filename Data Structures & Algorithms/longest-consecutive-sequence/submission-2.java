class Solution {
    public int longestConsecutive(int[] nums) {
       Set<Integer> set = new HashSet<>(); 

       for (int i = 0; i < nums.length; i++) {
        set.add(nums[i]);
       } 
        
        if (nums.length == 0) return 0;
       int longest = 1; 

       for (int i = 0; i < nums.length; i++) {
        int current = nums[i]; 
        if (set.contains(current+1)) {
            int tmp = 1; 
            while (set.contains(current+1)) {
                tmp++; 
                current++; 
            }
            if (tmp > longest) {
                longest = tmp; 
            }
        }
       }
       return longest; 
    }
}
