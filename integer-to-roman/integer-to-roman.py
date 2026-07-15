class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 500, 100, 50, 10, 5, 1]
        syms = ["M", "D", "C", "L", "X","V","I"]

        sol = ""
        for i in range(len(val)):
            count = num // val[i]

            if val[i] != val[-1]:
                next_count = (num - count * val[i]) // val[i+1]

            if count == 0:
                continue

            if (count <= 3) and (i % 2 == 0):
                sol += syms[i] * count
                num -= val[i] * count

            elif (count == 1) and (next_count <= 3):
                sol += syms[i]
                num -= val[i]

            elif (count == 1) and (next_count >= 4):

                sol += syms[i+1] + syms[i-1]
                if num < 10:
                    num -= 9
                else:
                    num -= val[i+1] * 9


            elif (count == 4) or (num == 4):
                sol += syms[i] + syms[i-1]
                if num < 10:
                    num -= 4
                else:
                    num -= val[i] * 4

        return sol


solution = Solution()
print(solution.intToRoman(3794))



