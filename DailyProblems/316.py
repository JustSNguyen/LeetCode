from functools import lru_cache


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        all_possible_characters = [chr(ascii_value) for ascii_value in range(ord('a'), ord('z') + 1)]
        chosen_characters = []

        for character in all_possible_characters:
            position = -1
            cur_chosen_characters_index = len(chosen_characters) - 1
            end_search_index = len(s)

            while cur_chosen_characters_index >= 0 and position == -1:
                chosen_character_info = chosen_characters[cur_chosen_characters_index]
                start_search_index = chosen_character_info[1]
                for i in range(start_search_index, end_search_index):
                    if s[i] == character:
                        position = i
                        break

                end_search_index = start_search_index
                cur_chosen_characters_index -= 1

            if position == -1:
                for i in range(end_search_index):
                    if s[i] == character:
                        position = i
                        break

            if position != -1:
                chosen_characters.append((character, position))

        print(chosen_characters)
        chosen_positions = {tuple[1]: 1 for tuple in chosen_characters}
        result = []
        for i in range(len(s)):
            if i in chosen_positions:
                result.append(s[i])

        return ''.join(result)

if __name__ == '__main__':
    sol = Solution()
    test = "cbacdcbc"
    result = sol.removeDuplicateLetters(test)
    print(result)
