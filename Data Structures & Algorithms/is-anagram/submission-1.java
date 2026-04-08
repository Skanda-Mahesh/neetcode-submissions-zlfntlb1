class Solution {
    public boolean isAnagram(String s_String, String t_String) {
        HashMap<Character, Integer> s = new HashMap<>();
        HashMap<Character, Integer> t = new HashMap<>();
        
        char s_array[] = s_String.toCharArray();
        char t_array[] = t_String.toCharArray(); 
        if (s_array.length != t_array.length) {
            return false;
        }
        for (int i = 0; i < s_array.length; i++) {
            if (s.containsKey(s_array[i])) {
                int tmp = s.get(s_array[i]);
                tmp++; 
                s.put(s_array[i], tmp);
            }
            else {
                s.put(s_array[i], 1); 
            }
            if (t.containsKey(t_array[i])) {
                int tmp = t.get(t_array[i]);
                tmp++; 
                t.put(t_array[i], tmp);
            }
            else {
                t.put(t_array[i], 1);
            }
        }

        for (Character key : s.keySet()) {
             if (!s.get(key).equals(t.get(key))) {
                return false;
             }
        }
        return true;
    }
}
