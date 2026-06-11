class Solution:
    def optimalUtilization(self, maxTravelDist, forwardRouteList, returnRouteList):

        res = []
        max_sum = float('-inf')

        for f_id, f_dist in forwardRouteList:
            for r_id, r_dist in returnRouteList:

                total = f_dist + r_dist

                if total > maxTravelDist:
                    continue

                if total > max_sum:
                    max_sum = total
                    res = [[f_id, r_id]]

                elif total == max_sum:
                    res.append([f_id, r_id])

        return res

  
