"""Бюджета на Иванчо.
Иванчо събира пари за книги по програмиране. Има и списък с книгите, които иска да вземе, обаче не е сигурен в две неща:

Колко най-много книги ще може да вземе със своя бюджет
Колко кредит ще трябва да изтегли, за да може да вземе останалите книги, извън бюджета му.
Във файла budget.py, напишете функцията on_budget(books, budget), където:

books е списък от цели числа - цените на книгите от списъка на Иванчо. В списъка може да има безплатни книги, отбелязани с цена 0.
budget е цяло число - бюджета на Иванчо.
Функцията трябва да върне речник, който има два ключа:

"books_on_budget" - като стойност на този ключ трябва да стои максималната бройка на книги, които Иванчо може да си купи с дадения budget
"loan" - стойността на този ключ са парите, които Иванчо трябва да вземе, за да може да си купи всички останали книги от списъка,
които са извън неговия бюджет, след като е взем максималната бройка преди това.

Например, ако имаме следния списък с цени и бюджет:

books = [0, 10, 100, 5, 3, 8, 25]
и budget = 35
То Иванчо ще може да вземе общо 5 книги за общо 26 лева, след което ще му останат 9 лева.

След това Иванчо трябва да изтегли заем от 100 + 25 - 9 = 116 лева.

Крайният резултат е:

{
  "books_on_budget": 5,
  "loan": 116
}
Примерни тестове
За:

books = [0, 0, 0]
budget = 10`
Имаме

{
  "books_on_budget": 3,
  "loan": 0
}
За:

books = [50, 60, 100]
budget = 20`
Имаме

{
  "books_on_budget": 0,
  "loan": 190
}
Подсказване
Алгоритъмът е следния:

Подреждате цената на книгите от най-ниската към най-високата. Това може да стане с вградената в Python функция sorted
Взимате поредната най-евтина книга, докато имате бюджет.
Накрая правите сметката за колко пари ще ви трябват допълнително

"""


def on_budget(books, budget):
    books_on_budget = []
    result = {"books_on_budget": "",
              "loan": ""}
    for book in sorted(books):
        books_on_budget += [book]
        print(sorted(books), 'This is sorted books list')
        print(books_on_budget, 'This is the list of books on budget')
        print(sum(books_on_budget), 'This is sum of books on budget')
        books.remove(book)
        if sum(books_on_budget) > budget:
            books.append(book)
            books_on_budget.remove(book)
    result["books_on_budget"] = len(books_on_budget)
    result["loan"] = sum(books) - (budget - sum(books_on_budget))
    print(books)
    if result["loan"] < 0:
        result["loan"] = 0
    return result


books = [0, 10, 100, 5, 3, 8, 25]
budget = 35


print(on_budget(books, budget))