"""Статус на курсистите
Радо е изпаднал в затруднение с курса по Ruby on Rails.

Системата му е дала списък с всички кандидатствали курсисти и техния статус - дали са си предали задачите или не.
Обаче Радо се е объркал и не може да разбере колко са финализираните кандидатури и колко не са.

Във файл status.py, напишете функция status_count(students), която:

Взима списък от речници students. Всеки речни в списъка има два ключа - "name" и "status",
като статусът може да е "finalized" или "not_finalized".

Връща речник, които има два ключа - "finalized" и "not_finalized".
Срещу всеки речник стои списък от имената на студентите, които имат дадения статус в students

Например, ако имаме следния списък:

students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized
            }]
То резултатът трябва да изглежда така:

{
  "finalized": ["Ivo", "Genadi"],
  "not_finalized": ["RadoRado"]
}

"""


def status_count(people):
    fin_names = []
    not_fin_names = []
    new_students = {"finalized": '',
                    "not_finalized": ''}
    for student in students:
        if student["status"] == "finalized":
            fin_names += [student["name"]]
        if student["status"] == "not_finalized":
            not_fin_names += [student["name"]]
    new_students["finalized"] = fin_names
    new_students["not_finalized"] = not_fin_names
    return new_students


students = [{
              "name": "RadoRado",
              "status": "not_finalized"
            }, {
              "name": "Ivo",
              "status": "finalized"
            }, {
              "name": "Genadi",
              "status": "finalized"
            }, {
                "name": "finalized",
                "status": "not_finalized"}]

print(status_count(students))
