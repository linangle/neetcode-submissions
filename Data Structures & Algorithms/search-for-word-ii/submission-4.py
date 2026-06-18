class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        m, n = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # if out of bounds or not in node.children
            if r < 0 or c < 0 or r >= m or c >= n or (r, c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r, c))
            # move the trie pointer
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord: # if we've completed the word, add it to the results
                res.add(word)
            
            # explore the board in all directions, adding to word
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, node, word)

            visit.remove((r, c))
        
        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
        
        return list(res)

