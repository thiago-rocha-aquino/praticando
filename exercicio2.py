#2.Elaborar um programa que em Python que receba um valor em real,
#a cotação do dolar. O programa devera converter o valor em dólares para real.
#Devera apresentar: o valor em reais, a cotação e o valor convertido.

valor_real = float(input("digite o valor em reais "))
cotacao = float(input("digite o valor da cotação "))
conv = valor_real/cotacao
print("valor em reais é: ", valor_real,"|", "cotação: ", cotacao, "|", "valor convertido em dolar: ", conv)
