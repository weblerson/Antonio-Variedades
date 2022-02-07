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


                    if ProviderController.register(company, mensality, category) == True:
                        print("Fornecedor cadastrado com sucesso!")

                    elif ProviderController.register(company, mensality, category) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(ProviderController.register(company, mensality, category))

                        again = Interface.again()

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


                    if ProviderController.change(company, mensality, category, new_company) == True:
                        print("Fornecedor alterado com sucesso!")

                    elif ProviderController.change(company, mensality, category, new_company) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(ProviderController.change(company, mensality, category, new_company))
                        Interface.linebreak()

                        again = Interface.again()

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


                    if ProviderController.remove(company) == True:
                        print("O fornecedor foi removido com sucesso!")
                        
                    elif ProviderController.remove(company) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(ProviderController.remove(company))
                        Interface.linebreak()

                        again = Interface.again()

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


                    if CustomerController.register(nickname, name, cpf, address, sex) == True:
                        print("Cliente cadastrado com sucesso!")

                    elif CustomerController.register(nickname, name, cpf, address, sex) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(CustomerController.register(nickname, name, cpf, address, sex))
                        Interface.linebreak()

                        again = Interface.again()

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


                    if CustomerController.change(nickname, new_nickname) == True:
                        print("O nickname do cliente foi alterado com sucesso!")
                    
                    elif CustomerController.change(nickname, new_nickname) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(CustomerController.change(nickname, new_nickname))
                        Interface.linebreak()

                        again = Interface.again()
                        
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


                    if CustomerController.remove(nickname) == True:
                        print("O cliente foi removido com sucesso!")

                    elif CustomerController.remove(nickname) == False:
                        print("Ocorreu um erro. Tente novamente.")

                    else:
                        print(CustomerController.remove(nickname))
                        Interface.linebreak()

                        again = Interface.again()

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
                pass

            elif choice == 3:
                pass

            elif choice ==  4:
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