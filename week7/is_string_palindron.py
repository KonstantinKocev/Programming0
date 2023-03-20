a = "Az obi4am ma4 i boza"
a = a.lower()


def is_string_palindrom(string):
    new_string = ""
    all_letters = "abcdefghijklmnopqrstuvwxyz1234567890"
    for letter in string:
        if letter in all_letters:
            new_string += letter
    rev_string = new_string[::-1]
    print(new_string, "|", rev_string)
    if rev_string == new_string:
        return True
    return False


print(is_string_palindrom(a))
