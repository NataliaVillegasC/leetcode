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

            if (count <= 3) and (val[i] % 10 == 0):
                print("num is power of 10", num)
                sol += syms[i] * count
                num -= val[i] * count
                print("num after power of 10", num, "sol is", sol)
                
            elif (count == 9) or (num == 9):
                print("num starts with 9", num)
                sol += syms[i] + syms[i-2]
                if num < 10:
                    num -= 9
                else:
                    num -= val[i] * 9
                print("num after start with 9", num, "sol is", sol)

            elif (count == 4) or (num == 4):
                print("num starts with 4", num)
                sol += syms[i] + syms[i-1]
                print(val[i] * 4)
                if num < 10:
                    num -= 4
                else:
                    num -= val[i] * 4
                print("num after start with 4", num, "sol is", sol)

            elif count == 1:
                print("num is", num)
                sol += syms[i]
                num -= val[i]
                print("num after 1", num, "sol is", sol)

        return sol


solution = Solution()
print(solution.intToRoman(3794))



