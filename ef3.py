# Exercício 3 - Cadastro

alunos = int(input ("Quantos alunos serão cadastrados? "))
contador = 1


while contador <= alunos:
   nome = input ("Digite o nome do aluno: {contador}" )
   print ("Aluno cadastrado:", nome)
   contador += 1
print ("Todos os alunos foram  cadastrados com sucesso!!")