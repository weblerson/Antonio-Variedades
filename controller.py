from model import *
from DAO import *
import datetime

class CategoryController:
    @classmethod
    def read(cls):
        categories_list = CategoryDAO.read_archive()

        return categories_list

    @classmethod
    def register(cls, new_category):
        categories_list = CategoryDAO.read_archive()

        if new_category in categories_list:
            return f"A categoria {new_category} já existe. Não é possível cadastrar."

        try:
            CategoryDAO.register(Category(new_category))

            return True

        except:
            return False

    @classmethod
    def change(cls, old_category, new_category):
        categories_list = CategoryDAO.read_archive()

        if old_category not in categories_list:
            return f"A categoria {old_category} não existe. Impossível fazer a alteração."
        
        try:
            CategoryDAO.change(Category(old_category), new_category)
                
            return True
        except:
            return False

    @classmethod
    def remove(cls, category):
        categories_list = CategoryDAO.read_archive()

        if category not in categories_list:
            return f"A categoria {category} não existe. Impossível fazer a remoção."
        
        try:
            CategoryDAO.remove(Category(category))
                
            return True
        except:
            return False
            
class ProductController:
    @classmethod
    def read(cls, category):
        product_list = ProductDAO.read_archive(Category(category))

        return product_list

    @classmethod
    def register(cls, category, name, price):
        category_list = CategoryController.read()

        if category not in category_list:
            return "Impossível cadastrar um produto numa categoria inexistente."

        product_list = [product for product in ProductController.read(category).keys()]

        if name in product_list:
            return f"O produto {name} já estava cadastrado cadastrado."

        ProductDAO.register(Product(name, price, 0, category))

        try:
            ProductDAO.register(Product(name, price, 0, category))

            return True
        
        except:
            return False

    @classmethod
    def change(cls, category, name, price, new_product):
        category_list = CategoryController.read()

        if category not in category_list:
            return "Impossível fazer uma mudança de um produto em uma categoria inexistente."

        product_list = [product for product in ProductController.read(category).keys()]

        if name not in product_list:
            return f"O produto {name} não existe. Não é possível fazer a alteração."

        try:
            ProductDAO.change(Product(name, price, 0, category), new_product)

            return True

        except:
            return False

    @classmethod
    def remove(cls, category, name):
        category_list = CategoryController.read()

        if category not in category_list:
            return f"A categoria {category} não existe. Impossível fazer a remoção do produto."

        product_list = [product for product in ProductController.read(category).keys()]

        if name not in product_list:
            return f"O produto {name} não existe. Impossível fazer a remoção."

        try:
            ProductDAO.remove(Product(name, None, None, category))

            return True
        
        except:
            return False

    @classmethod
    def add(cls, category, name, sales):
        category_list = CategoryController.read()

        if category not in category_list:
            return f'A categoria {category} não existe. Impossível manipular os dados.'

        product_list = [product for product in ProductController.read(category).keys()]

        if name not in product_list:
            return f"O produto {name} não existe. Impossível manipular os dados."

        try:
            ProductDAO.add(Product(name, None, sales, category))

            return True

        except:
            return False

class ProviderController:
    @classmethod
    def read(cls):
        provider_list = [provider for provider in ProviderDAO.read_archive().keys()]
        provider_info_list = [provider_info for provider_info in ProviderDAO.read_archive().values()]
        
        return provider_list, provider_info_list

    @classmethod
    def register(cls, company, mensality, category):
        provider_list, provider_info_list = ProviderController.read()
        category_list = CategoryController.read()

        if company in provider_list:
            return f"O fornecedor {company} já existe. Não é possível cadastrar."

        if category not in category_list:
            return f"A categoria {category} não existe. Não é possível cadastrar o fornecedor."

        try:
            ProviderDAO.register(Provider(company, mensality, category))

            return True

        except:
            return False

    @classmethod
    def change(cls, company, mensality, category, new_company):
        provider_list, provider_info_list = ProviderController.read()
        category_list = CategoryController.read()

        if company not in provider_list:
            return f"O fornecedor {company} não existe. Impossível alterar o fornecedor."

        if category not in category_list:
            return f"A categoria {category} não existe. Impossível fazer a alteração do fornecedor."

        try:
            ProviderDAO.change(Provider(company, mensality, category), new_company)

            return True

        except:
            return False

    @classmethod
    def remove(cls, company):
        provider_list, provider_info_list = ProviderController.read()

        if company not in provider_list:
            return f"O provedor {company} não existe. Impossível remover."

        try:
            ProviderDAO.remove(Provider(company, None, None))

            return True

        except:
            return False

