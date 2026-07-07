class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 500, 100, 50, 10, 5, 1]
        syms = ["M", "D", "C", "L", "X","V", "I"]

        sol = ""
        for i in range(len(val)):
            count = num // val[i]
            if (count <= 3) and (val[i] % 10 == 0):
                sol += syms[i] * count
                num -= val[i] * count
                print({"count": count, "num": num, "sol": sol})

            elif count == 9:
                print(" substracting", syms[i-2], " and ", syms[i], " for 2", val[i])
                sol += syms[i] + syms[i-2]
                num -= val[i] * 9
                print({"count-2": count, "num": num, "sol": sol})

            elif count == 4:
                print(" substracting", syms[i-1], " and ", syms[i], " for ", val[i])
                sol += syms[i] + syms[i-1]
                num -= val[i] * 4
                print({"count-2": count, "num": num, "sol": sol})
        return sol


solution = Solution()
print(solution.intToRoman(3749))



