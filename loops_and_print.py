def enumerate_list(list):
    lista1 = []
    for posicion,elemento in enumerate(list):
        if elemento != "":
            largo = len(lista1)
            lista1.append(f"{largo}. {elemento}")
    return lista1
    

def enumerate_backwards(list):
    lista1 = []
    for posicion, elemento in enumerate(list):
        if elemento != "":
            largo = len(lista1)
            lista1.append(f"{largo}. {elemento[::-1]}")
    return lista1
    