class CustomerController:
    @classmethod
    def read(cls):
        customer_list = [customer for customer in CustomerDAO.read_archive().keys()]
        customer_info_list = [customer_info for customer_info in CustomerDAO.read_archive().values()]

        return customer_list, customer_info_list

    @classmethod
    def register(cls, nickname, name, cpf, address, sex):
        customer_list, customer_info_list = CustomerController.read()

        if nickname in customer_list:
            return f"O nickname {nickname} já existe. Impossível cadastrar."

        if len(cpf) < 11:
            return "O CPF digitado não possui 11 caracteres. Digite um CPF válido."

        index = 0
        for customer in customer_info_list:
            if customer['cpf'] == cpf:
                return f"O CPF dado já foi cadastrado no cliente {customer_list[index]}. Impossível cadastrar novo cliente."

            index += 1

        try:
            CustomerDAO.register(Customer(nickname, name, cpf, address, sex))

            return True

        except:
            return False

    @classmethod
    def change(cls, nickname, new_nickname):
        customer_list, customer_info_list = CustomerController.read()
        
        if nickname not in customer_list:
            return f"O cliente {nickname} não existe. Impossível fazer a alteração."

        try:
            CustomerDAO.change(Customer(nickname, None, None, None, None), new_nickname)

            return True

        except:
            return False

    @classmethod
    def remove(cls, nickname):
        customer_list, customer_info_list = CustomerController.read()

        if nickname not in customer_list:
            return f"O cliente {nickname} não existe. Impossível fazer a remoção."

        try:
            CustomerDAO.remove(Customer(nickname, None, None, None, None))

            return True

        except:
            return False

class EmployeeController:
    @classmethod
    def read(cls):
        employee_list = [employee for employee in EmployeeDAO.read_archive().keys()]
        employee_info_list = [employee_info for employee_info in EmployeeDAO.read_archive().values()]

        return employee_list, employee_info_list

    @classmethod
    def register(cls, nickname, birthdate, marital_state, name, cpf, address, sex):
        employee_list, employee_info_list = EmployeeController.read()

        if nickname in employee_list:
            return f"Um funcionário com nickname {nickname} já está cadastrado. Impossível cadastrar."

        if len(cpf) < 11:
            return "O CPF digitado não possui 11 caracteres."

        index = 0
        for employee in employee_info_list:
            if employee['cpf'] == cpf:
                return f"O CPF dado já foi cadastrado no funcionário {employee_list[index]}."

            index += 1

        try:
            EmployeeDAO.register(Employee(nickname, birthdate, marital_state, name, cpf, address, sex))

            return True

        except:
            return False

    @classmethod
    def change(cls, nickname, new_nickname):
        employee_list, employee_info_list = EmployeeController.read()

        if nickname not in employee_list:
            return f"O funcionário {nickname} não existe. Impossível fazer a alteração."

        try:
            EmployeeDAO.change(Employee(nickname, None, None, None, None, None, None), new_nickname)

            return True

        except:
            return False

    @classmethod
    def remove(cls, nickname):
        employee_list, employee_info_list = EmployeeController.read()

        if nickname not in employee_list:
            return f"O funcionário {nickname} não existe. Impossível fazer a remoção."

        try:
            EmployeeDAO.remove(Employee(nickname, None, None, None, None, None, None))

            return True

        except:
            return False

class DailySalesController:
    @classmethod
    def read(cls):
        daily_list = DailySalesDAO.read_archive()

        return daily_list

    @classmethod
    def add(cls, sales):
        date_list = [date for date in DailySalesController.read().keys()]
        current_date = str(datetime.date.today())

        edit = [c for c in current_date]
        today = f"{edit[8]}{edit[9]}/{edit[5]}{edit[6]}/{edit[0]}{edit[1]}{edit[2]}{edit[3]}"

        if today not in date_list:
            try:
                DailySalesDAO.register(DailySales(today, 0))

            except:
                return False

        try:
            DailySalesDAO.add(DailySales(today, sales))

            return True

        except:
            return False

class SalesController:
    @classmethod
    def read(cls):
        sales_list = SalesDAO.read_archive()

        return sales_list

    @classmethod
    def add(cls, nickname, purchases, product, amount):
        customer_list, customer_info_list = CustomerController.read()
        sales_list = SalesController.read()

        if nickname not in customer_list:
            return f"O cliente {nickname} não existe."

        if nickname in customer_list and nickname not in sales_list.keys():
            try:
                SalesDAO.register_customer(Sales(nickname, 0, None, None))
            
            except:
                return False

        try:
            if sales_list[nickname][product]:
                pass

        except:
            try:
                SalesDAO.register_product(Sales(nickname, None, product, 0))

            except:
                return False

        try:
            SalesDAO.add(Sales(nickname, purchases, product, amount))

            return True
        
        except:
            return False

class StockController:
    @classmethod
    def read(cls):
        stock_items = [item for item in StockDAO.read_archive().keys()]
        stock_info = [info for info in StockDAO.read_archive().values()]

        return stock_items, stock_info

    @classmethod
    def register(cls, product):
        stock_items, stock_info = StockController.read()

        if product in stock_items:
            return f"O produto {product} já existe no estoque. Impossível cadastrar novamente."

        try:
            StockDao.register(Stock(product, 0))

            return True

        except:
            return False

    @classmethod
    def add(cls, product, amount):
        stock_items, stock_info = StockController.read()

        if product not in stock_items:
            return f"O produto {product} não existe. Impossível adicionar."

        try:
            StockDAO.add(Stock(product, amount))

            return True

        except:
            return False

    @classmethod
    def remove(cls, product, amount):
        stock_items, stock_info = StockController.read()

        if product not in stock_items:
            return f"O produto {product} não existe. Impossível remover."

        try:
            StockDAO.remove(Stock(product, amount))

            return True

        except:
            return False