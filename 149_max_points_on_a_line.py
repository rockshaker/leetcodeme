# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        if l == 0 or l == 1:
            return l

        max_points = 0
        for i in range(l):
            same_point_num = 0
            current_max_points = 1
            slope_dict = {}

            for j in range(i+1, l):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same_point_num += 1
                    current_max_points += 1
                else:
                    if points[j].x != points[i].x:
                        slope = 1.0 * (points[j].y - points[i].y) / (points[j].x - points[i].x)
                        if slope in slope_dict.keys():
                            slope_dict[slope] += 1
                        else:
                            slope_dict.update({slope: 2})
                    else:
                        slope = float("Inf")
                        if slope in slope_dict.keys():
                            slope_dict[slope] += 1
                        else:
                            slope_dict.update({slope: 2})
                    if slope_dict[slope] + same_point_num > current_max_points:
                        current_max_points = slope_dict[slope] + same_point_num
            if current_max_points > max_points:
                max_points = current_max_points
        return max_points
