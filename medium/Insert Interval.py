"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""


class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        """
        Create a return list. Let's call it final
        Start iteration through intervals
        Through each iteration, compare newInterval[0] with intervals[i][0]
        if newInterval[0] < intervals[i][0],
            create temp list with temp[0] = newInterval[0]
            start another iteration that continues from i
            if newInterval[1] < interval[i][0],
                return final + newInterval + intervals[i:]
            elif newInterval[1] in range(intervals[1][0],  intervals[i][1] + 1),
                return final + temp.append(intervals[i][1]) + intervals[i + 1:]
            else, continue 2nd iteration until one of the above conditions is met
                If not, return final + temp.append(newInterval[1])
        elif newInterval[0] in range(intervals[i][0], intervals[i][1] + 1),
            create temp list with temp[0] = intervals[i][0]
            start another iteration that continues from i
            if newInterval[1] < intervals[i][0],
                return final + temp.append(newInterval[1]) + intervals[i:]
            elif newIntervals[1] in range(intervals[1][0],  intervals[i][1] + 1),
                return final + temp.append(intervals[i][1]) + intervals[i + 1:]
            else, continue iteration until one of the above conditions is met
                If not, return final + temp.append(newInterval[1])
        else:
            final.append(intervals[i])

        if the algorithm ends without a return value, return intervals + [newIntervals, ]
        """
        # create a return list. Let's call it final
        final = []
        # start iteration through intervals using a while loop so that it stops at end of the list
        length = len(intervals)
        index = 0
        # Start iteration through intervals
        while index < length:
            if newInterval[0] < intervals[index][0]:
                temp = [newInterval[0], ]
                while index < length:
                    if newInterval[1] < intervals[index][0]:
                        return final + [newInterval, ] + intervals[index: ]
                    elif newInterval[1] in range(intervals[index][0], intervals[index][1] + 1):
                        return final + [(temp + [intervals[index][1], ]), ] + intervals[index + 1:]
                    index += 1
                return final + [temp + [newInterval[1], ],]
            elif newInterval[0] in range(intervals[index][0], intervals[index][1] + 1):
                temp = [intervals[index][0], ]
                while index < length:
                    if newInterval[1] < intervals[index][0]:
                        return final + [temp + [newInterval[1], ], ] + intervals[index: ]
                    elif newInterval[1] in range(intervals[index][0], intervals[index][1] + 1):
                        return final + [temp + [intervals[index][1], ], ] + intervals[index + 1: ]
                    index += 1
                return final + [temp + [newInterval[1], ], ]
            else:
                final.append(intervals[index])
            index += 1

        return intervals + [newInterval, ]
