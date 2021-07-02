a=[1,2,3,4,5]
print(a)

a.append([5,6,7,8]) # Solo se puede usar para meter un elemento
print(a)

a.extend([9,10,11]) #Fusiona las listas
print(a)

a.remove(2) #Remueve el valor que se quiera borrar
print(a)

a.remove(a[2]) ###Remueve el valor indicado por el índice, puede ser una lista entera dentro de la lista

a.reverse() ###Reversa y cambia la lista.

print(a.index(3)) ##El indice donde esta un valor

print(a.count(5)) ### Cuantas veces está el valor en la lista, pero solo en la capa que uno pregunte

print(a)