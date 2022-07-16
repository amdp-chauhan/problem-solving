
"""
URL - https://leetcode.com/problems/out-of-boundary-paths/
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        if not 0<=startRow<m or not 0<=startColumn<n:
            return 1

        if maxMove==0:
            return 0

        return self.findPaths(m, n, maxMove-1, startRow-1, startColumn) + self.findPaths(m, n, maxMove-1, startRow+1, startColumn) + self.findPaths(m, n, maxMove-1, startRow, startColumn-1) + self.findPaths(m, n, maxMove-1, startRow, startColumn+1)%((10**9)+7)
