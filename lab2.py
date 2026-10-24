import csv
import random
import xml.etree.ElementTree as ET


with open("books.csv", encoding="cp1251") as f:
    reader = csv.DictReader(f, delimiter=";")
    books = list(reader)

def get_year(book):
    date_with_time = book["Дата поступления"]      
    date = date_with_time.split(" ")[0]           
    year = date.split(".")[2]           
    return int(year)

# задание 1 количество записей с длиной названия больше 30 
counter_30 = 0
for book in books:
    if len(book["Название"]) > 30:
        counter_30 += 1
print("Количество книг с названием длиннее 30 символов:", counter_30)


# задание 2 функция для поиска книг по автору и при этом год с 2018 
def search_by_author(author):
    found_books = []
    for book in books:
        if book["Автор"] == author and get_year(book) >= 2018:
            found_books.append(book)
    return found_books

name = input("Введите автора: ")
found = search_by_author(name)
if len(found) == 0:
    print("Ничего не найдено")
else:
    for book in found:
        print(book["Автор"] + ". " + book["Название"] + " - " + str(get_year(book)))


# задание 3 библиографические ссылки
def bibliography(books, n):
    # просто в файле есть книги без автора, и чтобы в итоговом текстовом файле не было такого:2. . Литературная газета №01-02 (6445) 2014 - 2014, отсею книги без автора
    books_with_author = []
    for book in books:
        if book["Автор"] != "":
            books_with_author.append(book)

    chosen_books = random.sample(books_with_author, n)   
    for book in chosen_books:
        yield book["Автор"] + ". " + book["Название"] + " - " + str(get_year(book))


with open("bibliography.txt", "w", encoding="utf-8") as out:
    books20 = bibliography(books, 20)
    # print(list(books))
    number = 1
    for line in books20:
        out.write(str(number) + ". " + line + "\n")
        number += 1


# # допзадание 1 уникальные теги(без повторений) из жанров книг
tags = set()
for book in books:
    for tag in book["Жанр книги"].split("#"):
        tag = tag.strip()
        if tag != "":
            tags.add(tag)
for tag in sorted(tags):
    print(tag)

# допазадание 2 20 самых популярных книг
issued = {}
for book in books:
    title = book["Название"]
    count = int(book["Кол-во выдач"])
    if title in issued: #если книга уже есть в словаре, то + кол-во выдач
        issued[title] += count
    else:
        issued[title] = count

top = sorted(issued.items(), key=lambda x: x[1], reverse=True)
print("20 самых популярных книг:")
for i in range(20):
    print(i + 1, top[i][0], "-", top[i][1])

# задание с currency.xml словарь name - charcode
tree = ET.parse("currency.xml")
root = tree.getroot()
currency = {}
for valute in root.findall("Valute"):
    name = valute.find("Name").text
    char_code = valute.find("CharCode").text
    currency[name] = char_code

for name, char_code in currency.items():
    print(name, "-", char_code)
