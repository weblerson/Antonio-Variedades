from model import *
import json
import os

PRODUCTS = "data/products"
PROVIDERS = "data/providers.json"
CUSTOMERS = "data/customers.json"
EMPLOYEES = "data/employees.json"
DAILYSALES = "data/dailysales.json"
SALES = "data/sales.json"
STOCK = "data/stock.json"

class CategoryDAO:
    @classmethod
    def read_archive(cls):
        archives = os.listdir(PRODUCTS)
        categories_list = [archive.replace('.json', '') for archive in archives]

        return categories_list

    @classmethod
    def register(cls, category: Category):
        with open(os.path.join(PRODUCTS, f'{category.category}.json'), 'w') as categories:
            categories.write('{}')

    @classmethod
    def change(cls, category: Category, new_category):
        with open(os.path.join(PRODUCTS, f'{new_category}.json'), 'w') as new_category:
            new_category.write('{}')

        os.remove(os.path.join(PRODUCTS, f'{category.category}.json'))

    @classmethod
    def remove(cls, category: Category):
        os.remove(os.path.join(PRODUCTS, f'{category.category}.json'))

class ProductDAO:
    @classmethod
    def read_archive(cls, category: Category):
        with open(os.path.join(PRODUCTS, f'{category.category}.json'), 'r', encoding = 'utf8') as products:
            products_list = products.read()
            products_list = json.loads(products_list)

            return products_list

    @classmethod
    def register(cls, product: Product):
        products_list = ProductDAO.read_archive(Category(product.category))
        products_list.update({f"{product.name}": {
            "preço": product.price,
            "vendas": product.sales
        }})

        new_products_list = json.dumps(products_list, ensure_ascii = False)
            
        with open(os.path.join(PRODUCTS, f'{product.category}.json'), 'w') as products:
            products.write(new_products_list)

    @classmethod
    def change(cls, product: Product, new_product):
        products_list = ProductDAO.read_archive(Category(product.category))
        products_list[new_product] = products_list.pop(product.name)

        products_list.update({f"{new_product}": {
            "preço": product.price,
            "vendas": product.sales
        }})

        new_products_list = json.dumps(products_list, ensure_ascii = False)
            
        with open(os.path.join(PRODUCTS, f'{product.category}.json'), 'w') as products:
            products.write(new_products_list)

    @classmethod
    def remove(cls, product: Product):
        products_list = ProductDAO.read_archive(Category(product.category))
        products_list.pop(product.name)

        new_products_list = json.dumps(products_list, ensure_ascii = False)
            
        with open(os.path.join(PRODUCTS, f'{product.category}.json'), 'w') as products:
            products.write(new_products_list)

    @classmethod
    def add(cls, product: Product):
        products_list = ProductDAO.read_archive(Category(product.category))
        products_list[product.name]["vendas"] += product.sales

        new_products_list = json.dumps(products_list, ensure_ascii = False)

        with open(os.path.join(PRODUCTS, f'{product.category}.json'), 'w') as products:
            products.write(new_products_list)

class ProviderDAO:
    @classmethod
    def read_archive(cls):
        with open(PROVIDERS, 'r', encoding = 'utf8') as providers:
            providers_list = providers.read()
            providers_list = json.loads(providers_list)
            
            return providers_list

    @classmethod
    def register(cls, provider: Provider):
        providers_list = ProviderDAO.read_archive()
        providers_list.update({f"{provider.company}": {
            "categoria": f"{provider.category}",
            "mensalidade": provider.mensality}})

        new_providers_list = json.dumps(providers_list, ensure_ascii = False)

        with open(PROVIDERS, 'w') as providers:
            providers.write(new_providers_list)

    @classmethod
    def change(cls, provider: Provider, new_company):
        providers_list = ProviderDAO.read_archive()
        providers_list[new_company] = providers_list.pop(provider.company)
        
        providers_list.update({f"{new_company}": {
            "categoria": f"{provider.category}",
            "mensalidade": provider.mensality}})

        new_providers_list = json.dumps(providers_list, ensure_ascii = False)

        with open(PROVIDERS, 'w') as providers:
            providers.write(new_providers_list)

    @classmethod
    def remove(cls, provider: Provider):
        providers_list = ProviderDAO.read_archive()
        providers_list.pop(provider.company)
        new_providers_list = json.dumps(providers_list, ensure_ascii = False)

        with open(PROVIDERS, 'w') as providers:
            providers.write(new_providers_list)

class CustomerDAO:
    @classmethod
    def read_archive(cls):
        with open(CUSTOMERS, 'r', encoding = 'utf8') as customers:
            customers_list = customers.read()
            customers_list = json.loads(customers_list)

            return customers_list

    @classmethod
    def register(cls, customer: Customer):
        customers_list = CustomerDAO.read_archive()
        customers_list.update({f"{customer.nickname}": {
            "nome": f"{customer.name}",
            "sexo": f"{customer.sex}",
            "cpf": f"{customer.cpf}",
            "endereço": f"{customer.address}"
        }})

        new_customers_list = json.dumps(customers_list, ensure_ascii = False)

        with open(CUSTOMERS, 'w') as customers:
            customers.write(new_customers_list)

    @classmethod
    def change(cls, customer: Customer, new_nickname):
        customers_list = CustomerDAO.read_archive()
        customers_list[new_nickname] = customers_list.pop(customer.nickname)

        new_customers_list = json.dumps(customers_list, ensure_ascii = False)

        with open(CUSTOMERS, 'w') as customers:
            customers.write(new_customers_list)

    @classmethod
    def remove(cls, customer: Customer):
        customers_list = CustomerDAO.read_archive()
        customers_list.pop(customer.nickname)
        new_customers_list = json.dumps(customers_list, ensure_ascii = False)

        with open(CUSTOMERS, 'w') as customers:
            customers.write(new_customers_list)

