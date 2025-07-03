class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0

        while (i < n and newInterval[0] > intervals[i][1]):
            result.append(intervals[i])
            i += 1
        
        start = newInterval[0]
        end = newInterval[1]

        while (i < n and end >= intervals[i][0]):
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i = i+1
        
        result.append([start, end])

        while (i < n) :
            result.append(intervals[i])
            i = i+1
        
        return result


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0

        while(i < n and intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
            i += 1

        start = newInterval[0]
        end = newInterval[1]

        while(i < n and end >= intervals[i][0]):
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        result.append([start, end])

        while(i < n):
            result.append(intervals[i])
            i += 1

        return result