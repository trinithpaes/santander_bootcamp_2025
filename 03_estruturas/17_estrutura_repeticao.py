texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")
print()  # adicionar uma quebra de linha

# Exemplo utilizando um iterável
for numero in range(0, 11):
	print(numero, end=" ")
else:
    print()  # adicionar uma quebra de linha

# Exemplo utilizando a função buillt-in range
for numero in range(0, 51, 5):
	print(numero, end=" ")
