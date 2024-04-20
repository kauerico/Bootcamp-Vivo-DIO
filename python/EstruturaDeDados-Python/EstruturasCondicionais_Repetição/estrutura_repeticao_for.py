# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# exemplo utilizando um interavel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()


# exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")