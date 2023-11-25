from typing import List
from collections import defaultdict

class Twitter:

   def __init__(self):
        self.follow_list = defaultdict(list)
        self.post_list = defaultdict(list)

   def post_tweet(self, user_id, tweet_id):
        if user_id not in self.post_list.keys():
             self.post_list[user_id] = [tweet_id]
        else:
            self.post_list[user_id].append(tweet_id)

   def get_news_feed(self, user_id) -> List[int]:
        res = []
        for user_key, post_value in self.post_list.items():
             if user_id in self.follow_list[user_key]:
                  res.extend(post_value)

        return res[::-1][:10]

   def follow(self, follower_id, followee_id):
        if followee_id not in self.follow_list.keys():
             self.follow_list[followee_id] = [follower_id]
        else:
            self.follow_list[followee_id].append(follower_id)

   def unfollow(self, follower_id, followee_id):
        self.follow_list[followee_id].remove(follower_id)
   
   def get_follow(self):
        print(self.follow_list)
        print(self.post_list)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)

twitter = Twitter()
twitter.follow(1, 2)
twitter.follow(1, 3)
twitter.post_tweet(2, 4)
twitter.post_tweet(2, 6)
twitter.post_tweet(3, 2)
twitter.post_tweet(3, 7)
twitter.post_tweet(3, 3)
twitter.post_tweet(3, 8)
twitter.post_tweet(2, 1)
twitter.post_tweet(2, 9)
twitter.follow(1, 4)
twitter.post_tweet(4, 5)
twitter.post_tweet(4, 10)
twitter.unfollow(1, 2)
twitter.post_tweet(5, 11)
twitter.post_tweet(5, 12)
twitter.post_tweet(5, 13)
twitter.post_tweet(6, 14)
twitter.follow(1, 5)
twitter.post_tweet(7, 15)
twitter.post_tweet(7, 16)
twitter.post_tweet(7, 17)
twitter.post_tweet(7, 18)
twitter.follow(1, 7)
print(twitter.get_news_feed(1))

# twitter.get_follow()