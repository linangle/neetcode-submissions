class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
    # dfs sol : build ordering, detect cycles
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # w2 is a prefix of w1 and shorter (not possible)
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # edge from w1[j] --> w2[j]
                    break
        
        # 3-state tracking 
            # visiting : currently in path --> cycle if seen again
            # visited : fully processed --> skip
            # unvisited
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            # for each letter greater than this letter
            for neighChar in adj[char]: 
                if dfs(neighChar):
                    return True
            
            visited[char] = False # reset visiting state
            res.append(char)
        
        for char in adj:
            if dfs(char): # is True
                return "" 
        
        res.reverse()
        return "".join(res)



