
from collections import defaultdict
from heapq import nlargest
from typing import List

class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Dictionary mapping user_id to list of tweet_ids posted by that user
        self.user_tweets = defaultdict(list)
      
        # Dictionary mapping user_id to set of user_ids they follow
        self.user_following = defaultdict(set)
      
        # Dictionary mapping tweet_id to its timestamp
        self.tweets = defaultdict()
      
        # Global timestamp counter, incremented with each new tweet
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # Increment global timestamp
        self.time += 1
      
        # Add tweet to user's tweet list
        self.user_tweets[userId].append(tweetId)
      
        # Store tweet's timestamp for sorting purposes
        self.tweets[tweetId] = self.time

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users who the user followed 
        or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # Get the set of users this user follows
        following = self.user_following[userId]
      
        # Create set of all users whose tweets should appear in feed (followers + self)
        users = set(following)
        users.add(userId)
      
        # Collect the 10 most recent tweets from each user
        # Reverse each user's tweet list to get most recent first, then take up to 10
        tweets = [self.user_tweets[user][::-1][:10] for user in users]
      
        # Flatten the list of lists into a single list
        tweets = sum(tweets, [])
      
        # Return the 10 most recent tweets based on timestamp
        return nlargest(10, tweets, key=lambda tweet_id: self.tweets[tweet_id])

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # Add followee to follower's following set
        self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # Get the follower's following set
        following = self.user_following[followerId]
      
        # Remove followee if they exist in the following set
        if followeeId in following:
            following.remove(followeeId)
