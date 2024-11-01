class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario  # Atributo de salário protegido

    def get_salario(self):
        return self.__salario

    def aumentar_salario(self, aumento):
        if aumento > 0:
            self.__salario += aumento

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Salário: R${self.get_salario():.2f}"
