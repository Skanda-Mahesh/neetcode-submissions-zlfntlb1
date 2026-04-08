class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int [] hash = new int[26];
        List<List<String>> group = new ArrayList<List<String>>();
        
        for (int j = 0; j < strs.length; j++) {
            String word = strs[j]; 
            if (word == null) continue; 
            // Iterate through each, if an anagram is foudn add to list
            // At the end, add word itself 
            strs[j] = null;
            List<String> inner = new ArrayList<String>(); 
            inner.add(word); 
            
            for (int i = j + 1; i < strs.length; i++) {
                if (strs[i] != null && isAnagram(strs[i], word)) {
                    inner.add(strs[i]);
                    strs[i] = null;
                }
            }
            group.add(inner);

            
        }
        return group;
    }





    public static boolean isAnagram(String a, String b) {
        
        if (a.length() != b.length()) {
            return false; 
        }

        int [] hash = new int [26]; 

        for (int i = 0; i<a.length(); i++) {
            hash[a.charAt(i) - 'a']++;
            hash[b.charAt(i) - 'a']--;
        }


        for (int i : hash) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}
