class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                if c == ")" and stack.pop() != "(":
                    return False
                elif c == "]" and stack.pop() != "[":
                    return False
                elif c == "}" and stack.pop() != "{":
                    return False

        if len(stack) != 0:
            return False

        return True
