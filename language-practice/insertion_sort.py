""" this script will sort a list of key/value pairs """

class Pair:
    def __init__(self, key:int, value: str):
        self.key = key
        self.value = value

    def print_pair(self):
        tuple = (self.key, self.value)
        print(tuple)

class Solution:
    def insertionSort(self, pairs: list[Pair]) -> list[Pair]:
        sorted = []
        for pair in pairs:
            if len(sorted) == 0:
                sorted.append(pair)
            else:
                inserted = False
                i = 0
                while i < len(sorted) and not inserted:
                    if pair.key < sorted[i].key:
                        sorted.insert(i, pair)
                        inserted = True
                    elif pair.key == sorted[i].key:
                        sorted.insert(i+1, pair)
                        inserted = True
                    i += 1

                if not inserted:
                    sorted.append(pair)
        return sorted

solution = Solution()
pairs = [Pair(5, 'apple'), Pair(2, 'banana'), Pair(2, 'plantain'), Pair(9, 'cherry')]
sorted_pairs = solution.insertionSort(pairs)
for pair in sorted_pairs:
    pair.print_pair()