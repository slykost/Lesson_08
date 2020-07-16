# Представте себе книгу в книжном магазине. В этой книге хранятся записи о номере заказа,
# названии книги, количества и стоимости одной книги, как представленно ниже, в таблице

# +-------------+------------------------------------+----------+----------------+
# | Oder Number |     Book Title and Author          | Quantity | Price per Item |
# +-------------+------------------------------------+----------+----------------+
# |    34587    | Learning Python, Mark Lutz         |     4    |     40.95      |
# |    98762    | Programming Python, Mark Lutz      |     5    |     56.80      |
# |    77226    | Head First Python, Paul Burry      |     3    |     32.95      |
# |    88112    | Einfuhrung in Python3, Bernd Klein |     3    |     24.99      |
# +-------------+------------------------------------+----------+----------------+

# Напишите программу на Python, которая на вход получает список списков:
# [
#     [34587, 'Learning Python, Mark Lutz', 4, 40.95],
#     [98762, 'Programming Python, Mark Lutz', 5, 56.80],
#     [77226, 'Head First Python, Paul Burry', 3, 32.95],
#     [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
# ]

# и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения цены
# на товар и количества. Стоимость товара должна быть увеличена на $10, если стоимость заказа
# меньше $100. Программа должна использовать lambda и map.


lst = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Burry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

result = list(map(lambda x: (int(lst[x][0]), round(lst[x][3] + 10, 2)) if lst[x][2] * lst[x][3] < 100
        else (int(lst[x][0]), lst[x][3]), range(len(lst))))
print(result)
