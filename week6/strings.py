def reverse_str(string):
    return string[::-1]


print(reverse_str("Hello"), "\n")


def join(delimiter, items):
    new_string = ""
    for i in items:
        new_string += i + delimiter
    return new_string


print(join("\n", ["Hello", "there"]))


def startswith(search, string):
    counter = 0
    new_string = string[:len(search)]
    return search == new_string


print(startswith("Py", "Python"))


def endswith(search, string):
    new_string = string[:(len(string) - len(search)) - 1:-1]
    return search == new_string[::-1]


print(endswith("on", "Python"))


def trim(string):
    counter = 0
    result = ""
    for i in string:
        if i == " ":
            counter += 1
        else:
            break
    result = string[counter:]
    new_string = ""
    flag = False
    for i in result[::-1]:
        if i != " ":
            flag = True
            new_string += i
        else:
            if flag:
                new_string += " "

    return new_string[::-1]


print(trim("   python is amazing      "))
