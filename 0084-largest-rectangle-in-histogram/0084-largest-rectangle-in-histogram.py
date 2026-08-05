class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        next_smaller_to_left = [-1] * n
        next_smaller_to_right = [n] * n

        for i in range(n):
            while stack:
                if stack[-1][-1] < heights[i]:
                    next_smaller_to_left[i] = stack[-1][0]
                    stack.append((i, heights[i]))
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append((i, heights[i]))

        stack = []

        for i in range(n - 1, -1, -1):
            while stack:
                if stack[-1][-1] < heights[i]:
                    next_smaller_to_right[i] = stack[-1][0]
                    stack.append((i, heights[i]))
                    break
                else:
                    stack.pop()
            if not stack:
                stack.append((i, heights[i]))

        widths = [next_smaller_to_right[i] - next_smaller_to_left[i] - 1 for i in range(n)]

        ans = max(widths[i] * heights[i] for i in range(n))

        return ans