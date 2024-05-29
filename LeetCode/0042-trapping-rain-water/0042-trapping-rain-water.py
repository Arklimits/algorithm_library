class Solution:
    def trap(self, height: List[int]) -> int:
        stack = deque()
        water = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                bound = min(height[i], height[stack[-1]]) - height[top]
                water += distance * bound

            stack.append(i)

        return water