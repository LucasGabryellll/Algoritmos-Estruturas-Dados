from LISTAS.Simplismente_encadiada.Lista import Lista

lista = Lista()
print(lista)
lista.add('10')
lista.add('20')
lista.add('30')
print(lista)
lista.addIndex(0, '11')
lista.addIndex(3, '50')
print(lista)

print(lista.getIndex(0))
obj = lista.getIndex(3)
print('----------')
print(lista[0])
print(lista[1])
print(lista[2])
print('----------')
print(lista)
lista[1] = 'heldon'
lista[0] = 'jose'
#FAZ EM CASA
lista[-1] = 'jose'
print(lista)