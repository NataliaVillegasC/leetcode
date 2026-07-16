class Solution:

    def encode(self, strs: [str]) -> str:
        sol = ""
        for s in strs:
            sol += str(len(s)) + ";" + s
        return sol

    def decode(self, s: str) -> [str]:
        sol = []
        temp = ""
        i = 0
        while i < len(s):
            if s[i] != ";":
                temp += s[i]
                i += 1
            else:
                length = int(temp)
                temp = ""
                i += 1 # Add the space of the ";"
                sol.append(s[i:i+length])
                i += length # Move the index to the next length of the string
        return sol


encoded = Solution().encode(["Hello", "World"])
print (encoded)
decoded = Solution().decode(encoded)
print(decoded)