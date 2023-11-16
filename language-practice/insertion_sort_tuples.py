""" this script will create an insertion sort using tuples """

class Solution:
    def insertionSort(self, pairs: list[tuple]) -> list[tuple]:
        sorted = []
        for pair in pairs:
            if len(sorted) == 0:
                sorted.append(pair)
            else:
                inserted = False
                i = 0;
                while i < len(sorted) and not inserted:
                    if pair[0] < sorted[i][0]:
                        sorted.insert(i, pair)
                        inserted = True
                    elif pair[0] == sorted[1][0]:
                        sorted.insert(i+1, pair)
                        inserted = True
                    i += 1

                if not inserted:
                    sorted.append(pair)
        return sorted

solution = Solution()
pairs = [(5, 'apple'), (2, 'banana'), (2, 'plantain'), (9, 'cherry')]
sorted_pairs = solution.insertionSort(pairs)
for pair in sorted_pairs:
    print(pair)
