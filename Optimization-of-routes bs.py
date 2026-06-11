class Solution:
    def optimalUtilization(self, maxTravelDist, forwardRouteList, returnRouteList):
        returnRouteList.sort(key=lambda x: x[1])
        def bs(target):
            low, high = 0, len(returnRouteList) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if returnRouteList[mid][1] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        res = []
        max_sum = -1

        for f_id, f_dist in forwardRouteList:
            target=maxTravelDist - f_dist
            idx = bs(target)

            if idx < 0:
                continue

            total = f_dist + returnRouteList[idx][1]

            if total > max_sum:
                max_sum = total
                res = [[f_id, returnRouteList[idx][0]]]

            elif total == max_sum:
                res.append([f_id, returnRouteList[idx][0]])

        return res
