class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}
        sum = 0
        count = 0

        for num in nums:
            sum += num
            if sum - k in sum_map:
                count += sum_map[sum - k]
            if sum in sum_map:
                sum_map[sum] += 1
            else:
                sum_map[sum] = 1

        return count