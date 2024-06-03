class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        if right == 0:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left = mid - 1
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        else:
            return [-1, -1]

        while left > 0 and nums[left] >= target:
            left -= 1

        while left < 0 or nums[left] < target:
            left += 1

        for i in range(left, right + 1):
            if nums[i] != target:
                right = i - 1
                break

        return [left, right]