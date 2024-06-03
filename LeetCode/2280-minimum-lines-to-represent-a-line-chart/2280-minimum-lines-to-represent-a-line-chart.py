class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)

        if n < 2:
            return n - 1

        stockPrices.sort()
        dx = stockPrices[0][0] - stockPrices[1][0]
        dy = stockPrices[0][1] - stockPrices[1][1]

        count = 1

        for index in range(2, n):
            dx1 = stockPrices[index - 1][0] - stockPrices[index][0]
            dy1 = stockPrices[index - 1][1] - stockPrices[index][1]

            if dx1 * dy != dx * dy1:
                count += 1
                dx = dx1
                dy = dy1

        return count