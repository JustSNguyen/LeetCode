from typing import List
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.followed = defaultdict(dict)
        self.tweet_time = 0
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_time, tweetId))
        self.tweet_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        max_heap = []

        self.followed[userId][userId] = 1

        for follow in self.followed[userId]:
            if self.tweets[follow]:
                tweet_time, tweet_id = self.tweets[follow][-1]
                tweet_index = len(self.tweets[follow]) - 1
                heapq.heappush(max_heap, (-tweet_time, tweet_index, follow))

        while max_heap and len(result) != 10:
            most_recent_tweet_info = heapq.heappop(max_heap)
            tweet_index = most_recent_tweet_info[1]
            tweet_user_id = most_recent_tweet_info[2]
            tweet_id = self.tweets[tweet_user_id][tweet_index][1]

            result.append(tweet_id)

            if tweet_index - 1 >= 0:
                new_tweet_info = self.tweets[tweet_user_id][tweet_index - 1]
                tweet_time = new_tweet_info[0]
                heapq.heappush(max_heap, (-tweet_time, tweet_index - 1, tweet_user_id))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            del self.followed[followerId][followeeId]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)