class Solution(object):
    def atoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sti_dicts = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                     '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        str = str.strip()
        INT_MAX, INT_MIN = 2147483647, -2147483648

        result = 0
        neg_flag = 0
        for k, ch in enumerate(str):
            if not ch:
                continue

            if ch not in sti_dicts.keys():
                if k == 0:
                    if ch == '-':
                        neg_flag = 1
                        continue
                    if ch == '+':
                        continue
                break

            result = result*10 + sti_dicts[ch]

        if neg_flag:
            result = -result

            if result < INT_MIN:
                result = INT_MIN
        if result > INT_MAX:
            result = INT_MAX

        return result


class Solution2:
    # @return an integer
    def atoi(self, str):
        s = str.strip()

        if len(s) == 0:
            return 0

        INT_MAX, INT_MIN = 2147483647, -2147483648

        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        res = 0
        while i < len(s):
            digit = ord(s[i]) - ord('0')
            if 0 <= digit <= 9:
                res = res * 10 + digit
                if res > INT_MAX:
                    return INT_MIN if sign == -1 else INT_MAX
            else:
                break

            i += 1

        return sign * res

s = Solution()
print s.atoi("  -0012a42")
