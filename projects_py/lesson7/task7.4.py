# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение  ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError

class Category:

    categories: list

    def __init__(self):
        self.categories=[]

    def add(self,title:dict):
        name=title.get('name')
        for book in self.categories:
            if book.get('name')==name:
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

    def update(self,indexx,title:dict):
        name = title.get('name')
        for book in self.categories:
            if book.get('name') == name:
                raise ValueError
        else:
            if len(self.categories) > indexx:
                self.categories[indexx]=title
            else:
                self.categories.append(title)

    def make_published(self, indexx):
        if len(self.categories) > indexx:
            self.categories[indexx]['is_published']=True
        else:
            raise IndexError
    def make_unpublished(self, indexx):
        if len(self.categories) > indexx:
            self.categories[indexx]['is_published']=False
        else:
            raise IndexError

    def __str__(self):
        return self.categories.__str__()

books=Category()

print(books.add({"name":"horror","is_published":False}))
print(books.add({"name":"comedy","is_published":False}))
print(books.add({"name":"detectiv","is_published":False}))

print(books)
#print(books.get(2))
#print(books.update(2,{"name":"sex","is_published":False}))
#print(books.delete(8))
print(books.make_published(1))
print(books)
print(books.make_unpublished(1))
print(books)