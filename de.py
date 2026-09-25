def calcular_total (preco, quantidade):
      
   return preco * quantidade

preco = float(input ("Digite o preço: "))
quantidade = int(input ("Digite a quantidade: "))     

total = calcular_total(preco, quantidade)
print (total)