
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int tmp = 0; 
        for (int key : nums) {
            tmp = 0; 
            if (map.containsKey(key)) {
                tmp = map.get(key);
                tmp++;
                map.put(key, tmp);
            }
            else {
                map.put(key, 1);
            }
        }

        for (Integer key : map.keySet()) {
            if (map.get(key) > 1) {
                return true;
            }
        }
        return false;
    }
}