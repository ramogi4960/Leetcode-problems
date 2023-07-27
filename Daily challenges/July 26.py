from math import ceil
"""
You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute
to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where
dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on
the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach
the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal
point.

Input: dist = [1,3,2], hour = 6
Output: 1
Explanation: At speed 1:
-The first train ride takes 1/1 = 1 hour.
-Since we are already at an integer hour,we depart immediately at the 1 hour mark.The second train takes 3/1 = 3 hours.
-Since we are already at an integer hour,we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
-You will arrive at exactly the 6 hour mark.

Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
-The first train ride takes 1/3 = 0.33333 hours.
-Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
-Since we are already at an integer hour, we depart immediately at the 2 hour mark.
The third train takes 2/3 = 0.66667 hours.
-You will arrive at the 2.66667 hour mark.

Input: dist = [1,3,2], hour = 1.9
Output: -1
Explanation: It is impossible because the earliest the third train can depart is at the 2 hour mark.
"""

""" THE SLOW WAY (according to leetcode.com) """


class Solution:
    def minSpeedOnTime(self, dist: [int], hour: float) -> int:
        # we need to iterate through all items in dist to find the total time taken
        # we also need a variable for the speed that keeps adding by 1 if the
        # total time taken at that speed is more than hour
        # we can first give the speed as the lowest integer, 1 since the speed can't
        # be 0
        # we can also give a random time which is first more than hour, but keeps
        # on taking the value of the total time taken after every iteration
        if len(dist) - 1 > hour:
            return -1
        speed = 1  # km/hr
        time_taken = hour + 1
        while time_taken > hour:
            t = 0
            for i in range(len(dist)):
                if i == len(dist) - 1:
                    t += dist[i] / speed
                else:
                    if dist[i] / speed == int(dist[i] / speed):
                        t += dist[i] / speed
                    else:
                        t += int(dist[i] / speed) + 1

            time_taken = t
            speed += 1

        return speed - 1


""" THE FAST WAY (beats 99% of users in speed)"""


class Solution:
    def minSpeedOnTime(self, dist, hour):
        n = len(dist)  # Get the size of the input list 'dist' (number of distances to travel)
        minSpeed, maxSpeed = 1, 10**7 + 1  # Initialize the minimum and maximum possible speeds
        answer = -1  # Initialize the variable to store the final answer

        while minSpeed < maxSpeed:  # Binary search loop to find the minimum required speed
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2  # Calculate the middle speed

            totalHours = 0.0  # Initialize total travel time to 0

            # Calculate the total hours required to travel each distance at the current middle speed
            for i in range(n - 1):
                # Add the time taken to travel distance at index i using current midSpeed to totalHours
                totalHours += (dist[i] + midSpeed - 1) // midSpeed

            # Add the time taken to travel the last distance using current midSpeed to totalHours
            totalHours += dist[n - 1] / midSpeed

            if totalHours > hour:
                # If the total hours exceed the given hour, update minSpeed to consider higher speeds
                minSpeed = midSpeed + 1
            else:
                # If the total hours are within the given hour, update the answer to the current speed
                # and search for a potentially smaller speed in the lower half of the range.
                answer = midSpeed
                maxSpeed = midSpeed

        return answer  # Return the minimum speed required to reach the destination on time

