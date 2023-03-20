strings = ["python", "gogo", "perl", "java", "haskell", "ruby0nRails"]

def string_matrix(number, string):
    the_matrix = []
    for i in string:
        row = join(" | ", i)
        row = "| " + row
        the_matrix +=[row]
    letter_counter = 0
    for letter in the_matrix:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter_counter += 1
    if letter_counter < number:


def join(delimiter, items):
    new_string = ""
    for i in items:
        new_string += i + delimiter
    return new_string
