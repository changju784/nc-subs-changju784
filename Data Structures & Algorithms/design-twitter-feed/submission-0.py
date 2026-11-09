"""
tweets 
- unique ids 
- tied to user id 
- one user can post multiple tweets 
- fetch tweet should get: 
    - followers post 
    - ordered by frequently post 

{
0: [53, 21]
1: [0, 1, 2, 3]
2: [321, 132]
3: [11, 221]
}

{
0: 1,
0: 2
}
0 -> 1
[(1, 0), ]

users 
- following func 
- hashmap key - follower, value - followee 

"""
from collections import defaultdict
import heapq
class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.posts = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] 
        # get followers and myself 
        followers = [userId] + list(self.users[userId])
        for follower in followers: 
            for ts, tweetId in self.posts[follower]:
                heapq.heappush(heap, (ts, tweetId))
                if len(heap) > 10: 
                    heapq.heappop(heap) 
        result = [] 
        while heap: 
            _, ti = heapq.heappop(heap)
            result.append(ti)
        return result[::-1]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.users[followerId].discard(followeeId)
        
