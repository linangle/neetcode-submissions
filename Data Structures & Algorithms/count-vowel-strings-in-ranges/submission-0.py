class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    # idea: precompute prefix sum array where prefix[i]
        # stores the count of vowel strings from 0 to i - 1

        vowel_set = set("aeiou")
        prefix_cnt = [0] * (len(words) + 1)
        res = [0] * len(queries)
        prev = 0

        for i, w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set: 
                prev += 1
            prefix_cnt[i + 1] = prev
        
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_cnt[r + 1] - prefix_cnt[l]
        
        return res
