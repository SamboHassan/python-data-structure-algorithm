# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        """Create an entry with given name and score."""
        self._name = name
        self._score = score

    def get_name(self):
        """Return the name of the person for this entry."""
        return self._name

    def get_score(self):
        """Return the score of this entry."""
        return self._score

    def __str__(self):
        """Return string representation of the entry."""
        return "({0}, {1})".format(self._name, self._score)  # e.g., '(Bob, 98)'


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self._board = [None] * capacity  # reserve space for future scores
        self._n = 0  # number of actual entries

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return "\n".join(str(self._board[j]) for j in range(self._n))  # List of tuple

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        # self._n is the current number of entries on the
        # board (or the position we are managing up to).
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):  # no score drops from list
                self._n += 1  # so overall current/actual number entries increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j - 1].get_score() < score:
                self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
                j -= 1  # and decrement j
            self._board[j] = entry  # when done, add new entry


if __name__ == "__main__":
    board = Scoreboard(5)
    for e in (
        ("Rob", 750),
        ("Mike", 1105),
        ("Rose", 590),
        ("Jill", 740),
        ("Jack", 510),
        ("Anna", 660),
        ("Paul", 720),
        ("Bob", 400),
    ):
        ge = GameEntry(e[0], e[1])
        board.add(ge)
        print("After considering {0}, scoreboard is:".format(ge))
        print(board)
        print()


class GameEntry:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return f"({self._name}, {self._score})"


class Scoreboard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity
        self._n = 0

    def __getitem__(self, k):
        return self._board[k]

    # In Python, the __str__ method is a special method that returns
    # a string representation of an object.

    def __str__(self):
        # This part is a generator expression, which generates a sequence of
        # strings to be joined.
        return "\n".join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

        j = self._n - 1
        while j > 0 and self._board[j - 1].get_score() < score:
            # shifts each element to the right by one position
            self._board[j] = self._board[j - 1]
            j -= 1
        self._board[j] = entry


games = [
    ("Rob", 750),
    ("Mike", 1105),
    ("Rose", 590),
    ("Jill", 740),
    ("Jack", 510),
    ("Anna", 660),
    ("Paul", 720),
    ("Bob", 400),
]

if __name__ == "__main__":
    board = Scoreboard(5)
    for e in games:
        ge = GameEntry(e[0], e[1])
        board.add(ge)
        print("After considering {0}, scoreboard is:".format(ge))
        print(board)
        print()
