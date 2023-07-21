# Runtime 63ms
# Memory 16.49mb

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        item_list = [[] for i in range(numRows)]
        dwn = -1
        i = 0
        if numRows == 1:
            return s
        for j in s:
            item_list[i].append(j)
            if i == 0 or i == numRows - 1:
                dwn *= -1
            i += dwn
        item_list = list(chain(*item_list))
        return ''.join(item_list)