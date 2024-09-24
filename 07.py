#Faça um algoritmo que leia uma variável e some 5,
# caso seja par ou some 8, caso seja ímpar, imprimir o resultado desta operação.
var = int(input("digite um valor "))
if(var%2== 0):
    resul = var + 5
    print("resultado é: ", resul)
else:
    resul = var + 8
    print("resultado é: ", resul)    