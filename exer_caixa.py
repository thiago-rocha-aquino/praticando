# um programa para um caixa eletrônico. O programa deve receber como entrada 
#um valor inteiro em reais e apresentar quantas cédulas serão fornecidas para
#formar este montante(cédulas de 100,50, 20, 10, 2 reias)

valor = int(input("digite o valor a sacar: "))
valororig = valor
n2 = n5 = n10 = n20 = n50 = n100 = 0
if(valor < 2)or(valor == 3):
    print("valor inválido")
else:
    #tratando os valores que terminam em 11, 13, 6 e 8
    if(valor % 10 == 1):
        n2 = 3
        n5 = 1
        valor = valor - 11
    elif(valor % 10 == 3):
        n2 = 4
        n5 = 1 
        valor = valor - 13
    elif(valor % 10 == 6):
        n2 = 3
        n5 = 0
        valor = valor - 6
    elif(valor % 10 == 8):
        n2 = 4
        n5 = 0
        valor = valor - 8
    #tratando os valores das notas de 100 a 2 reais
    if(valor >=100):
        n100 = valor // 100
        valor = valor % 100
    if(valor >=50):
        n50 = valor // 50
        valor = valor % 50
    if(valor >=20):
        n20 = valor // 20
        valor = valor % 20
    if(valor >=10):
        n10 = valor // 10
        valor = valor % 10
    if(valor >=5):
        n5 = valor // 5
        valor = valor % 5
    if(valor >=2):
        n2 = valor // 2
        valor = valor % 2
    else:
        print("opção inválida!!")
print("valor a sacar é: ", valororig) 
print("notas de 100 - ",n100,"|",
      "notas de 50 - ", n50,"|",
      "notas de 20 - ", n20,"|",
      "notas de 10 - ", n10,"|,"
      "notas de 5 - ", n5,"|",
      "notas de 2 - ", n2,"|")      

