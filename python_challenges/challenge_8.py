
def comp(n):
    temp =  [i for i in range(n)]
    return(temp)
print(comp(100))

square = lambda x : x*x
print(square(5))

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def read(self):
        print(f"You are reading '{self.title}' by {self.author}.")

book = Book('Leviathan Wakes','James S. A. Corey')
book.read()


