# Runtime 54ms
# Memory 16.44mb

class Solution:
    def myAtoi(self, str: str) -> int:
        value, flag, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            char = str[pos]
            if flag == 0:
                if char == " ":
                    flag = 0
                elif char == "+" or char == "-":
                    flag = 1
                    sign = 1 if char == "+" else -1
                elif char.isdigit():
                    flag = 2
                    value = value * 10 + int(char)
                else:
                    return 0
            elif flag == 1:
                if char.isdigit():
                    flag = 2
                    value = value * 10 + int(char)
                else:
                    return 0
            elif flag == 2:
                if char.isdigit():
                    state = 2
                    value = value * 10 + int(char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value