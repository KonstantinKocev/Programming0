"""Задача 6 - Is it friday yet?
Ще направим нещо подобно на това - http://isitfridayyet.org/

В файла friday.py имате следния код:

import time

today = time.strftime("%A")

print(today)
Имате следната задача:

Разберете какво прави този код. Пуснете файла и експериментирайте!
Допишете код към файла, така че ако е петък, да изпише It is friday!
Ако не е петък - да напише It is not friday ;( Today is ......, като на мястото на ...... да пише днешния ден.
Примерно използване:

It is not friday ;( Today is Monday.

"""

import time

today = time.strftime('%A')

print(today)


if today