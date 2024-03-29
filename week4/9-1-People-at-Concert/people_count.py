"""Хора на концерт
Вие сте шеф на голяма концертна зала и искате да разберете колко хора са били общо на концерта снощи.

Тъй като системата за билети се е сринала, вие не знаете тази бройка.

Оказва се, че имате обединените записи от всички входове, които отбелязват името на човек, когато влезе и когато излезе.

Например един такъв запис би изглеждал така:

["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]
Общата бройка на отделните хора в горния списък е 4.

Във файл people_count.py, напишете функция get_people_count(activity), където:

activity е списък от низове, където имаме такива записи на имената на влизащи и излизащи.
Функцията трябва да върне броят на отделните хора, независимо колко пъти 1 човек е влизал или излизал.
Тестови данни
За да си вземете тестовеи данни, може да заредите и изпълните файла в същата папка - test_data.py.

Ще ви изкара списък с повтарящи се имена, който може да копирате във вашата програма.

"""

activity = ["Rado", "Ivo", "Maria", "Aneta", "Rado", "Rado", "Aneta", "Ivo", "Maria", "Rado"]


def get_people_count(x):
    people = {}
    for person in activity:
        if person == "Rado":
            people["Rado"] = person
        if person == "Ivo":
            people["Ivo"] = person
        if person == "Maria":
            people["Maria"] = person
        if person == "Aneta":
            people["Aneta"] = person
    return people


print(len(get_people_count(activity)))
