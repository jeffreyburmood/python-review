""" this exercise will count the number of subsequences that occur for a given string.
    a subsequence can be any of the following:
    1) all characters in a direct sequence, eg, ABC -> ABDABC -> indexes = (1,2,6), (4,5,6)
    2) all characters in an indirect sequence, eg, ABC -> ABDECB -> indexes = (1,2,5)
    The provided string is always three characters. Subsequences must always have the characters in the
    same order as the provided string. """

# const buildIndexArray = function (char, str) {
#   // initialize character index arrays
#   const indexes = [];
# 
#   // build character index array
#   let searchStr = str;
#   let searchResult = undefined;
#   while (true) {
#     searchResult = searchStr.indexOf(char);
#     if (searchResult === -1) break;
#     indexes.push(searchResult);
#     searchStr = searchStr.replace(char, "0");
#   }
# 
#   return indexes;
# };

def build_index_array(search_char:str, search_string:str) -> list:
    """ build an array of the indicies where the provided character appears in the provided string """
    indexes = []

    while True:
        try:
            search_result = search_string.index(search_char)
            indexes.append(search_result)
            search_string = search_string.replace(search_char, "0", 1)
        except ValueError:
            break
            
    return indexes


# const get_subsequence_count = function (s1, s2) {
#   // build index array for each character in s1
#   char1Indexes = buildIndexArray(s1[0], s2);
#   char2Indexes = buildIndexArray(s1[1], s2);
#   char3Indexes = buildIndexArray(s1[2], s2);
# 
#   // parse character index arrays and build index permutations
#   let subsequenceCnt = 0;
#   for (let i = 0; i < char1Indexes.length; i++) {
#     for (let j = 0; j < char2Indexes.length; j++) {
#       for (let k = 0; k < char3Indexes.length; k++) {
#         if (
#           char1Indexes[i] < char2Indexes[j] &&
#           char2Indexes[j] < char3Indexes[k]
#         )
#           subsequenceCnt++;
#       }
#     }
#   }
#   // return number of index permutations
#   return subsequenceCnt;
# };

def get_subsequence_count(s1:str, s2:str) -> int:
    
    char1_indexes = build_index_array(s1[0], s2)
    print(char1_indexes)
    char2_indexes = build_index_array(s1[1], s2)
    print(char2_indexes)
    char3_indexes = build_index_array(s1[2], s2)
    print(char3_indexes)
    
    subsequence_count = 0    
    for i in range(0, len(char1_indexes)):
        for j in range(0, len(char2_indexes)):
            for k in range(0, len(char3_indexes)):
                if char1_indexes[i] < char2_indexes[j] and char2_indexes[j] < char3_indexes[k]:
                    subsequence_count += 1
    
    return subsequence_count

print(get_subsequence_count("ABC", "ABCBABC"))
print(get_subsequence_count("HRW", "HWRWHHRWW"))
print(get_subsequence_count("XYZ", "XZYYXX"))
print(get_subsequence_count("ABD", "ABCBABC"))
