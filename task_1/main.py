#Gleb Zhukovskiy
#1 var

num = 1
print ("start code ...")
books  = [
    {"title": "Война и мир", "author":"Лев Толстой","year": "1869"},
    {"title": "Дом в котором", "author":"Мариам Петросян","year": "2009"},
    {"title": "451 градус по Фаренгейту", "author":"Рэй Бредбери","year": "1953"},
    {"title": "1984", "author":"Джордж Оруэлл","year": "1949"},
    {"title": "Мастер и Маргарита", "author":"Михаил Булгаков","year": "1967"}
]

for i in books:
    print("-" * 25,"Книга", num, "-" * 25)
    print(f"Название: {i["title"]}, Автор: {i["author"]}")
    print("-" * 25, i["year"], "-" * 25, "\n")
    num += 1
    
print ("end code ...")