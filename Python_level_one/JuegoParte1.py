from random import randint
def entregaListaMaquina():
    return [randint(0, 9),randint(0, 9),randint(0, 9)]

def advinar(lista, listaMaq):
    salida = []
    for idx, numero in enumerate(lista):
        salida.append(checkNum(numero,listaMaq,idx))

    return salida

def checkNum(num, lista, pos):
    for idx, numMaq in enumerate(lista):
        if num == numMaq and pos == idx:
            return "Match"
            break
        elif num == numMaq:
            return "Close"
            break
    return "Nope"

listaMaquina = entregaListaMaquina()
listaBuscar = [1,2,3]
print("Lista a buscar")
print(listaBuscar)
print("Lista a maquina")
print(listaMaquina)
print(advinar(listaBuscar,listaMaquina))
