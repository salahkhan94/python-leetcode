class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        output = []
        for interval in intervals:
            cur_start = interval[0]
            cur_end = interval[1]
            if cur_start > end:
                output.append([start, end])
                start = cur_start
            end = max(end, cur_end)
        output.append([start, end])
        return output


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # 2. Initialize output list with the first interval
        merged = [intervals[0]]
        
        # 3. Iterate through the rest of the intervals
        for current in intervals[1:]:
            # Compare current interval to the last interval in merged
            last_start, last_end = merged[-1]
            current_start, current_end = current
            
            # If there's an overlap, merge
            if current_start <= last_end:
                merged[-1][1] = max(last_end, current_end)
            else:
                merged.append(current)
        
        return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]

        for interval in intervals:
            cur_start = interval[0]
            cur_end = interval[1]
            if (cur_start > end) :
                merged.append([start, end])
                start = cur_start
            end = max(end, cur_end)

        
        merged.append([start, end])
        return merged



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        merged = []
        for interval in intervals:
            cur_start = interval[0]
            cur_end = interval[1]
            if (cur_start > end):
                merged.append([start, end])
                start = cur_start
            end = max(end, cur_end)
        
        merged.append([start, end])
        return merged

