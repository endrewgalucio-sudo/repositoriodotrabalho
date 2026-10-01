# Exercício Sistema de Biblioteca

print("====================================")
print("       SISTEMA PARA BIBLIOTECA")
print("====================================")

biblioteca = []
lista = []
lista_alunos = []

repeticoes = int(input("Quantas vezes deseja utilizar o menu? "))

for i in range(repeticoes):

    print()
    print("====================================")
    print("       SISTEMA PARA BIBLIOTECA")
    print("====================================")
    print("1 - Menu de Livros")
    print("2 - Cadastrar Alunos")
    print("3 - Realizar Empréstimo")
    print("4 - Sair")
    print("====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        
        def cadastrar_livro():
            quantidade_livros = int(input("Quantos livros deseja cadastrar? "))
            for i in range(quantidade_livros):
                print()
                print("LIVRO", i + 1)      
                codigo = int(input("Código: "))
                    
                titulo = input("Título: ")
                if titulo == "":
                    print("Título do livro não pode ficar vazio.")
                    continue
                    
                autor = input("Autor: ")
                if autor == "":
                    print ("O autor do livro não pode ficar vazio.")
                ano = int(input("Ano: "))
                
                dados_livro = [codigo, titulo, autor, ano]
                biblioteca.append(dados_livro)
                lista.append(dados_livro)
                print(f"O Livro intitulado: '{titulo}' foi cadastrado com sucesso!")

        def listar_livros():
            if len(lista) == 0:
                print("Nenhum livro na lista até o momento.")
                print("Selecione novamente;")
            else: 
                print("\n===== Lista de Livros =====") 
                for livro in lista: 
                    print(f"- Título: {livro[1]} | Autor: {livro[2]} | Código: {livro[0]} | Ano: {livro[3]}")
        
        def alterar_livro():
            print("\n--- ALTERAR LIVRO ---")
            if len(lista) == 0:
                print("Nenhum livro cadastrado para alterar.")
                return
                
            livro_para_alterar = input("Digite o nome exato do título do livro que deseja alterar: ")
            
            achou = False
            for livro in lista:
                if livro[1] == livro_para_alterar:
                    print(f"Livro encontrado! Nome atual: {livro[1]}")
                    novo_titulo = input("Digite o novo título: ")
                    if novo_titulo != "":
                        livro[1] = novo_titulo
                        print("Título alterado com sucesso!")
                    achou = True
                    break
            
            if not achou:
                print("Esse livro não foi encontrado na lista.")

        def excluir_livro():
            print("\n--- EXCLUIR LIVRO ---")
            if len(lista) == 0:
                print("Nenhum livro cadastrado para excluir.")
                return
                
            livro_para_excluir = input("Digite o nome exato do título do livro que deseja excluir: ")
            
            achou = False
            for livro in lista:
                if livro[1] == livro_para_excluir:
                    lista.remove(livro)
                    if livro in biblioteca:
                        biblioteca.remove(livro)
                    print(f"Livro '{livro_para_excluir}' removido com sucesso!")
                    achou = True
                    break
            
            if not achou:
                print("Esse livro não foi encontrado na lista.")
    
        while True:
            print()
            print("========== SUBMENU DE LIVROS ==========")
            print("1 - Cadastrar livro") 
            print("2 - Listar livros")
            print("3 - Alterar livro")
            print("4 - Excluir livro")
            print("5 - Voltar ao Menu Principal")
            opcao_submenu = input("Escolha: ")
        
            if opcao_submenu == "1":
                cadastrar_livro()
            elif opcao_submenu == "2":
                listar_livros() 
            elif opcao_submenu == "3":
                alterar_livro()
            elif opcao_submenu == "4":
                excluir_livro()
            elif opcao_submenu == "5":
                print("Voltando ao menu anterior...")
                break
            else: 
                print("Opção Inválida!")

    elif opcao == "2":
        print()
        print("========== CADASTRO DE ALUNOS ==========")
        quantidade_alunos = int(input("Quantos alunos deseja cadastrar? "))

        for i in range(quantidade_alunos):
            print()
            print("ALUNO", i + 1)
            matricula = input("Matrícula: ")

            if matricula == "":
                print("Matrícula não pode ficar vazia.")
            else:
                nome = input("Nome do aluno: ")

                if nome == "":
                    print("Nome não pode vazio.")
                else:
                    turma = input("Turma: ")

                    if turma == "":
                        print("Turma não pode ficar vazia.")
                    else:
                        lista_alunos.append([matricula, nome, turma])
                        print("Aluno cadastrado com sucesso!")

    elif opcao == "3":
        print()
        print("========== EMPRÉSTIMO ==========")
        codigo_livro = input("Código do livro: ")

        if codigo_livro == "":
            print("Código do livro não pode ficar vazio.")
        else:
            matricula = input("Matrícula do aluno: ")

            if matricula == "":
                print("Matrícula do aluno não pode ficar vazia.")
            else:
                livro_existe = False
                for livro in lista:
                    if livro[0] == codigo_livro:
                        livro_existe = True
                        break
                
                aluno_existe = False
                for aluno in lista_alunos:
                    if aluno[0] == matricula:
                        aluno_existe = True
                        break
                
                if not livro_existe:
                    print("Não é possível realizar o empréstimo: Livro não cadastrado.")
                elif not aluno_existe:
                    print("Não é possível realizar o empréstimo: Aluno não cadastrado.")
                else:
                    quantidade_disponivel = input("Quantidade disponível de exemplares: ")

                    if quantidade_disponivel == "":
                        print("Quantidade disponível não pode ficar vazia.")
                    else:
                        quantidade_disponivel = int(quantidade_disponivel)

                        if quantidade_disponivel > 0:
                            print("Empréstimo realizado com sucesso!")
                        else:
                            print("Não é possível realizar o empréstimo.")
                            print("Não há exemplares disponíveis.")

    elif opcao == "4":
        print()
        print("Sistema encerrado.")
        break

    else:
        print()
        print("Opção inválida. Escolha uma opção de 1 a 4.")
