"""
Основы ООП, класс, объект, метод и атрибут
"""


class User:
    name: str

    def hello(self):
        print(f"Hello, {self.name}!")


john = User()
john.name = "John"

john.hello()
# hello_user(john.name)
