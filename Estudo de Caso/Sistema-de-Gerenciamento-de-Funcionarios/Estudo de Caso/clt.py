from funcionario import Funcionario 

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, cpf, salario_base, bonus):
        super().__init__(nome, cpf, salario_base)
        self.bonus = bonus
    
    def calcular_salario(self):
        return self.get_salario_base() + self.bonus