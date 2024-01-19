class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            list_of_lists = [[1], [1,1]]
            for _ in range(numRows-2):
                new = [1]
                for i in range(1, len(list_of_lists[-1])):
                    new.append(list_of_lists[-1][i]+list_of_lists[-1][i-1])
                new.append(1)
                list_of_lists.append(new)
            return list_of_lists