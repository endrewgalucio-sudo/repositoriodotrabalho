def verificar_senha():
    senha_correta = "1234"
    senha = input("Digite a senha correta: ")
    
    while True:
        if senha == "1234":
            print("Senha Correta! Acesso Liberado. 🔓")
            break
        else:
            print("Senha Incorreta! ❌")
            senha = input("Tente novamente: ")

# O programa principal fica limpo e fácil de ler:
print("Iniciando o sistema...")
verificar_senha()  # O Python vai lá dentro do 'def' e executa tudo
print("Sistema encerrado.")


#         codigo = int(input("Código: "))
#        titulo = input("Título: ")
#        autor = input("Autor: ")
#        ano = int(input("Ano: "))
                  
 #       livro = [codigo, titulo, autor, ano]