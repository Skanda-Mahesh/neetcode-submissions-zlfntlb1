class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> stack = new ArrayDeque<>(); 

        int[] result = new int[temperatures.length]; 

        for (int i = 0; i < result.length; i++) {
            result[i] = 0; 
        }   
        int len = temperatures.length - 1 ; 
        for (int i = len; i >= 0; i--) {
            // If stack empty, push, and leave as 0
            // If stack top greater, just push on
            // if stack top lesser, keep popping, then calc diff
            // IM STORING THE INDEXES, SO ITS EASY

            if (stack.isEmpty()) {
                result[i] = 0; 
                stack.push(i); 
            }

            else if (temperatures[stack.peek()] > temperatures[i]) {
                result[i] = stack.peek() - i; 
                stack.push(i); 
            }

            else if (temperatures[stack.peek()] <= temperatures[i]) {
                while (!stack.isEmpty() && temperatures[stack.peek()] <= temperatures[i]) {
                    stack.pop(); 
                }
                if (stack.isEmpty()) {
                    result[i] = 0; 
                    stack.push(i); 
                }
                else {
                result[i] = stack.peek() - i; 
                stack.push(i);
                }
            }

        }
        return result; 
    }
}
