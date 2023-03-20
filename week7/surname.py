def taken_name(surname_husband, surname_wife):
    if surname_husband in surname_wife:
        return True
    return False


print(taken_name("Petrov", "Ivanova-Petrova"))
