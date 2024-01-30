class Solution:
    def heap_sort(self, input):
        self.arr = []

        n = len(input)

        self._build_heap(input)

        result = []
        for _ in range(n):
            a = self._pop_heap()
            result.append(a)

        return result

    def print_heap(self):
        ## Used for debugging
        import math

        if len(self.arr) == 0:
            print("0 nodes")
            return

        height = math.ceil(math.log(len(self.arr), 2))

        for h in range(height):
            start = math.pow(2, h) - 1
            end = min(start + math.pow(2, h), len(self.arr))

            for i in range(int(start), int(end)):
                print(self.arr[i], end=" ")
            print()

        return

    def _build_heap(self, input):
        for a in input:
            self.arr.append(a)
            self._fix_up(len(self.arr) - 1)

    def _fix_up(self, pos):
        if pos < 1:
            return

        upper_pos = (pos - 1) // 2

        if self.arr[upper_pos] > self.arr[pos]:
            return

        self._swap(pos, upper_pos)
        self._fix_up(upper_pos)
        return

    def _fix_down(self, pos):
        low_left = pos * 2 + 1
        low_right = pos * 2 + 2
        last_pos = len(self.arr) - 1

        if low_left > last_pos:
            return

        if low_right > last_pos:
            if self.arr[pos] < self.arr[low_left]:
                self._swap(pos, low_left)
            return

        if self.arr[pos] > self.arr[low_left] and self.arr[pos] > self.arr[low_right]:
            return

        if (
            self.arr[pos] < self.arr[low_left]
            and self.arr[low_left] > self.arr[low_right]
        ):
            self._swap(pos, low_left)
            self._fix_down(low_left)
            return

        if (
            self.arr[pos] < self.arr[low_right]
            and self.arr[low_right] > self.arr[low_left]
        ):
            self._swap(pos, low_right)
            self._fix_down(low_right)
            return

        raise ("Should not be here")

    def _pop_heap(self):
        ans = self.arr[0]

        self.arr[0] = self.arr[-1]
        self.arr = self.arr[:-1]

        self._fix_down(0)

        return ans

    def _swap(self, pos1, pos2):
        tmp = self.arr[pos1]
        self.arr[pos1] = self.arr[pos2]
        self.arr[pos2] = tmp


if __name__ == "__main__":
    s = Solution()

    testCases = [
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [5, 4, 3, 2, 1],
        [1, 3, 5, 7, 2, 4, 6],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [5, 4, 3, 2, 1, 0],
        [1, 3, 5, 7, 9, 2, 4, 6, 8],
    ]

    for testCase in testCases:
        print("input:", testCase)
        result = s.heap_sort(testCase)
        print("output:", result, end="\n\n")
