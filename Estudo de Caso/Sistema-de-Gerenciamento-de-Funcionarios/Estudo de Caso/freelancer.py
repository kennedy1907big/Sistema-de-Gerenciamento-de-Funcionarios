from funcionario import Funcionario

class Freelancer(Funcionario):
    def __init__(self, nome, cpf, valor_projetos, qtd_projetos):
        super(). __init__(nome, cpf, 0)
        self.valor_projetos = valor_projetos
        self.qtd_projetos = qtd_projetos

    def calcular_salario(self):
        return self.valor_projetos * self.qtd_projetos