# Exemplo 01
while True:
	numero = int(input("Informe um número: "))
	
	if numero == 10:
		break
	
	print(numero)
	

# Exemplo 02
for numero in range(100):
	
    if numero == 10:
	    break
	
print(numero, end=" ")

print()


# Exemplo 03
for numero in range(100):
	
    if numero == 10:
	    continue
	
print(numero, end=" ")