import veiculo

class Moto(veiculo.Veiculos):
    def __init__(self, cor, tipo_combustivel, potencia, carenagem:bool):
        super().__init__(cor, tipo_combustivel, potencia)
        self.carenagem = carenagem

    def empinar(self):
        print(f'empinandoooooooo')