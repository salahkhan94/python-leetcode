class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])

        start = points[0][0]
        end = points[0][1]

        intersected_intervals = []

        for interval in points:
            cur_start = interval[0]
            cur_end = interval[1]

            if cur_start > end :
                intersected_intervals.append([start, end])
                end = cur_end
            else:
                end = min(end, cur_end)
            start = max(start, cur_start)

        
        intersected_intervals.append([start, end])

        return len(intersected_intervals)

if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12]]
    
    solution = Solution()
    
    result = solution.findMinArrowShots(points)
    print(result)