class Person:
    def __init__(self, name: str, cpf: str, address: str, sex: str):
        self.name = name
        self.cpf = cpf
        self.address = address
        self.sex = sex

class Category:
    def __init__(self, category: str):
        self.category = category

class Product(Category):
    def __init__(self, name: str, price: float, sales: int, category: str):
        super().__init__(category)
        self.name = name
        self.price = price
        self.sales = sales

class Provider(Category):
    def __init__(self, company: str, mensality: float, category: str):
        super().__init__(category)
        self.company = company
        self.mensality = mensality

class Customer(Person):
    def __init__(self, nickname: str, name: str, cpf: str, address: str, sex: str):
        super().__init__(name, cpf, address, sex)
        self.nickname = nickname

class Employee(Person):
    def __init__(self, nickname: str, birthdate: str, marital_state: str, name: str, cpf: str, address: str, sex: str):
        super().__init__(name, cpf, address, sex)
        self.nickname = nickname
        self.birthdate = birthdate
        self.marital_state = marital_state

class DailySales:
    def __init__(self, date: str, sales: int):
        self.date = date
        self.sales = sales

class Sales(Customer):
    def __init__(self, nickname: str, purchases: int, product: str, amount: int):
        super().__init__(nickname, None, None, None, None)
        self.purchases = purchases
        self.product = product
        self.amount = amount

class Stock:
    def __init__(self, product: str, amount: int):
        self.product = product
        self.amount = amount