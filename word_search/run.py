class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        self.board = board

        startPositions = self.findAllFirstChars(word[0], self.board)
        if len(startPositions) == 0:
            return False

        curPositions = startPositions
        for pos in curPositions:
            if self.dfs(word, 1, pos, [pos]):
                return True

        return False

    def dfs(self, word, curIdx, curPos, traces):
        if curIdx == len(word):
            print(traces)
            return True

        lastAns = False

        # print("\n")
        # print("current_state:")
        # print(f"curIdx: {curIdx}")
        # print(f"curPos: {curPos}")
        # print(f"traces: {traces}")
        # print(f"now_char: {word[:curIdx]}")
        # print()

        upPos = [curPos[0], curPos[1] - 1]
        if (
            upPos not in traces
            and upPos[1] >= 0
            and self.board[upPos[0]][upPos[1]] == word[curIdx]
        ):
            # print(f"found {word[curIdx]} at {upPos}")
            lastAns |= self.dfs(word, curIdx + 1, upPos, traces + [upPos])

        leftPos = [curPos[0] - 1, curPos[1]]
        if (
            leftPos not in traces
            and leftPos[0] >= 0
            and self.board[leftPos[0]][leftPos[1]] == word[curIdx]
        ):
            # print(f"found {word[curIdx]} at {leftPos}")
            lastAns |= self.dfs(word, curIdx + 1, leftPos, traces + [leftPos])

        downPos = [curPos[0], curPos[1] + 1]
        if (
            downPos not in traces
            and downPos[1] < len(self.board[0])
            and self.board[downPos[0]][downPos[1]] == word[curIdx]
        ):
            # print(f"found {word[curIdx]} at {downPos}")
            lastAns |= self.dfs(word, curIdx + 1, downPos, traces + [downPos])

        rightPos = [curPos[0] + 1, curPos[1]]
        if (
            rightPos not in traces
            and rightPos[0] < len(self.board)
            and self.board[rightPos[0]][rightPos[1]] == word[curIdx]
        ):
            # print(f"found {word[curIdx]} at {rightPos}")
            lastAns |= self.dfs(word, curIdx + 1, rightPos, traces + [rightPos])

        return lastAns

    def findAllFirstChars(self, firstChar, board):
        positions = []

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == firstChar:
                    positions.append([i, j])

        return positions


if __name__ == "__main__":
    s = Solution()
    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
    )
    print()
    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )
    )
    print()
    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
    )
