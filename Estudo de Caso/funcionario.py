class Funcionario:
    def __init__(self, nome, cpf, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base
    
    # GETTERS
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_salario_base(self):
        return self.__salario_base
    
    # SETTERS com validação
    def set_nome(self, nome):
        self.__nome = nome  
    
    def set_cpf(self, cpf):
        if cpf == "":
            print("CPF não pode ser vazio!")
        else:
            self.__cpf = cpf
    
    def set_salario_base(self, salario):
        if salario < 0:
            print("Salário não pode ser negativo!")
        else:
            self.__salario_base = salario
        
    def exibir_dados(self):
        print(f"Nome: {self.__nome} | CPF: {self.__cpf}")

    def calcular_salario(self):
        return self.__salario_base