
# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError


class Category:

    categories: list

    def __init__(self):
        self.categories=[]

    def add(self,title:str):
        title=title.lower()
        if title in self.categories:
            print("такая категория есть")
            raise ValueError
        else:
            print(" такой категории нет, добавим")
            self.categories.append(title)
            return self.categories.index(title)
    def get(self,indexx):

        if len(self.categories) > indexx:
            return self.categories[indexx]
        else:
            raise IndexError


    def delete(self,indexx):
        if len(self.categories) > indexx:
            del self.categories[indexx]
        else:
            pass

    def update(self,indexx,title:str):
        title = title.lower()
        if title in self.categories:
            raise ValueError
        else:
            if len(self.categories) > indexx:
                self.categories[indexx]=title
            else:
                self.categories.append(title)

    def __str__(self):
        return self.categories.__str__()

books=Category()

print(books.add("horror"))
print(books.add("comedy"))
print(books.add("sci-fi"))

print(books)

print(books.update(9,"sci-fi"))
print(books)
