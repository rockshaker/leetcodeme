class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = '+-*/'
        stc = []
        for s in tokens:
            if s in operators:
                num2 = int(stc.pop())
                num1 = int(stc.pop())
                if s == '+':
                    num1 += num2
                elif s == '-':
                    num1 -= num2
                elif s == '*':
                    num1 *= num2
                else:
                    if num1 / num2 < 0 and num1 % num2 != 0:
                        num1 = num1 / num2 + 1
                    else:
                        num1 /= num2

                stc.append(str(num1))
            else:
                stc.append(s)
        return int(stc.pop())