class EmployeeDAO:
    @classmethod
    def read_archive(cls):
        with open(EMPLOYEES, 'r', encoding = 'utf8') as employees:
            employees_list = employees.read()
            employees_list = json.loads(employees_list)

            return employees_list

    @classmethod
    def register(cls, employee: Employee):
        employees_list = EmployeeDAO.read_archive()
        employees_list.update({f"{employee.nickname}": {
            "nome": f"{employee.name}",
            "sexo": f"{employee.sex}",
            "cpf": f"{employee.cpf}",
            "endereço": f"{employee.address}",
            "data de nascimento": f"{employee.birthdate}",
            "estado civil": f"{employee.marital_state}"
            }})

        new_employees_list = json.dumps(employees_list, ensure_ascii = False)

        with open(EMPLOYEES, 'w') as employees:
            employees.write(new_employees_list)

    @classmethod
    def change(cls, employee: Employee, new_nickname):
        employees_list = EmployeeDAO.read_archive()
        employees_list[new_nickname] = employees_list.pop(employee.nickname)

        new_employees_list = json.dumps(employees_list, ensure_ascii = False)

        with open(EMPLOYEES, 'w') as employees:
            employees.write(new_employees_list)

    @classmethod
    def remove(cls, employee: Employee):
        employees_list = EmployeeDAO.read_archive()
        employees_list.pop(employee.nickname)

        new_employees_list = json.dumps(employees_list, ensure_ascii = False)

        with open(EMPLOYEES, 'w') as employees:
            employees.write(new_employees_list)

class DailySalesDAO:
    @classmethod
    def read_archive(cls):
        with open(DAILYSALES, 'r', encoding = 'utf8') as daily:
            dailysales_list = daily.read()
            dailysales_list = json.loads(dailysales_list)

            return dailysales_list

    @classmethod
    def register(cls, daily: DailySales):
        daily_list = DailySalesDAO.read_archive()

        daily_list.update({f"{daily.date}": {
            "vendas": daily.sales
        }})

        new_daily_list = json.dumps(daily_list, ensure_ascii = False)

        with open(DAILYSALES, 'w') as daily:
            daily.write(new_daily_list)

    @classmethod
    def add(cls, daily: DailySales):
        daily_list = DailySalesDAO.read_archive()

        daily_list[daily.date]["vendas"] += daily.sales

        new_daily_list = json.dumps(daily_list, ensure_ascii = False)

        with open(DAILYSALES, 'w') as daily:
            daily.write(new_daily_list)

class SalesDAO:
    @classmethod
    def read_archive(cls):
        with open(SALES, 'r', encoding = 'utf8') as sales:
            sales_list = sales.read()
            sales_list = json.loads(sales_list)

            return sales_list

    @classmethod
    def register_customer(cls, sales: Sales):
        sales_list = SalesDAO.read_archive()

        sales_list.update({f"{sales.nickname}": {
            "compras": sales.purchases
        }})

        new_sales_list = json.dumps(sales_list, ensure_ascii = False)

        with open(SALES, 'w') as sales:
            sales.write(new_sales_list)

    @classmethod
    def register_product(cls, sales: Sales):
        sales_list = SalesDAO.read_archive()

        sales_list[sales.nickname].update({f"{sales.product}": sales.amount})

        new_sales_list = json.dumps(sales_list, ensure_ascii = False)

        with open(SALES, 'w') as sales:
            sales.write(new_sales_list)

    @classmethod
    def add(cls, sales: Sales):
        sales_list = SalesDAO.read_archive()

        sales_list[sales.nickname]["compras"] += sales.purchases
        sales_list[sales.nickname][sales.product] += sales.amount

        new_sales_list = json.dumps(sales_list, ensure_ascii = False)

        with open(SALES, 'w') as sales:
            sales.write(new_sales_list)

class StockDAO:
    @classmethod
    def read_archive(cls):
        with open(STOCK, 'r', encoding = 'utf8') as stock:
            stock = stock.read()
            stock = json.loads(stock)

            return stock

    @classmethod
    def register(cls, stock: Stock):
        stock = StockDAO.read_archive()

        stock.update({f"{stock.product}": {
            "quantidade": stock.amount
        }})

        new_stock = json.dumps(stock, ensure_ascii = False)

        with open(STOCK, 'w') as stock:
            stock.write(new_stock)

    @classmethod
    def add(cls, stock: Stock):
        stock = StockDAO.read_archive()

        stock[stock.product]["quantidade"] += stock.amount

        new_stock = json.dumps(stock, ensure_ascii = False)

        with open(STOCK, 'w') as stock:
            stock.write(new_stock)

    @classmethod
    def remove(cls, stock: Stock):
        stock = StockDAO.read_archive()

        stock[stock.product]["quantidade"] -= stock.amount

        new_stock = json.dumps(stock, ensure_ascii = False)

        with open(STOCK, 'w') as stock:
            stock.write(new_stock)