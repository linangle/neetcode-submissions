class TrieNode:
    def __init__(self):
        self.children = {} # hash map : letter --> TrieNode
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: # if we haven't found the letter yet
                cur.children[c] = TrieNode() # make it a node in the trie
            cur = cur.children[c] # move the pointer down to the child node
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # goal : returns true if there is any string that matches word
            # else return false
            # word may contain dots "." where dots can be matched with any letter
            def dfs(j, root):
                cur = root # initialize the pointer at the root

                for i in range(j, len(word)):
                    c = word[i]
                    if c == ".":
                        # cur.children.values() are the TrieNodes
                        for child in cur.children.values():
                            if dfs(i + 1, child):
                                return True
                        return False
                    else: 
                        if c not in cur.children: # if we haven't seen a letter 
                            return False 
                        cur = cur.children[c] # move the pointer
                return cur.endOfWord

            return dfs(0, self.root)
        
