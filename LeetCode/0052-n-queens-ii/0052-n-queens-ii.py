count = 0

class Solution:
    def totalNQueens(self, n: int) -> int:
        def queen(now, basket):
            global count

            if now >= n:
                count += 1
                return

            for i in range(n - now):
                pivot = basket[0]
                del basket[0]
                if not up[now + pivot] and not down[now - pivot]:
                    up[now + pivot] = down[now - pivot] = 1
                    queen(now + 1, basket)
                    up[now + pivot] = down[now - pivot] = 0
                basket.append(pivot)

            return

        up = [0] * (n * 2 - 1)
        down = [0] * (n * 2 - 1)

        arr = [i for i in range(n)]

        global count
        count = 0

        queen(0, arr)

        return count