from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        R, C = len(board), len(board[0])
        q = []
        for r in range(R):
            for c in range(C):
                if (r == 0 or r == R - 1 or c == 0 or c == C - 1) and board[r][c] == 'O':
                    board[r][c] = '#'
                    q.append((r, c))
        for r, c in q:
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    q.append((nr, nc))
        for r in range(R):
            for c in range(C):
                board[r][c] = 'O' if board[r][c] == '#' else 'X'