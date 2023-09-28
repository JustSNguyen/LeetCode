class Solution:
    def decodeAtIndex(self, S, K):
        def is_digit(char: str) -> bool:
            return ord("1") <= ord(char) <= ord("9")

        def is_alphabet(char: str) -> bool:
            return not is_digit(char)

        cur_string_length = 0
        end_index = -1
        for char in S:
            end_index += 1
            if is_digit(char):
                cur_string_length = cur_string_length * int(char)
            else:
                cur_string_length = cur_string_length + 1

            if cur_string_length >= K:
                break

        for i in range(end_index, -1, -1):
            char = S[i]
            if is_digit(char):
                cur_string_length //= int(char)
                K %= cur_string_length
            elif is_alphabet(char):
                if K == 0 or K == cur_string_length: return char
                cur_string_length -= 1








