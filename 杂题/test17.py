# 携程2

class Solution:
    def get_out(self, matrix):
        if not matrix: return []
        ans = []
        row1 = 0
        row2 = len(matrix) - 1
        col1 = 0
        col2 = len(matrix[0]) - 1

        while row1 <= row2 and col1 <= col2:
            for r, c in self.spiral_operate(row1, col1, row2, col2):
                ans.append(matrix[r][c])
            row1 += 1
            row2 -= 1
            col1 += 1
            col2 -= 1
        return ans

    def spiral_operate(self, row1, col1, row2, col2):
        for c in range(col1, col2 + 1):
            yield row1, c
        for r in range(row1 + 1, row2 + 1):
            yield r, col2
        if row1 < row2 and col1 < col2:
            for c in range(col2 - 1, col1, -1):
                yield row2, c
            for r in range(row2, row1, -1):
                yield r, col1

if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = []
    i = 0
    while i < m:
        i += 1
        lyst = list(map(int, input().split()))
        matrix.append(lyst)

    solu1 = Solution()

    result = solu1.get_out(matrix)
    print(",".join(map(str, result)))
