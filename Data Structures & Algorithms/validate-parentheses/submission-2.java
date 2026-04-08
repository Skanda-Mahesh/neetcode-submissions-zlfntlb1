class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>(); 
        Set<Character> opening = Set.of('[', '(', '{');
        Set<Character> closing = Set.of(']', ')', '}');

        for (char ch : s.toCharArray()) {
            if (opening.contains(ch)) {
                stack.push(ch);
            }
            else {
                if (stack.isEmpty()) return false;
                switch (ch) {
                    case '}':
                        if (stack.peek().equals('{')) {
                            stack.pop(); 
                
                        }
                        else {
                            return false; 
                        }
                        break;
                    
                    case ']':
                        if (stack.peek().equals('[')) {
                            stack.pop(); 
                
                        }
                        else {
                            return false;
                        }
                        break;
                    
                    case ')':
                        if (stack.peek().equals('(')) {
                            stack.pop(); 
                
                        }
                        else {
                            return false;
                        }
                        break;
                    default:
                        return false; 
                }   

            }
        }
        if (!stack.isEmpty()) return false; 
        return true;
    }
}
