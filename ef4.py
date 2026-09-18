# Exercício 4 - Menu simples

opcao = 0


while opcao != 3:
  print ("MENU SIMPLES")
  print ("1 - Cadastrar Livro;")
  print ("2 - Listar Livro;")
  print ("3 - Sair")

  opcao = int (input ("Digite o número correspondente a opção: "))

  if opcao == 1:
     cadastro = input ("Digite o título do livro: ")
     print ("Livro cadastrado!", cadastro)
  elif opcao == 2:
     print ("Livro listado.")
  elif opcao == 3:
     print ("Saindo do menu.")
  else: print ("Inválido, digite novamente.")