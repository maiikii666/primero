manzana= True and (True or False)
banana= (False and True) and False
uvas= not(banana and manzana)
manzana=(uvas or banana) and manzana

manzana==False
banana==False
uvas==True

print(manzana)
print(banana)
print(uvas)