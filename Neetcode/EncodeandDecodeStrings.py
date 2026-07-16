class Solution:

    def encode(self, strs: [str]) -> str:
        sol = ""
        for s in strs:
            sol += str(s)+";"
        return sol

    def decode(self, s: str) -> [str]:
        sol = []
        temp = ""
        for char in s:
            if char != ";":
                temp += char
            else:
                sol.append(temp)
                temp = ""
        return sol


encoded = Solution().encode(["Hello", "World"])
print (encoded)
decoded = Solution().decode(encoded)
print(decoded)