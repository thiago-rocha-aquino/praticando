#Encontrar o dobro de um número caso ele seja positivo
# e o seu triplo caso seja negativo, imprimindo o resultado.
num = int(input("digite um número: "))
if(num >=0):
    num=2*num
    print(num)
else:
    num=3*num 
    print(num)