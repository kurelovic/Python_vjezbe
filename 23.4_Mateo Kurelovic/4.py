def jedinstveni_elementi(lista):
    for element in lista:
        lista.sort
        if lista.count(element)>1:
            lista.remove(element)
    return lista
print(jedinstveni_elementi([1,2,2,2,4,5,5,5,4,4]))
