class Veiculos():
    """
    Essa é a classe veiculos, Está classe é utilizada para instanciar novos veiculos
    """
    def __init__(self, cor, tipo_combustivel, potencia):
        self.__cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self.__qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0
        self._libras = 0

    def __del__(self):
        print('O objeto foi removido da memoria. :)')

    def abastecer(self, qtd_combustivel):
        """
        O metodo abastecer recebe como parametro a quantidade e incrementa no atributo QTD_COMBUSTIVEl do objeto
        """
        self.__qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.__is_ligado:
            return f'O veiculo foi está ligado'
        else:
            self.__is_ligado = True
            return f'O veiculo esta ligado'

    def desligar(self):
        if self.__is_ligado:
            self.__is_ligado = False
            return f'O veiculo foi desligado'
        else:
            return f'Está desligado'
    
    def acelerar(self, velocidade=10):
        if self.__is_ligado:
            self.__velocidade += velocidade
        else:
            print('Motor desligado')