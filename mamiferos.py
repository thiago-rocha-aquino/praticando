classes = int(input("digite 1, 2 ou 3"))
if(classes == 3):
    print("você escolheu repteis")
    carat = int(input("digite 1, com casco, digite 2, carnivoro, digite 3, sem patas"))
    if(carat == 1):
        print("você escolheu tartaruga")
    elif(carat == 2):
        print("você escolheu crocodilo")  
    elif(carat == 3):
        print("você escolheu cobra")   
    else:
        print("opção invalida")  
elif(classes == 2):
    print("você escolheu aves") 
    carat = int(input("digite 1, não voadores, digite 2, nadadores, digite 3, rapina"))
    if(carat == 1):
        print("você escolheu não voadores")
        ambiente = int(input("digite 1, tropical, digite 2, polar"))
        if(ambiente == 1):
            print("você escolheu avetruz")
        elif(ambiente == 2):
            print("você escolheu pinguim")
        else:
            print("opção invalida") 
    elif(carat == 2):
        print("você escolheu pato") 
    elif(carat == 3):
        print("você escolheu águia")
    else:
        print("opção invalida")                               
elif( classes == 1):
    print("você escolheu mamifero")
    carat = int(input("digite 1, nadadora"))
    if( carat == 1):
        print("você escolheu baleia")
    else:
        print("opção invalida")    


