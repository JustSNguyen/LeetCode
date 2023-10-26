class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:
            number_of_backspaces = 0
            while number_of_backspaces > 0 or s[i] == "#":
                if s[i] == "#":
                    number_of_backspaces += 1
                else:
                    number_of_backspaces -= 1
                i -= 1

                if i < 0:
                    break

            number_of_backspaces = 0
            while number_of_backspaces > 0 or t[j] == "#":
                if t[j] == "#":
                    number_of_backspaces += 1
                else:
                    number_of_backspaces -= 1
                j -= 1

                if j < 0:
                    break

            s_char = ""
            if i >= 0:
                s_char = s[i]

            t_char = ""
            if j >= 0:
                t_char = t[j]

            if s_char != t_char:
                return False

            i -= 1
            j -= 1

        return True


if __name__ == '__main__':
    sol = Solution()
    s = "ab##"
    t = "c#d#"
    result = sol.backspaceCompare(s, t)
    print(result)
