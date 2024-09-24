#Faça um algoritmo que leia dois valores inteiros A e B se os valores
# forem iguais deverá se somar os dois, caso contrário multiplique A por B.
# Ao final de qualquer um dos cálculos deve-se atribuir o resultado para
# uma variável C e mostrar seu conteúdo na tela.
a = int(input("digite o valor para a "))
b = int(input("digite o valor para b"))
if(a == b):
    resul = a+b
    print("a soma do valor a e b é: ", resul)
else:
    resul = a*b
    print("a multiplicação do valor a e b é: ", resul) 
c = resul
print("o valor da variavel c é: ",c)       