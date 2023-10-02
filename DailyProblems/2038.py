class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_number_of_options = 0
        bob_number_of_options = 0

        number_of_consecutive_colors = 0
        previous_color = ""
        for color in colors:
            if color == previous_color:
                number_of_consecutive_colors += 1
            else:
                if number_of_consecutive_colors >= 3:
                    if previous_color == "A":
                        alice_number_of_options += number_of_consecutive_colors - 2
                    else:
                        bob_number_of_options += number_of_consecutive_colors - 2

                number_of_consecutive_colors = 1

            previous_color = color

        if number_of_consecutive_colors >= 3:
            if previous_color == "A":
                alice_number_of_options += number_of_consecutive_colors - 2
            else:
                bob_number_of_options += number_of_consecutive_colors - 2

        print(alice_number_of_options, bob_number_of_options)

        if alice_number_of_options > bob_number_of_options:
            return True

        return False


if __name__ == '__main__':
    sol = Solution()
    colors = "AAABABB"
    print(sol.winnerOfGame(colors))
