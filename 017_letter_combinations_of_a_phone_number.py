class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return self.letterCombinationsImp(digits, digit_to_letter)

    def letterCombinationsImp(self, digits, digit_to_letter):
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [ch for ch in digit_to_letter[digits[0]]]
        res = []
        rest_combs = self.letterCombinationsImp(digits[1:], digit_to_letter)
        num = digits[0]
        for comb in rest_combs:
            for letter in digit_to_letter[num]:
                res.append(letter + comb)
        return res
