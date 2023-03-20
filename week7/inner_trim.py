def inner_trim(string):
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
            if not flag:
                pass
    return new_string[::-1]


print(inner_trim("  Python     Django   "))
