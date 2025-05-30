def add(self, entry):
    """Consider adding entry to high scores."""
    score = entry.get_score()

    # Does new entry qualify as a high score?
    # answer is yes if board not full or score is higher than last entry
    # Last entry is at the top
    good = self._n < len(self._board) or score > self._board[-1].get_score()

    if good:
        if self._n < len(self._board):  # no score drops from list
            self._n += 1  # so overall number increases

        # shift lower scores rightward to make room for new entry
        j = self._n - 1
        while j > 0 and self._board[j - 1].get_score() < score:
            self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
            j -= 1  # and decrement j
        self._board[j] = entry  # when done, add new entry

        # class py_solution:


#     def int_to_Roman(self, num):
#         val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#         syb = ["M", "CM", "D", "CD" "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

#         roman_num = ""

#         i = 0

#         while num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# print(py_solution().int_to_Roman(4000))
