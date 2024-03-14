class Solution:
    def encode(self, strs):
        string_as_list = []
        for string in strs:
            string_as_list.append(f"{len(string)}/")
            string_as_list.append(string)

        return "".join(string_as_list)

    def decode(self, string):
        strings = []
        i = 0
        while i < len(string):
            string_length = 0
            while string[i] != "/":
                digit = int(string[i])
                string_length = string_length * 10 + digit
                i += 1

            string_start = i + 1
            string_end = i + string_length + 1
            strings.append(string[string_start: string_end])

            i = string_end

        return strings

if __name__ == '__main__':
    test1 = ["///", "we", "say/", ":", "yes"]
    sol = Solution()
    result = sol.encode(test1)
    result = sol.decode(result)
    print(result)