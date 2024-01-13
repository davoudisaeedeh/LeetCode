class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            lens = [len(i) for i in strs]
            smallest_str = strs[lens.index(min(lens))]
            index = 0
            common = ""
            while index != min(lens):
                if len(list(set([item[index] for item in strs]))) == 1 and index != min(lens):
                    common += smallest_str[index]
                    index += 1
                else:
                    return common
            return common