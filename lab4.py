# Unicode for empty box, u"\u25A1"
# Unicode for black box, u"\u25A0"
# can double check if Unicodes are true
board = [
    [X, X, X, X, X],
    [X, X, X, X, X],
    [X, X, X, X, X],
    [X, X, X, X, X],
    [X, X, X, X, X]
]


def main():

    def index_to_row(row):
        row // 5

    def index_to_col(col):
        col // 5

    index_to_col(input('Please choose a column number (0 , -4): '))
    index_to_row(input('Please choose a row number (0, -4): '))
