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
                Interface.provider()
            elif choice == 4:
                Interface.customer()
            elif choice == 5:
                Interface.employee()
            elif choice == 6:
                Interface.sales()

    @classmethod
    def cashier(cls):
        Interface.clear()

        while True:
            options = ["S", "N", "0"]
            is_registered = None

            print("Digite 0 a qualquer momento para sair.\n")
            
            choice = input("O cliente tem cadastro? (S/N): ").upper()

            if choice not in options:
                Interface.clear()
                print("Digite um comando válido.")

                continue

            if choice == '0':
                Interface.clear()
                break

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

                    if CustomerController.register(nickname, name, cpf, address, sex) == True:
                        print("Cliente cadastrado com sucesso!")
                        is_registered = True

                    elif CustomerController.register(nickname, name, cpf, address, sex) == False:
                        print("Ocorreu um erro. Tente novamente.")
                        is_registered = False

                    else:
                        print(CustomerController.nickname(nickname, name, cpf, address, sex))
                        is_registered = False

                elif choice == "N":
                    is_registered = False

                Interface.clear()

            if is_registered:
                nickname = input("Digite o nickname do cliente que está comprando: ")

                price = 0
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento.")
                    Interface.linebreak()

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

                    price += ProductController.read(category)[name]["preço"] * amount

                    Interface.linebreak()


                    if StockController.remove(name, amount) == True:
                        print("Quantidade removida com sucesso do estoque do produto!")

                    elif StockController.remove(name, amount) == False:
                        Interface.clear()
                        print("Ocorreu um erro. Tente novamente!")

                        break

                    else:
                        Interface.clear()
                        print(StockController.remove(name, amount))

                        break

                    success = "Vendas adicionadas com sucesso ao relatório do produto."
                    again = Interface.test(ProductController.add(category, name, amount), success)

                    if again:
                        continue

                    else:
                        pass
                    
                    success = "Vendas adicionadas com sucesso ao relatório do cliente."
                    again = Interface.test(SalesController.add(nickname, amount, name, amount), success)

                    if again:
                        continue

                    else:
                        pass


                    if DailySalesController.add(amount):
                        print("Vendas adicionadas com sucesso ao relatório diário.")

                    elif not DailySalesController.add(amount):
                        print("Ocorreu um erro ao adicionar vendas ao relatório diário.")

                    Interface.linebreak()

                    print(f"Preço total a ser pago: R$ {price}")

                    Interface.linebreak()

                    print("Para fazer mais uma operação, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            else:
                price = 0
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento.")
                    Interface.linebreak()

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

                    price += ProductController.read(category)[name]["preço"] * amount

                    Interface.linebreak()

                    if StockController.remove(name, amount) == True:
                        print("Quantidade removida com sucesso do estoque do produto!")

                    elif StockController.remove(name, amount) == False:
                        Interface.clear()
                        print("Ocorreu um erro. Tente novamente!")

                        break

                    else:
                        Interface.clear()
                        print(StockController.remove(name, amount))

                        break

                    success = "Vendas adicionadas com sucesso ao relatório do produto!"
                    again = Interface.test(ProductController.add(category, name, amount), success)

                    if again:
                        continue

                    else:
                        pass


                    if DailySalesController.add(amount):
                        print("Vendas adicionadas com sucesso ao relatório diário.")

                    elif not DailySalesController.add(amount):
                        print("Ocorreu um erro ao adicionar vendas ao relatório diário.")

                    Interface.linebreak()

                    print(f"Preço total a ser pago: R$ {price}")

                    Interface.linebreak()

                    print("Para fazer mais uma operação, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

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

                    Interface.linebreak()


                    success = "Categoria cadastrada com sucesso!"
                    again = Interface.test(CategoryController.register(new_category), success)

                    if again:
                        continue

                    else:
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

                    Interface.linebreak()


                    success = "Categoria alterada com sucesso!"
                    again = Interface.test(CategoryController.change(old_category, new_category), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para alterar mais uma, digite 'S', senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
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
                        Interface.clear()
                        break

                    Interface.linebreak()
                    

                    success = "Categoria excluída com sucesso!"
                    again = Interface.test(CategoryController.remove(category), success)

                    if again:
                        continue

                    else:
                        pass
                    
                    print("Para excluir mais uma, digite 'S', senão, digite qualquer tecla para sair.")

                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()
                    
                    break

    @classmethod
    def product(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4, 5, 6]

            print("Terminal de ações de Produtos. Selecione a ação que deseja executar:")
            print("Digite 0 para sair a qualquer momento!")

            print('''
            Digite 1 para fazer a leitura dos produtos.
            Digite 2 para fazer o cadastro de um produto.
            Digite 3 para fazer a alteração de um produto.
            Digite 4 para excluir um produto.
            Digite 5 para adicionar produto no estoque.
            Digite 6 para tirar produto do estoque.''')

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
                    

                    success = "Produto cadastrado com sucesso!"
                    again = Interface.test(ProductController.register(category, name, price), success)

                    if again:
                        continue

                    else:
                        pass

                    success = "Produto cadastrado com sucesso no estoque!"
                    again = Interface.test(StockController.register(name), success)

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


                    success = "Produto alterado com sucesso!"
                    again = Interface.test(ProductController.change(category, name, price, new_product), success)

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


                    success = "Produto removido com sucesso!"
                    again = Interface.test(ProductController.remove(category, name), success)

                    if again:
                        continue

                    else:
                        pass

                    success = "Produto removido com sucesso do estoque!"
                    again = Interface.test(StockController.unregister(name), success)

                    if again:
                        continue

                    else:
                        pass

                    choice = input("Digite S para remover outro produto. Senão, digite qualquer tecla para sair.").upper()
                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 5:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")

                    product = input("Digite o nome do produto: ").lower()
                    if product == '0':
                        break

                    amount = int(input("Digite a quantidade a ser adicionada ao estoque: "))
                    if amount == 0:
                        break

                    Interface.linebreak()

                    success = "Quantidade adicionada com sucesso ao estoque!"
                    again = Interface.test(StockController.add(product, amount), success)

                    Interface.linebreak()

                    if again:
                        continue

                    else:
                        pass

                    print("Para adicionar mais um produto, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 6:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")

                    product = input("Digite o nome do produto: ").lower()
                    if product == '0':
                        break

                    amount = int(input("Digite a quantidade a ser removida do estoque: "))
                    if amount == 0:
                        break

                    Interface.linebreak()

                    success = "Quantidade removida com sucesso do estoque estoque!"
                    again = Interface.test(StockController.remove(product, amount), success)

                    Interface.linebreak()

                    if again:
                        continue

                    else:
                        pass

                    print("Para remover mais um produto, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

    @classmethod
    def provider(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4]

            print("Terminal de ações de Fornecedores. Selecione a opção que deseja executar.")
            print("Digite 0 para sair a qualquer momento!")

            print('''
            Digite 1 para fazer a leitura dos fornecedores.
            Digite 2 para fazer o cadastro de um fornecedor.
            Digite 3 para fazer a alteração de um fornecedor.
            Digite 4 para excluir um fornecedor.''')

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

                provider_list, provider_info_list = ProviderController.read()

                index = 0
                for provider in provider_list:
                    print(f"{provider}:")
                    print(f"Categoria: {provider_info_list[index]['categoria']}")
                    print(f"Mensalidade: R$ {provider_info_list[index]['mensalidade']}")

                    Interface.linebreak()

                    index += 1

                Interface.linebreak()

                input("Digite qualquer tecla para sair.")

                Interface.clear()

            elif choice == 2:
                while True:
                    Interface.clear()

                    print("Digite 0 a qualquer momento para sair!")
                    Interface.linebreak()

                    company = input("Digite o nome do fornecedor/empresa: ")
                    if company == '0':
                        Interface.clear()
                        break

                    try:
                        mensality = float(input("Digite a mensalidade que vai ser paga ao fornecedor: "))
                    except:
                        Interface.linebreak()
                        print("Digite um valor numérico!")

                        again = Interface.again()

                        if again:
                            continue

                        else:
                            Interface.clear()

                            break

                    if mensality == 0:
                        Interface.clear()
                        break

                    category = input("Digite a categoria dos produtos que o fornecedor vai prover: ")
                    if category == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()


                    success = "Fornecedor cadastrado com sucesso!"
                    again = Interface.test(ProviderController.register(company, mensality, category), success)

                    if again:
                        continue

                    else:
                        pass

                    Interface.linebreak()

                    print("Para realizar um cadastro novamente, digite 'S'. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 3:
                while True:
                    options = ["S", "N"]
                    Interface.clear()

                    print("Digite 0 a qualquer momento para sair!")
                    Interface.linebreak()

                    new = input("O fornecedor mudou de nome ou quer mudar de fornecedor? (S/N): ").upper()

                    if new not in options:
                        Interface.clear()
                        print("Digite um comando válido!")

                        stop = input("Digite qualquer tecla para continuar")

                        continue


                    company = input("Digite o nome do fornecedor que deseja alterar: ")
                    if company == '0':
                        Interface.clear()
                        break

                    if new == 'S':
                        new_company = input("Digite o nome do novo fornecedor: ")
                        if new_company == '0':
                            Interface.clear()
                            break

                    elif new == 'N':
                        new_company = company

                    category = input("Digite o nome da nova categoria: ")
                    if category == '0':
                        Interface.clear()
                        break

                    try:
                        mensality = float(input("Digite o novo valor da mensalidade: "))
                    except:
                        Interface.linebreak()
                        print("Digite um valor numérico!")

                        again = Interface.again()

                        if again:
                            continue

                        else:
                            break

                    if mensality == 0:
                        Interface.clear()
                        break
                    
                    Interface.linebreak()


                    success = "Fornecedor alterado com sucesso!"
                    again = Interface.test(ProviderController.change(company, mensality, category, new_company), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para alterar mais um fornecedor, digite 'S'. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 4:
                while True:
                    Interface.clear()
                    
                    print("Digite 0 para sair a qualquer momento!")
                    Interface.linebreak()

                    company = input("Digite o nome do fornecedor que deseja remover: ")
                    if company == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()


                    success = "O fornecedor foi removido com sucesso!"
                    again = Interface.test(ProviderController.remove(company), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para remover mais um fornecedor, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()
                    
                    break

    @classmethod
    def customer(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4]

            print("Terminal de ações de Clientes. Selecione a opção que deseja executar.")
            print("Digite 0 para sair a qualquer momento!")

            print('''
            Digite 1 para fazer a leitura dos clientes.
            Digite 2 para fazer o cadastro de um cliente.
            Digite 3 para fazer a alteração do nickname de um cliente.
            Digite 4 para excluir um cliente.''')

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

                customer_list, customer_info_list = CustomerController.read()

                print("Digite 'F' para exibir a informação de um cliente por nickname. Senão, digite qualquer tecla para mostrar todos.")
                choice = input("Escolha: ").upper()

                Interface.clear()

                if choice == 'F':
                    nickname = input("Digite o nickname do cliente: ")
                    Interface.linebreak()

                    if nickname not in customer_list:
                        print("Não existe nenhum cliente com esse nickname. Não é possível exibir informações.")
                        Interface.linebreak()
                    
                    else:
                        index = customer_list.index(nickname)

                        print(f"{nickname}:")
                        print(f"Nome completo: {customer_info_list[index]['nome']}")
                        print(f"Sexo: {customer_info_list[index]['sexo']}")
                        print(f"CPF: {customer_info_list[index]['cpf']}")
                        print(f"Endereço: {customer_info_list[index]['endereço']}")
                        
                        Interface.linebreak()



                else:
                    index = 0
                    for customer in customer_list:
                        print(f"{customer}:")
                        print(f"Nome completo: {customer_info_list[index]['nome']}")
                        print(f"Sexo: {customer_info_list[index]['sexo']}")
                        print(f"CPF: {customer_info_list[index]['cpf']}")
                        print(f"Endereço: {customer_info_list[index]['endereço']}")
                        
                        Interface.linebreak()

                        index += 1

                input("Digite qualquer tecla para sair.")

                Interface.clear()

            elif choice == 2:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")
                    Interface.linebreak()

                    nickname = input("Digite o nickname do cliente: ")
                    if nickname == '0':
                        Interface.clear()
                        break

                    name = input("Digite o nome completo do cliente: ")
                    if name == '0':
                        Interface.clear()
                        break

                    cpf = input("Digite o CPF do cliente: ")
                    if cpf == '0':
                        Interface.clear()
                        break

                    address = input("Digite o endereço completo do cliente (Rua, Bairro): ")
                    if address == '0':
                        Interface.clear()
                        break
                    
                    sex = input("Digite o sexo do cliente: ")
                    if sex == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()


                    success = "Cliente cadastrado com sucesso!"
                    again = Interface.test(CustomerController.register(nickname, name, cpf, address, sex), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Digite S para cadastrar mais um cliente. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 3:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")
                    Interface.linebreak()

                    nickname = input("Digite o nickname antigo do cliente: ")
                    if nickname == '0':
                        Interface.clear()
                        break

                    new_nickname = input("Digite o novo nickname do cliente: ")
                    if new_nickname == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()


                    success = "O nickname do cliente foi alterado com sucesso!"
                    again = Interface.test(CustomerController.change(nickname, new_nickname), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para alterar o nickname de outro cliente, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 4:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")
                    Interface.linebreak()

                    nickname = input("Digite o nickname do cliente que deseja remover: ")
                    if nickname == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()

                    
                    success = "O cliente foi removido com sucesso!"
                    again = Interface.test(CustomerController.remove(nickname), success)
                    
                    if again:
                        continue

                    else:
                        pass

                    print("Para remover mais um cliente, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

    @classmethod
    def employee(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4]

            print("Terminal de ações de Funcionários. Selecione a opção que deseja executar.")
            print("Digite 0 para sair a qualquer momento!")

            print('''
            Digite 1 para fazer a leitura dos funcionários.
            Digite 2 para fazer o cadastro de um funcionários.
            Digite 3 para fazer a alteração do nickname de um funcionário.
            Digite 4 para excluir um funcionário.''')

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
                employee_list, employee_info_list = EmployeeController.read()

                print("Digite F para exibir as informações de um funcionário. Senão, digite qualquer tecla para mostrar todos.")
                choice = input("Escolha: ").upper()

                Interface.linebreak()

                if choice == 'F':
                    Interface.clear()
                    nickname = input("Digite o nickname do funcionário: ")

                    Interface.linebreak()

                    if nickname not in employee_list:
                        print("Não existe nenhum funcionário com esse nickname. Impossível exibir as informações.")

                    else:
                        index = employee_list.index(nickname)

                        print(f"{nickname}:")
                        print(f"Nome Completo: {employee_info_list[index]['nome']}")
                        print(f"Sexo: {employee_info_list[index]['sexo']}")
                        print(f"CPF: {employee_info_list[index]['cpf']}")
                        print(f"Endereço: {employee_info_list[index]['endereço']}")
                        print(f"Data de Nascimento: {employee_info_list[index]['data de nascimento']}")
                        print(f"Estado Civil: {employee_info_list[index]['estado civil']}")

                else:
                    Interface.clear()

                    index = 0
                    for employee in employee_list:
                        print(f"{employee}:")
                        print(f"Nome Completo: {employee_info_list[index]['nome']}")
                        print(f"Sexo: {employee_info_list[index]['sexo']}")
                        print(f"CPF: {employee_info_list[index]['cpf']}")
                        print(f"Endereço: {employee_info_list[index]['endereço']}")
                        print(f"Data de Nascimento: {employee_info_list[index]['data de nascimento']}")
                        print(f"Estado Civil: {employee_info_list[index]['estado civil']}")

                        Interface.linebreak()
                        index += 1


                input("Digite qualquer tecla para sair.")

                Interface.clear()

            elif choice == 2:
                while True:
                    Interface.clear()

                    print("Digite 0 a qualquer momento para sair!")
                    Interface.linebreak()

                    nickname = input("Digite o nickname do funcionário: ")
                    if nickname == '0':
                        Interface.clear()
                        break

                    birthdate = input("Digite a data de nascimento do funcionário: ")
                    if birthdate == '0':
                        Interface.clear()
                        break

                    marital_state = input("Digite o estado civil do funcionário: ")
                    if marital_state == '0':
                        Interface.clear()
                        break

                    name = input("Digite o nome completo do funcionário: ")
                    if name == '0':
                        Interface.clear()
                        break

                    cpf = input("Digite o CPF do funcionário: ")
                    if cpf == '0':
                        Interface.clear()
                        break

                    address = input("Digite o endereço completo do funcionário (Rua, Bairro): ")
                    if address == '0':
                        Interface.clear()
                        break

                    sex =  input("Digite o sexo do funcionário: ")
                    if sex == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()


                    success = "Funcionário cadastrado com sucesso!"
                    again = Interface.test(EmployeeController.register(nickname, birthdate, marital_state, name, cpf, address, sex), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para cadastrar mais um funcionário, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice == 3:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")
                    Interface.linebreak()

                    nickname = input("Digite o nickname do funcionário que deseja alterar: ")
                    if nickname == '0':
                        Interface.clear()
                        break

                    new_nickname = input("Digite o novo nickname do funcionário: ")
                    if new_nickname == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()


                    success = "Nickname do funcionário alterado com sucesso!"
                    again = Interface.test(EmployeeController.change(nickname, new_nickname), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para alterar o nickname de mais um funcionário, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

            elif choice ==  4:
                while True:
                    Interface.clear()

                    print("Digite 0 para sair a qualquer momento!")
                    Interface.linebreak()

                    nickname = input("Digite o nickname do funcionário que deseja remover: ")
                    if nickname == '0':
                        Interface.clear()
                        break

                    Interface.linebreak()

                    success = "Funcionário removido com sucesso!"
                    again = Interface.test(EmployeeController.remove(nickname), success)

                    if again:
                        continue

                    else:
                        pass

                    print("Para remover mais um funcionário, digite S. Senão, digite qualquer tecla para sair.")
                    choice = input("Escolha: ").upper()

                    if choice == 'S':
                        continue

                    Interface.clear()

                    break

    @classmethod
    def sales(cls):
        Interface.clear()

        while True:
            options = [0, 1, 2, 3, 4, 5]

            print("Terminal de ações de Vendas. Selecione a opção que deseja executar.")
            print("Digite 0 para sair a qualquer momento!")

            print('''
            Digite 1 para ver o relatório geral de vendas.
            Digite 2 para ver o relatório de vendas por data.
            Digite 3 para ver o relatório de produtos mais vendidos.
            Digite 4 para ver o relatório de clientes cadastrados que mais compraram.
            Digite 5 para ver o relatório de estoque disponível por produto.''')

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
                daily_sales = [sales for sales in DailySalesController.read().values()]

                sales = 0
                for sale in daily_sales:
                    sales += sale["vendas"]

                print(f"Vendas Totais: {sales}")

                Interface.linebreak()

                input("Digite qualquer tecla para sair.")

                Interface.clear()

                break

            elif choice == 2:
                Interface.clear()
                daily_sales = DailySalesController.read()

                for date in DailySalesController.read().keys():
                    print(f"Data: {date}")
                    print(f"Vendas: {daily_sales[date]['vendas']}")

                    Interface.linebreak()

                input("Digite qualquer tecla para sair.")

                Interface.clear()

                break

            elif choice == 3:
                Interface.clear()
                category_list = CategoryController.read()

                product_sales_list = []
                for category in category_list:
                    product_list = ProductController.read(category)

                    for product in product_list.keys():
                        product_sales_list.append((product, product_list[product]["vendas"]))

                product_sales_list.sort(key = lambda x: x[1], reverse = True)

                if len(product_sales_list) >= 3:
                    print("Top 3 produtos mais vendidos:")
                    Interface.linebreak()

                    print(f"1° lugar: {product_sales_list[0][0]} com {product_sales_list[0][1]} vendas!")
                    print(f"2° lugar: {product_sales_list[1][0]} com {product_sales_list[1][1]} vendas!")
                    print(f"3° lugar: {product_sales_list[2][0]} com {product_sales_list[2][1]} vendas!")

                else:
                    print("Não existe quantidade suficiente de produtos cadastrados para montar um ranking.")

                Interface.linebreak()

                input("Digite qualquer tecla para sair.")

                Interface.clear()

                break

            elif choice == 4:
                Interface.clear()
                sales = SalesController.read()
                customer_list = [customer for customer in SalesController.read().keys()]

                customer_purchases_list = []
                for customer in sales.keys():
                    customer_purchases_list.append((customer, sales[customer]["compras"]))

                customer_purchases_list.sort(key = lambda x: x[1], reverse = True)

                if len(customer_list) >= 3:
                    print("Top 3 clientes que mais compraram:")
                    Interface.linebreak()

                    print(f"1° lugar: {customer_purchases_list[0][0]} com {customer_purchases_list[0][1]} compras!")
                    print(f"2° lugar: {customer_purchases_list[1][0]} com {customer_purchases_list[1][1]} compras!")
                    print(f"3° lugar: {customer_purchases_list[2][0]} com {customer_purchases_list[2][1]} compras!")

                else:
                    print("Não tem clientes cadastrados o suficiente para montar um ranking de 3 pessoas.")

                Interface.linebreak()

                input("Digite qualquer tecla para sair.")

                Interface.clear()

                break

            elif choice == 5:
                Interface.clear()
                stock_items, stock_info = StockController.read()

                index = 0
                for product in stock_items:
                    print(f"Produto: {product}")
                    print(f"Quantidade no estoque: {stock_info[index]['quantidade']}")

                    index += 1
                    Interface.linebreak()

                input("Digite qualquer tecla para sair.")

                Interface.clear()

                break

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
    def test(cls, function, success):
        if function == True:
            print(success)

        elif function == False:
            print("Ocorreu um erro. Tente novamente.")

        else:
            print(function)
            Interface.linebreak()

            again = Interface.again()

            if again:
                return True

            else:
                return False

    @classmethod
    def clear(cls):
        os.system('clear')

if __name__ == "__main__":
    Interface.run()