class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            if t == 1:
                return False

            return True

        min_to_reach_same_fx = abs(fx - sx)
        if min_to_reach_same_fx > t:
            return False

        pos_new_y = sy + min_to_reach_same_fx
        neg_new_y = sy - min_to_reach_same_fx

        if neg_new_y <= fy <= pos_new_y:
            return True

        dist1 = abs(pos_new_y - fy)
        dist2 = abs(neg_new_y - fy)
        min_dist = min(dist1, dist2)

        t_left = t - min_to_reach_same_fx

        return t_left >= min_dist
