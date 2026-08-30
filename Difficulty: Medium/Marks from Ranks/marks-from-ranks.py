from bisect import bisect_left

class Solution:

    def getMarks(self, l, r, rank):
        cumulative = []
        total = 0

        for i in range(len(l)):
            total += r[i] - l[i] + 1
            cumulative.append(total)

        ans = []

        for k in rank:

            # Find first cumulative count >= k
            i = bisect_left(cumulative, k)

            # Marks before this interval
            previous = 0 if i == 0 else cumulative[i - 1]

            # Position inside current interval
            position = k - previous

            # Actual mark
            mark = l[i] + position - 1

            ans.append(mark)

        return ans