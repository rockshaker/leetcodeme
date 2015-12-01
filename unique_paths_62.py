from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.count_paths((0, n-1), (m-1, 0))

    @memo
    def count_paths(self, start, end):
        x_distance = end[0] - start[0]
        y_distance = abs(end[1] - start[1])
        if x_distance == 0 and y_distance == 0:
            return 1
        if x_distance == 1 and y_distance == 0:
            return 1
        if x_distance == 0 and y_distance == 1:
            return 1

        return self.count_paths((start[0], start[1]-1), end) + self.count_paths((start[0]+1, start[1]), end)

class Solution2(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = {}
        for i in range(m):
            paths[i, 0] = 1

        for j in range(n):
            paths[0, j] = 1

        for i in range(1, m):
            for j in range(1, n):
                paths[i, j] = paths[i-1, j] + paths[i, j-1]

        return paths[m-1, n-1]


s = Solution2()
print s.uniquePaths(1, 10)
