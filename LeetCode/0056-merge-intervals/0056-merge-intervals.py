class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        left, right = intervals[0][0], intervals[0][1]

        for i in intervals[1:]:
            if i[0] <= right <= i[1]:
                right = i[1]
            elif right < i[1]:
                result.append([left, right])
                left, right = i[0], i[1]

        if result == [] or result[-1][1] < right:
            result.append([left, right])

        return result