from funcionario import Funcionario 

class Estagiario(Funcionario):
    def __init__(self, nome, cpf, bolsa, desconto):
        super().init__(nome, cpf, bolsa)
        self.desconto = desconto

    def calcular_salario(self):
        return self.get_salario_base() - self.desconto