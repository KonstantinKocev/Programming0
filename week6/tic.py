def board_to_string(board):
    result = []
    for i in board:
        row = join(" | ", i)
        row = "| " + row
        result += [row]

    return join("\n", result)


def join(delimiter, items):
    new_string = ""
    for i in items:
        new_string += i + delimiter
    return new_string


board = [["X", "O", "#"],
         ["X", "X", "X"],
         ["#", "#", "#"]]

print(board_to_string(board))
