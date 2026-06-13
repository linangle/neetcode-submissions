class TrieNode:
    def __init__(self):
        # each node contains
            # array of child pointers (one for each letter)
        self.children = [None] * 26
            # indicator for end of the word
        self.endOfWord = False

class PrefixTree:
    # array sol
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a") # normalize with a at index 0
            if cur.children[i] == None: # if we haven't seen this letter
                cur.children[i] = TrieNode() # make the letter a trie node
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None: # if we haven't seen it before
                return False # it's not in the trie
            cur = cur.children[i]
        return cur.endOfWord # return true only if end of word is true
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return True
        