from sistema import Sistema
from clt import FuncionarioCLT
from freelancer import Freelancer
from estagiario import Estagiario

sistema = Sistema()

# 5 de cada tipo (pré-cadastro)
for i in range(1, 6):
    sistema.adicionar(FuncionarioCLT(f"CLT{i}", "123", 2000, 500))
    sistema.adicionar(Freelancer(f"Free{i}", "456", 300, 5))
    sistema.adicionar(Estagiario(f"Est{i}", "789", 1000, 100))

while True:
    print("\n1 - Listar")
    print("2 - Folha total")
    print("3 - Sair")

    op = input("Escolha: ")

    if op == "1":
        sistema.listar()
    
    elif op == "2":
        sistema.folha_total()
    
    elif op == "3":
        break