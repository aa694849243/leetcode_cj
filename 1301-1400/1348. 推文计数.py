# -*- coding: utf-8 -*-
import bisect
import collections
from typing import List


# 请你实现一个能够支持以下两种方法的推文计数类 TweetCounts：
#
#  1. recordTweet(string tweetName, int time)
#
#
#  记录推文发布情况：用户 tweetName 在 time（以 秒 为单位）时刻发布了一条推文。
#
#
#  2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, i
# nt endTime)
#
#
#  返回从开始时间 startTime（以 秒 为单位）到结束时间 endTime（以 秒 为单位）内，每 分 minute，时 hour 或者 日 day
# （取决于 freq）内指定用户 tweetName 发布的推文总数。
#  freq 的值始终为 分 minute，时 hour 或者 日 day 之一，表示获取指定用户 tweetName 发布推文次数的时间间隔。
#  第一个时间间隔始终从 startTime 开始，因此时间间隔为 [startTime, startTime + delta*1>, [startTime
# + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ...
#  , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)>，其中 i 和 delta
# （取决于 freq）都是非负整数。
#
#
#
#
#  示例：
#
#  输入：
# ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFre
# quency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
#
# [[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute
# ","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
#
# 输出：
# [null,null,null,null,[2],[2,1],null,[4]]
#
# 解释：
# TweetCounts tweetCounts = new TweetCounts();
# tweetCounts.recordTweet("tweet3", 0);
# tweetCounts.recordTweet("tweet3", 60);
# tweetCounts.recordTweet("tweet3", 10);                             // "tweet3"
#  发布推文的时间分别是 0, 10 和 60 。
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。统
# 计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60> - > 2 条推文。
# tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2,1]
# 。统计频率是每分钟（60 秒），因此有两个有效时间间隔 1) [0,60> - > 2 条推文，和 2) [60,61> - > 1 条推文。
# tweetCounts.recordTweet("tweet3", 120);                            // "tweet3"
#  发布推文的时间分别是 0, 10, 60 和 120 。
# tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // 返回 [4]。统
# 计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211> - > 4 条推文。
#
#
#
#
#  提示：
#
#
#  同时考虑 recordTweet 和 getTweetCountsPerFrequency，最多有 10000 次操作。
#  0 <= time, startTime, endTime <= 10^9
#  0 <= endTime - startTime <= 10^4
#
#  Related Topics 设计 哈希表 二分查找 有序集合 排序
#  👍 21 👎 0
class TweetCounts:

    def __init__(self):
        self.m = collections.defaultdict(list)
        self.f = {'minute': 60, 'hour': 3600, 'day': 3600 * 24}

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort_left(self.m[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = self.f[freq]
        li = self.m[tweetName]
        ans = []
        l = startTime
        while l <= endTime:
            l_ = bisect.bisect_left(li, l)
            r_ = bisect.bisect_left(li, min(l + delta,endTime+1)) #右边界需要特殊处理下，因为假如形式是[1,6,9],l=2,endtime=5,delta=6的话，如果不加min(l+delta,endTime+1的话，ans会是1，实际答案是0
            ans.append(r_ - l_)
            l += delta
        return ans


with open(r'F:\新建文件夹\新建文件夹 (2)\a.txt') as f:
    a = f.read()
with open(r'F:\新建文件夹\新建文件夹 (2)\b.txt') as f:
    b = f.read()
a=eval(a)
b=eval(b)
# Your TweetCounts object will be instantiated and called as such:
obj = TweetCounts()
ans = []
for i, s in enumerate(b[1:],1):
    if s=='recordTweet':
        obj.recordTweet(*a[i])
    else:
        ans.append(obj.getTweetCountsPerFrequency(*a[i]))

# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
