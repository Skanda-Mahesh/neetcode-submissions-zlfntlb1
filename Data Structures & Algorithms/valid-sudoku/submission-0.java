class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Check rows 
        for (int i = 0; i < 9; i++) {
            Set<Character> rowset = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (rowset.contains(board[i][j])) {
                        return false; 
                    }
                    else {
                        rowset.add(board[i][j]);
                    }
                }
            }
        }
        
        for (int i = 0; i < 9; i++) {
            Set<Character> colset = new HashSet<>(); 
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    if (colset.contains(board[j][i])) {
                        return false;
                    }
                    else {
                        colset.add(board[j][i]);
                    }
                }
            }
        }
        for (int rowStart = 0; rowStart < 9; rowStart+= 3) {
            for (int colStart = 0; colStart<9; colStart+=3) {

                Set<Character> set = new HashSet<>(); 

                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        Character c = board[rowStart + i][colStart + j]; 

                        if (c != '.') {
                            if (set.contains(c)) {
                                return false;
                            }
                            else set.add(c);
                        }
                    }
                }
            } 
        }
        return true;
    }
}
