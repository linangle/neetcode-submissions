class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bfs problem where we look for the shortest path
        if amount == 0:
            return 0
        
        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    # if within bounds and unseen mark seen and push onto q
                    seen[nxt] = True
                    q.append(nxt)
        return -1