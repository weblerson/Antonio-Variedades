from controller import *
import os

class Interface:
    @classmethod
    def run(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4, 5, 6]

            print("Terminal de ações da Antonio Variedades. Selecione a ação que deseja executar:")
            print('''
            Digite 0 para uma operação de Caixa
            Digite 1 para ver as opções de Categoria
            Digite 2 para ver as opções de Produtos
            Digite 3 para ver as opções de Fornecedores
            Digite 4 para ver as opções de Clientes
            Digite 5 para ver as opções de Funcionários
            Digite 6 para ver as opções de Vendas''')

            Interface.linebreak()

            try:
                choice = int(input('Escolha: '))
            except:
                Interface.clear()
                print("Digite um comando numérico.")

                break

            if choice not in options:
                Interface.clear()
                print("Digite um comando válido.")

                Interface.linebreak()

                continue

            if choice == 0:
                Interface.cashier()
            elif choice == 1:
                Interface.category()
            elif choice == 2:
                Interface.product()
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass

    @classmethod
    def cashier(cls):
        Interface.clear()

        while True:
            options = ["S", "N", "0"]
            is_registered = None

            print("Digite 0 a qualquer momento para sair.\n")
            
            choice = input("O cliente tem cadastro? (S/N): ").upper()

            if choice not in options:
                os.system('clear')
                print("Digite um comando válido.")

                continue

            if choice == '0':
                Interface.clear()
                Interface.run()

            if choice == "S":
                is_registered = True

            elif choice == "N":
                choice = input("O cliente gostaria de se cadastrar? (S/N): ").upper()

                Interface.clear()

                if choice.upper() not in options:
                    Interface.clear()
                    print("Digite um comando válido.")

                    continue
                
                if choice == "S":
                    print("Digite as informações do cliente:")

                    name = input("Digite o nome completo do cliente: ")
                    cpf = input("Digite o CPF do cliente: ")
                    address = input("Digite o endereço do cliente: ")
                    sex = input("Digite o sexo do cliente: ")

                    nickname = input("Digite o nickname do cliente: ")

                    if CustomerController.register(nickname, name, cpf, address, sex):
                        print("Cliente cadastrado com sucesso!")
                        is_registered = True

                    elif not CustomerController.register(nickname, name, cpf, address, sex):
                        print("Ocorreu um erro. Tente novamente.")
                        is_registered = False

                    else:
                        print(CustomerController.nickname(nickname, name, cpf, address, sex))
                        is_registered = False

                elif choice == "N":
                    is_registered = False

            if is_registered:
                nickname = input("Digite o nickname do cliente que está comprando: ")

                while True:
                    print("\nDigite 0 para sair a qualquer momento.\n")

                    category = input("Digite a categoria do produto: ")
                    if category == '0':
                        Interface.clear()
                        break

                    name = input("Digite o nome do produto: ")
                    if name == '0':
                        Interface.clear()
                        break

                    amount = int(input("Digite a quantidade comprada de produtos: "))
                    if amount == 0:
                        Interface.clear()
                        break

                    Interface.linebreak()


                    if ProductController.add(category, name, amount) == True:
                        print("Vendas adicionadas com sucesso ao relatório do produto.")
                    
                    elif ProductController.add(category, name, amount) == False:
                        print("Ocorreu um erro ao adicionar vendas ao relatório do produto.")

                    else:
                        print(ProductController.add(category, name, amount))

                        again = Interface.again()

                        if again:
                            continue

                        if not again:
                            pass

                    Interface.linebreak()

                    if SalesController.add(nickname, amount, name, amount) == True:
                        print("Vendas adicionadas com sucesso ao relatório do cliente.")

                    elif SalesController.add(nickname, amount, name, amount) == False:
                        print("Ocorreu um erro ao adicionar vendas ao relatório do cliente.")

                    else:
                        print(SalesController.add(nickname, amount, name, amount))

                        again = Interface.again()

                        if again:
                            continue

                        if not again:
                            pass

                    Interface.linebreak()


                    if DailySalesController.add(amount):
                        print("Vendas adicionadas com sucesso ao relatório diário.")

                    elif not DailySalesController.add(amount):
                        print("Ocorreu um erro ao adicionar vendas ao relatório diário.")

            else:
                while True:
                    print("\nDigite 0 para sair a qualquer momento.\n")

                    category = input("Digite a categoria do produto: ")
                    if category == '0':
                        Interface.clear()
                        break

                    name = input("Digite o nome do produto: ")
                    if name == '0':
                        Interface.clear()
                        break

                    amount = int(input("Digite a quantidade comprada de produtos: "))
                    if amount == 0:
                        Interface.clear()
                        break

                    Interface.linebreak()


                    if ProductController.add(category, name, amount) == True:
                        print("Vendas adicionadas com sucesso ao relatório do produto.")
                    
                    elif ProductController.add(category, name, amount) == False:
                        print("Ocorreu um erro ao adicionar vendas ao relatório do produto.")

                    else:
                        print(ProductController.add(category, name, amount))

                        again = Interface.again()

                        if again:
                            continue

                        if not again:
                            pass

                    Interface.linebreak()


                    if DailySalesController.add(amount):
                        print("Vendas adicionadas com sucesso ao relatório diário.")

                    elif not DailySalesController.add(amount):
                        print("Ocorreu um erro ao adicionar vendas ao relatório diário.")

    @classmethod
    def category(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4]

            print("Terminal de ações de Categoria. Selecione a ação que deseja executar:")
            print("Digite 0 para sair a qualquer momento!")
            Interface.linebreak()

            print('''
            Digite 1 para fazer a leitura das categorias.
            Digite 2 para fazer o cadastro de uma categoria.
            Digite 3 para fazer a alteração de uma categoria.
            Digite 4 para excluir uma categoria.''')

            Interface.linebreak()

            try:
                choice = int(input("Escolha: "))

            except:
                Interface.clear()
                print("Digite um comando numérico.")

                Interface.linebreak()

                continue


            if choice not in options:
                Interface.clear()
                print("Digite um comando válido.")

                Interface.linebreak()

                continue


            if choice == 0:
                break

            elif choice == 1:
                Interface.clear()

                print("Categorias:")
                Interface.linebreak()

                for category in CategoryController.read():
                    print(category)

                Interface.linebreak()

                print("Para sair, digite qualquer tecla.")
                choice = input("Escolha: ")

                Interface.clear()

                break

            elif choice == 2:
                while True:
                    Interface.clear()

                    print("Para cancelar a qualquer momento, digite 0.")
                    Interface.linebreak()

                    new_category = input("Digite o nome da nova categoria: ")
                    if new_category == '0':
                        Interface.clear()

                        break

                    if CategoryController.register(new_category) == True:
                        print("Categoria cadastrada com sucesso!")
                        Interface.linebreak()
                    
                    elif CategoryController.register(new_category) == False:
                        print("Ocorreu um erro. Tente novamente.")
                        Interface.linebreak()

                    else:
                        print(CategoryController.register(new_category))
                        Interface.linebreak()

                        again = Interface.again()

                        if again:
                            continue

                        elif not again:
                            pass


                    print("Para cadastrar mais uma, digite 'S', senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue
                    
                    Interface.clear()

                    break

            elif choice == 3:
                while True:
                    Interface.clear()

                    print("Para cancelar a qualquer momento, digite 0.")
                    Interface.linebreak()

                    old_category = input("Digite o nome da categoria que deseja alterar: ")
                    if old_category == '0':
                        Interface.clear()

                        break

                    new_category = input(f"Digite um novo nome para a categoria {old_category}: ")
                    if new_category == '0':
                        Interface.clear()

                        break

                    if CategoryController.change(old_category, new_category) == True:
                        print("Categoria alterada com sucesso!")
                        Interface.linebreak()

                    elif CategoryController.change(old_category, new_category) == False:
                        print("Ocorreu um erro. Tente novamente.")
                        Interface.linebreak()

                    else:
                        print(CategoryController.change(old_category, new_category))
                        Interface.linebreak()

                        again = Interface.again()

                        if again:
                            continue

                        elif not again:
                            pass
                    

                    print("Para alterar mais uma, digite 'A', senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'A':
                        continue
                    
                    Interface.clear()

                    break

            elif choice == 4:
                while True:
                    Interface.clear()

                    print("Para cancelar a qualquer momento, digite 0")
                    Interface.linebreak()

                    category = input("Digite o nome da categoria que deseja excluir: ")

                    if category == '0':
                        break

                    if CategoryController.remove(category) == True:
                        print("Categoria excluída com sucesso!")
                        Interface.linebreak()
                    
                    elif CategoryController.remove(category) == False:
                        print("Ocorreu um erro. Tente novamente.")
                        Interface.linebreak()

                    else:
                        print(CategoryController.remove(category))
                        Interface.linebreak()

                        again = Interface.again()

                        if again:
                            continue

                        elif not again:
                            pass

                    
                    print("Para excluir mais uma, digite 'E', senão, digite qualquer tecla para sair.")

                    choice = input("Escolha: ").upper()

                    if choice == 'E':
                        continue

                    Interface.clear()
                    
                    break

    @classmethod
    def product(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4]

            print("Terminal de ações de Produtos. Selecione a ação que deseja executar:")
            print("Digite 0 para sair a qualquer momento!")

            print('''
            Digite 1 para fazer a leitura dos produtos.
            Digite 2 para fazer o cadastro de um produto.
            Digite 3 para fazer a alteração de um produto.
            Digite 4 para excluir um produto.''')

            Interface.linebreak()

            try:
                choice = int(input("Escolha: "))

            except:
                Interface.clear()
                print("Digite um comando numérico.")

                Interface.linebreak()

                continue


            if choice not in options:
                Interface.clear()
                print("Digite um comando válido.")

                Interface.linebreak()

                continue


            if choice == 0:
                break

            elif choice == 1:
                Interface.clear()

                category = input("Digite a categoria da qual deseja ver os produtos: ")
                Interface.linebreak()

                print(f"Produtos na categoria {category}:")

                for product in ProductController.read(category):
                    print(product)

                Interface.linebreak()
                
                input("Digite qualquer coisa para sair: ")

                Interface.clear()

            elif choice == 2:
                while True:
                    Interface.clear()

                    print("Para sair a qualquer momento, digite 0.")
                    Interface.linebreak()

                    category = input("Digite a categoria na qual deseja cadastrar o produto: ")
                    if category == '0':
                        Interface.clear()
                        break

                    name = input("Digite o nome do novo produto: ")
                    if name == '0':
                        Interface.clear()
                        break

                    price = float(input("Digite o preço do novo produto: "))
                    if price == 0:
                        Interface.clear()
                        break

                    Interface.linebreak()

                    if ProductController.register(category, name, price) == True:
                        print("Produto cadastrado com sucesso!")

                    elif ProductController.register(category, name, price) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(ProductController.register(category, name, price))
                        Interface.linebreak()

                        again = Interface.again()

                        if again:
                            continue

                        else:
                            pass

                    choice = input("Digite S para cadastrar outro produto, senão, digite qualquer tecla para sair.").upper()
                    
                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 3:
                while True:
                    Interface.clear()

                    print("Para sair a qualquer momento, digite 0.")
                    Interface.linebreak()

                    category = input("Digite a categoria na qual deseja alterar um produto: ")
                    if category == '0':
                        Interface.clear()
                        break

                    name = input("Digite o nome do produto que deseja alterar: ")
                    if name == '0':
                        Interface.clear()
                        break

                    new_product = input("Digite o nome do novo produto: ")
                    if new_product == '0':
                        Interface.clear()
                        break

                    price = float(input("Digite o preço do novo produto: "))
                    if price == 0:
                        Interface.clear()
                        break

                    Interface.linebreak()

                    if ProductController.change(category, name, price, new_product) == True:
                        print("Produto alterado com sucesso!")

                    elif ProductController.change(category, name, price, new_product) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(ProductController.change(category, name, price, new_product))
                        Interface.linebreak()

                        again = Interface.again()

                        if again:
                            continue

                        else:
                            pass
                    
                    choice = input("Digite S para alterar outro produto. Senão, digite qualquer tecla para sair.").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 4:
                while True:
                    Interface.clear()

                    print("Para sair a qualquer momento, digite 0.")

                    Interface.linebreak()

                    category = input("Digite o nome da categoria da qual deseja remover um produto: ")
                    if category == '0':
                        Interface.clear()

                        break

                    name = input("Digite o nome do produto que deseja remover: ")
                    if name == '0':
                        Interface.clear()

                        break

                    Interface.linebreak()

                    if ProductController.remove(category, name) == True:
                        print("Produto removido com sucesso!")

                    elif ProductController.remove(category, name) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(ProductController.remove(category, name))
                        Interface.linebreak()

                        again = Interface.again()

                        if again:
                            continue

                        else:
                            pass

                    choice = input("Digite S para remover outro produto. Senão, digite qualquer tecla para sair.").upper()
                    if choice == 'S':
                        continue

                    Interface.clear()

                    break


    @classmethod
    def provider(cls):
        Interface.clear()

        while True:
            pass

    @classmethod
    def again(cls):
        options = ["S", "N", "0"]
        choice = input("Quer tentar novamente? (S/N): ").upper()

        if choice not in options:
            Interface.clear()
            print("Digite uma opção válida.")

            return True


        if choice == 'S':
            Interface.clear()

            return True

        elif choice == '0':
            Interface.clear()

            return False

    @classmethod
    def linebreak(cls):
        print(" ")

    @classmethod
    def clear(cls):
        os.system('clear')

if __name__ == "__main__":
    Interface.run()