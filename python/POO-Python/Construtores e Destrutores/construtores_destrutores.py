class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor  = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe ....")

    def falar(self):
        print("Auau")

def criar_cachoroo():
    c = Cachorro("Pitu", "Azul", False)
    print(c.nome)

c = Cachorro("Pitu", "Azul")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")


# criar_cachoroo()