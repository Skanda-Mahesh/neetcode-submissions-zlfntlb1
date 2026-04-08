class Solution {

    public String encode(List<String> strs) {
        StringBuilder answer = new StringBuilder("");
        for (String str : strs) {
            Integer len = str.length();
            StringBuilder tmp = new StringBuilder();
            tmp.append(len.toString());
            tmp.append('#');
            tmp.append(str);
            answer.append(tmp);

        }
        System.out.println(answer);
        return answer.toString();
    }

    public List<String> decode(String str) {

        ArrayList<String> answer = new ArrayList<>();
        int j = 0;
        int i = 0; 
        while (i < str.length()) {
            // j is the delimiter location
            j = i+1; 

            while (str.charAt(j) != '#') {
                j++;
            }

            // Length will be from i till j, not including j
            int length = Integer.parseInt(str.substring(i, j)); 

            String word = str.substring(j + 1, (length + j+1)); 
            i = j+1+length; 
            answer.add(word); 

        }
        return answer; 
    }
}
