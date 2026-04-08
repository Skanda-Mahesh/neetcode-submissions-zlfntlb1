class MinStack {

    private int[] stack = new int[200];
    private int top = 0;
    
    private int[] minStack = new int[50];
    
    private int minTop = 0;

    public MinStack() {}
        
    

    public void push(int val) {
        stack[top++] = val;
        if (minTop == 0) {
            minStack[minTop++] = val;
        }
        else if (minStack[minTop - 1] >= val) {
            minStack[minTop++] = val;
        } 
        }
    

    public void pop() {
        if (stack[top - 1] == minStack[minTop - 1]) {
            minTop--; 
            top--;
        }
        else { 
            top--;
        }
    
    }

    public int top() {
        return stack[top - 1];
    }

    public int getMin() {
        System.out.println(minTop);
        System.out.println(minStack[minTop-1]);
        return minStack[minTop - 1];
    }
}
