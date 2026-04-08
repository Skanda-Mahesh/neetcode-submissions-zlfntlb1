class Solution {
    public boolean isPalindrome(String s) {
        int start = 0; 
        int end = s.length()-1; 
        String sen = s.toLowerCase(); 
        while (start <= end) {
            if (!Character.isLetterOrDigit(sen.charAt(start))) {
                start++;  
                continue;
            } 
            if (!Character.isLetterOrDigit(sen.charAt(end))) {
                end--; 
                continue;
            } 
            if (sen.charAt(start) == sen.charAt(end)) {
                start++; 
                end--; 
            }
            else {
                System.out.println(sen.charAt(start));
                System.out.println(sen.charAt(end)); 

                System.out.println(start); 
                System.out.println(end); 

                return false;
            }
        } 
        return true;
    }
}
