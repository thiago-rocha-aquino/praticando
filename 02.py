#Faça um algoritmo que leia o nome,
#  o sexo e o estado civil de uma pessoa.
#  Caso sexo seja “F” e estado civil seja “CASADA”,
#  solicitar o tempo de casada (anos).
nome = input("digite um o seu nome")
sexo = input("digite a seu sexo, se for feminino F, e se for masculino M")
estado_civil = input("digite o estado civil")
if(sexo == "f")or(estado_civil == "casada"):
    tempo_casada = int(input("digite o tempo de casada em anos"))
    print("o tempo de casada é: ", tempo_casada,"anos")