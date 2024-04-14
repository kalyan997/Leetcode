class Twitter:

    def __init__(self):
        self.time = 0
        self.user_following = defaultdict(set)
        self.user_tweetsTime = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweetsTime[userId].append([self.time,tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []
        self.user_following[userId].add(userId)
        for following in self.user_following[userId]:
            for curr_tweet in self.user_tweetsTime[following]:
                heapq.heappush(min_heap,curr_tweet)
                if len(min_heap)>10:
                    heapq.heappop(min_heap)
        while min_heap:
            res.append(heapq.heappop(min_heap))
        print(res)
        fin_res = []
        for item in reversed(res):
            fin_res.append(item[1])
        
        return fin_res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)