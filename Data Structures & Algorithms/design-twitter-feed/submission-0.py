class Twitter:

    def __init__(self):
        # decreasing timestamp for ordering tweets
        self.count = 0
        # maps userId --> (time, tweetID) sorted by freq
        self.tweetMap = defaultdict(list) 
        # maps userId -> set of followee
        self.followMap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # insert (timestamp, tweetId) at the end of the user's list
        self.tweetMap[userId].append([self.count, tweetId])
        # only keep the 10 most recent tweets, pop oldest one
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        # decrease global timestamp so newer tweets have smaller vals
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        # ensure user is following themselves
        self.followMap[userId].add(userId)
        # if greater than 10 followees
        if len(self.followMap[userId]) >= 10:
            # max heap that keeps 10 latest tweets from followees
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId,
                    followeeId, index -1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
