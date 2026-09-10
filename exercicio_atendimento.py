nome = input ("Nome de usuário: ")


print("Selecione o número que corresponde ao tipo de problema na lista abaixo:")
print("1 - Indisponibilidade total do sistema;")
print("2 - Sistema funcionando, mas com lentidão ou erros;")
print("3 - Problema que não impede o trabalho;" )
print("4 - Outros problemas.")

problema = input ("Qual é o tipo de problema? ")

if problema == "1":
 prioridade = "Crítica"

elif problema == "2":
 prioridade = "Alta"

elif problema == "3":
 prioridade = "Média"

elif problema == "4":
 prioridade = "Baixa"

else : "Ops! Não conseguimos indentificar este problema, por favor selecione um dos listados por número."

tempo = int (input ("Há quantos minutos o problema foi relatado? "))

print ("Usuário:" , nome)
print ("Tipo de Problema:", problema)
print ("Tempo do Problema:", tempo, "minutos")
print ("Prioridade:", prioridade)
