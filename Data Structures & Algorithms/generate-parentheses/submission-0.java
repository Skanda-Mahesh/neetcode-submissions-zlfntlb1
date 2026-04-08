class Solution {
    public List<String> generateParenthesis(int n) {
        StringBuilder stack = new StringBuilder(); 
        List<String> result = new ArrayList<>(); 
        backtrack(n, 0, 0, stack, result); 
        return result;
    }

    public static void backtrack(int n, int openN, int closedN, StringBuilder stack,List<String> result) {
        if (openN == closedN && closedN == n) {
            result.add(stack.toString()); 
            return;
        }

        if (openN < n) {
            stack.append("(");
            backtrack(n, openN+1, closedN, stack, result);
            stack.deleteCharAt(stack.length() - 1); 
        }
        
        if (closedN < openN) {
            stack.append(")"); 
            backtrack(n, openN, closedN+1, stack, result); 
            stack.deleteCharAt(stack.length() -1); 
        }
    }
}
