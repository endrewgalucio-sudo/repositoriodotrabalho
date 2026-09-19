# Exercício 5 - Validação

idade = int(input("Digite a sua idade: "))

while idade < 2 or idade > 120:
        
    if idade < 2:
        print("Valor inválido! Ninguém pode ter uma idade negativa, nasceu ontem por acaso? ")
    elif idade > 120:
        print("Valor inválido! Essa idade parece alta demais para um ser humano.")
           
    idade = int(input("Digite novamente uma idade válida: "))

print(f"\nIdade válida cadastrada com sucesso: {idade} anos! ")
