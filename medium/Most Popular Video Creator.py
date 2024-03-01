"""
You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video on a
platform was created by creator[i], has an id of ids[i], and has views[i] views.

The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the
 highest popularity and the id of their most viewed video.

If multiple creators have the highest popularity, find all of them.
If multiple videos have the highest view count for a creator, find the lexicographically smallest id.
Return a 2D array of strings answer where answer[i] = [creatori, idi] means that creatori has the highest popularity and
 idi is the id of their most popular video. The answer can be returned in any order.



Example 1:

Input: creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
Output: [["alice","one"],["bob","two"]]
Explanation:
The popularity of alice is 5 + 5 = 10.
The popularity of bob is 10.
The popularity of chris is 4.
alice and bob are the most popular creators.
For bob, the video with the highest view count is "two".
For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than
"three", it is included in the answer.
Example 2:

Input: creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]
Output: [["alice","b"]]
Explanation:
The videos with id "b" and "c" have the highest view count.
Since "b" is lexicographically smaller than "c", it is included in the answer.


Constraints:

n == creators.length == ids.length == views.length
1 <= n <= 105
1 <= creators[i].length, ids[i].length <= 5
creators[i] and ids[i] consist only of lowercase English letters.
0 <= views[i] <= 105
"""


class Solution:
    def mostPopularCreator(self, creators: [str], ids: [str], views: [int]) -> [[str]]:
        """
        Use a dict: creators for keys and a list for values.
        The values list[0] == most popular video id and list[1] == total views
        Sort dict items using values[1]
        Return a list with key and value[0] for items with the most values[1]
        """
        records = {}
        for i in range(len(creators)):
            try:
                records[creators[i]][1] += views[i]
            except KeyError as k:
                records[creators[i]] = [[ids[i], i], views[i]]
            else:
                if views[i] > views[records[creators[i]][0][1]]:
                    records[creators[i]][0][0] = ids[i]
                    records[creators[i]][0][1] = i
                elif views[i] == views[records[creators[i]][0][1]]:
                    if ids[i] < records[creators[i]][0][0]:
                        records[creators[i]][0][0] = ids[i]

        y = sorted(records.items(), key=lambda x: x[1][1], reverse=True)
        most = y[0][1][1]
        return [[item[0], item[1][0][0]] for item in y if item[1][1] == most]
