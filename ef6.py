# Exercício 6 - Senha

print ("Seja bem-vindo! Usuário.")
senha = (input("Digite a senha correta: "))
while True:
   
    if senha == "1234":
    
      print ("Senha Correta! Acesso Liberado.")
    else:
     print ("Senha Incorreta!")

    senha = input ("Tente novamente:")
    break