class Anagramas():
    def __init__(self, palavra01, palavra02):
        self.palavra01 = palavra01
        self.palavra02 = palavra02

    def sao_anagramas(self) -> str:
        qtd_letras_iguais = 0
        for i in self.palavra01:
            for x in self.palavra02:
                if i == x:
                    qtd_letras_iguais += 1
        if qtd_letras_iguais == len(self.palavra01):
            return('são palavras anagramas')
        
