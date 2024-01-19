class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lists = []
        for i in range(1, numRows+1):
            new = [1] * i
            for j in range(1, (i-1)//2+1):
                val = lists[-1][j]+lists[-1][j-1]
                new[j], new[-j-1] = val, val
            lists.append(new)
        return lists