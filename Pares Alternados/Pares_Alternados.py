m = int(input("Inserte primer número: "))
n = int(input("Inserte segundo número: "))
lista=[]
if m<n:
	while m<n-1:
		m+=1
		if m%2==0:
			lista.append(m)
elif n<m:
	while n<m-1:
		n+=1
		if n%2==0:
			lista.append(n)
listaz=[]

r=-1
if r<len(lista):
    while r<len(lista)-1:
    	r+=1
    	if r%2==0:
    		listaz.append(lista[r])		
adicion=sum(listaz)

print("Los números son: \n", listaz)
print("La suma de elementos de la lista es",adicion)
if len(listaz)!=1:
    print("Existen", len(listaz), "números pares alternados en la lista")
else:
    print("Existe un solo número par alternado en la lista")

input()