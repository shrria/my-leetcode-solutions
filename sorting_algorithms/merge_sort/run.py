class Solution:
    def mergeSort(self, input):
        if len(input) <= 1:
            return

        midPos = len(input) // 2

        leftArray = input[:midPos]
        rightArray = input[midPos:]
        self.mergeSort(leftArray)
        self.mergeSort(rightArray)

        i = j = k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                input[k] = leftArray[i]
                i += 1
            else:
                input[k] = rightArray[j]
                j += 1

            k += 1

        if i < len(leftArray):
            input[k:] = leftArray[i:]

        if j < len(rightArray):
            input[k:] = rightArray[j:]


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
        s.mergeSort(testCase)
        print("output:", testCase, end="\n\n")
