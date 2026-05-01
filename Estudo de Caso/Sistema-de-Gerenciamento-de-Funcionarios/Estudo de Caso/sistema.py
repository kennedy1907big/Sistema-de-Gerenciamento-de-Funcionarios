class Sistema:
    def __init__(self):
        self.funcionarios = []

    def adicionar(self, func):
        self.funcionarios.append(func)

    def listar(self):
        for f in self.funcionarios:
            f.exibir_dados()
            print(f"Salário: {f.calcular_salario()}")
            print("-" * 30)

    def folha_total(self):
        total = 0
        for f in self.funcionarios:
            total += f.calcular_salario()
        print(f"Folha total: {total}")