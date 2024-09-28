#Atividade - Loja de Roupas
#ma loja de roupas precisa de um programa que ajude a calcular o valor final da venda de produtos. Existem algumas regras que precisam ser respeitadas na venda de um produto:
 
#1 – A vista – 10% de desconto, caso o valor da venda seja maior que 500 15%, caso seja maior que 1000, 20% de desconto;
#2 – A prazo – A venda pode ser parcelada em até 18x. Caso seja parcelado em mais do que 10x possui juros:
#Apenas compras com mais de 800 reais podem ser parceladas acima de 5x;
#Juros:
 #         1 – 11 vezes: 5% de juros ao mês.
  #        2 – 12 vezes: 6.5% de juros ao mês.
   #       3 – 13 vezes: 7% de juros ao mês.
    #      4 – 14 vezes: 9% de juros ao mês.
     #     5 – 15 vezes: 9.5% de juros ao mês.
     #     6 – 16 vezes: 10% de juros ao mês.
   #       7 – 17 vezes: 11.3% de juros ao mês.
    #      8 – 18 vezes: 12% de juros ao mês. 

ValorCompra = float(input("qual o valor da compra em R$?"))
print("-"*20)
print("1- A vista")
print("2- A prazo")
print("-"*20)
FormaPagamento = input("qual forma de pagamento?")
print("-"*20)
if FormaPagamento == "1":
  print("-"*20)
  print("forma escolinda foi a vista")
print("-"*20)
if ValorCompra <= 500:
  print("-"*20) 
  print(f"seus valor de compra foi de {ValorCompra - (ValorCompra * 0.1)}")
  print("-"*20)
elif ValorCompra <= 999:
  print(f"seus valor de compra foi de {ValorCompra - (ValorCompra * 0.15)}")
  print("-"*20)
elif ValorCompra >1000:
  print(f"seus valor de compra foi de {ValorCompra - (ValorCompra * 0.2)}")
  print("-"*20)



















# elif FormaPagamento == "2":
#   print("forma escolhida foi a prazo")
# else:
#   print("forma invalida")

# print("-"*20)
# print("1- sim")
# print("2- não")
# print("-"*20)
# correçao = input("sua escolha esta correta?")

# if correçao == "1":
#   print("ok vamos proseguir")

# elif correçao == "2":
#   print("ok")

# print("-"*20)
# print("1- sim")
# print("2- não")
# print("-"*20)

# correçao = input("sua escolha esta correta?")

# if correçao == "1":
#   print("ok vamos proseguir")






