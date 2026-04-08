class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>(); 
        int a = 0; 
        int b = 0;  
        int tmp = 0; 
        Set<String> operators = Set.of("+", "-", "*", "/");
        for (int i = 0; i < tokens.length; i++) {
            if (!operators.contains(tokens[i])) {
                stack.push(Integer.parseInt(tokens[i]));
            }
            else {
                System.out.println(stack.peek());
                b = stack.pop(); 
                System.out.println(stack.peek());

                a = stack.pop(); 

                if (tokens[i].equals("+")) {
                    tmp = a + b; 
                    stack.push(tmp); 
                }
                if (tokens[i].equals("*")) {
                    tmp = a * b; 
                    stack.push(tmp); 
                }
                if (tokens[i].equals("-")) {
                    tmp = a - b; 
                    stack.push(tmp); 
                }if (tokens[i].equals("/")) {
                    tmp = a / b; 
                    stack.push(tmp); 
                }
            }
        }
        return stack.peek();
    }
}
