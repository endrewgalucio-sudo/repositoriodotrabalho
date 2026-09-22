# Exercício Sistema de Biblioteca
quantidade = int(input ("Quantos alunos deseja cadastrar? "))
print("====================================")
print("       SISTEMA PARA BIBLIOTECA")
print("====================================")

repeticoes = int(input("Quantas vezes deseja utilizar o menu? "))

for i in range(repeticoes):

    print()
    print("====================================")
    print("       SISTEMA PARA BIBLIOTECA")
    print("====================================")
    print("1 - Cadastrar Livros")
    print("2 - Cadastrar Alunos")
    print("3 - Realizar Empréstimo")
    print("4 - Sair")
    print("====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
     while opcao != "6":
        print()
        print ("\n========== SISTEMA DE BIBLIOTECA ==========")
        print ("1 - Cadastrar livro") 
        print ("2 - Listar livros")
        print ("3 - Pesquisar livro")
        print ("4 - Alterar lvro")
        print ("5 - Excluir livro")
        print ("6 - Sair")
        break
     if opcao == "1":
        
        quantidade_livros = int(input("Quantos livros deseja cadastrar? "))
        for i in range(quantidade_livros):
                
                            print()
                            print("LIVRO", i + 1)
        biblioteca = []

        codigo = int(input("Código: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
                  
        livro = [codigo, titulo, autor, ano]
        biblioteca.append(livro)         

        print("Livro Cadastrado!")
        print(f"\n", biblioteca)
        
       
            

        if codigo == "":
                print("Código do livro não pode ficar vazio.")
        
                if titulo == "":
                    print("Título do livro não pode ficar vazio.")
               

                   
                



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
                    print("Nome não pode ficar vazio.")
                else:
                    turma = input("Turma: ")

                    if turma == "":
                        print("Turma não pode ficar vazia.")
                    else:
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
                quantidade_disponivel = input(
                    "Quantidade disponível: "
                )

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
    



