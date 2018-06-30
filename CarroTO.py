class CarroTO:

    def getAno(self):
        return self.ano

    def getMarca(self):
        return self.marca

    def getValor(self):
        return self.valor

    def getFoto(self):
        return self.foto

    def __init__(self, marca, ano, valor, foto):
        self.ano = ano
        self.marca = marca
        self.valor = valor
        self.foto = foto
