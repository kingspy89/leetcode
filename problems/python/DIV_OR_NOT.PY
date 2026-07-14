class Solution:
    def differenceOfSums(self, n, m):
        div_sum = 0
        not_div_sum = 0

        for i in range(1, n + 1):
            if i % m == 0:
                div_sum += i
            else:
                not_div_sum += i

        return not_div_sum - div_sum