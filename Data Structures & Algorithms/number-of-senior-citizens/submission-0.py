class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        
        for info in details:
            if int(info[11:13]) > 60:
                res += 1
                
        return res