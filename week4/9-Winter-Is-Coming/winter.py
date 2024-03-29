"""Иде ли зимата?
Вие сте нов синоптик във Вестерос и сте нагърбени със задача, да кажете дали зимата иде.

Това, което получавате е списък от низове seasons, където всеки елемент ще бъде един от следните низове:

"winter"
"summer"
"spring"
Във Вестерос има следното правило - зимата иде само, ако са минали най-малко 5 сезона (лято или пролет), след последната зима.

Сезоните са подредени по хронологичен ред в seasons.

Например, ако имаме seasons = ["winter", "summer", "summer", "summer", "spring", "spring"], то зимата иде,
защото от последната зима са минали 5 други, различни сезона.

Във файл winter.py, напишете функция winter_is_coming(seasons), която отговаря с True или False на базата на сезоните, които идват.

"""

seasons = ["winter", "summer", "summer", "summer", "spring", "spring"]


def winter_is_coming(x):
    for season in seasons:
        if season == 'winter':
            return True
        else:
            return False


print(winter_is_coming(seasons))
