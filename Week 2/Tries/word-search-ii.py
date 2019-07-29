class Solution(object):
    def findWords(self, board, words):
        """
        PROBLEM STATEMENT:
        Given a 2D board and a list of words from the dictionary, find all words in the board.
        Each word must be constructed from letters of sequentially adjacent cell, 
        where "adjacent" cells are those horizontally or vertically neighboring. 
        The same letter cell may not be used more than once in a word.
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            temp = trie
            for char in word:
                if char not in temp:
                    temp[char] = {}
                temp = temp[char]
            temp["#"] = word
            
        row, col = len(board),len(board[0])
        used = [[False for _ in range(col)] for _ in range(row)]
        boards = []
        
        def search(i, j, tries):
            used[i][j] = True
            next_tries = tries[board[i][j]]
            
            if "#" in next_tries and next_tries["#"] != "#":
                boards.append(next_tries["#"])
                next_tries["#"]="#"
                
            if i-1 >= 0 and not used[i-1][j] and board[i-1][j] in next_tries : search(i-1, j, next_tries)
            if j-1 >= 0 and not used[i][j-1] and board[i][j-1] in next_tries : search(i, j-1, next_tries)
            if i+1 < row and not used[i+1][j] and board[i+1][j] in next_tries : search(i+1, j, next_tries)
            if j+1 < col and not used[i][j+1] and board[i][j+1] in next_tries : search(i, j+1, next_tries)
            
            used[i][j] = False
            
        for i in range(row):
            for j in range(col):
                if board[i][j] in trie:
                    search(i,j,trie)
                    
        return boards
