def head(list):
    return list[0]


print(head([1, 2, 3, 4]))


def last(list):
    return list[-1]


print(last([1, 2, 3, 4]))


def tail(list):
    new_list = []
    for item in list:
        if item != list[0]:
            new_list += [item]

    return new_list


print(tail([1, 2, 3, 4]))


def equal_list(list1, list2):
    if list1 == list2:
        return True


print(equal_list([1, 2, 3, 4], [1, 2, 3, 4]))


def count_item(digit, list):
    counter = 0
    for item in list:
        if item == digit:
            counter += 1
    return counter


print(count_item(5, [1, 2, 3, 4, 5]))


def take(digit, list):
    new_list = []
    for item in range(0, min(digit, len(list))):
        new_list += [list[item]]

    return new_list


print(take(2, [1, 2, 3, 4, 5]))


def drop(digit, list):
    for item in list:
        if item == digit:
            list.remove(item)
    return list


print(drop(1, [1, 2, 3]))


def reversed_list(list):
    list.reverse()
    return list


print(reversed_list([1, 2, 3, 4]))
