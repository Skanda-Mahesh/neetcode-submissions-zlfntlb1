class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // U dont actually need to calculate an array
        // By using the max and min, you "emulate" the k array

        int left = 1; 
        int right = 0; 
        
        for (int i = 0; i < piles.length; i++) {
            if (piles[i] > right) {
                right = piles[i];
            }
        }
        int result = right; 

        while (left <= right) {
            int mid = (int) (right + left) / 2;
            int sum = 0; 
            for (int i = 0; i < piles.length; i++) {
                sum = sum + (int) Math.ceil((double) piles[i] / mid);
            }
            if (sum <= h) {
                result = Math.min(mid, result);
                right = mid - 1;  
            }
            else {
                left = mid + 1; 
            }

        }
        return result;
    }
}
