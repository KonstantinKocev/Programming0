def reverse_str(string):
    return string[::-1]


print(reverse_str("Hello"), "\n")


def join(delimiter, items):
    new_string = ""
    for i in items:
        new_string += i + delimiter
    return new_string


print(join("\n", ["Hello", "there"]))


def startwith(search, string):
    counter = 0
    for i in search:
        counter += 1
        if i == string[counter - 1]:
            return True


print(startwith("Py", "Python"))


def endswith(search, string):
    counter = -2
    for i in search:
        if i == string[counter]:
            counter += 1
            return True


print(endswith("on", "Python"))


def trim(string):
    for i in string:
        if i == " ":
            string.remove(i)
    return string


print(trim("  python is cool    "))
