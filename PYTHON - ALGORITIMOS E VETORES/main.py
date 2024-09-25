#Indice do vetor
# 0 | 1 | 2 | 3 | 4
# Valores armazenados
# 5 | 2 | 4 | 6 | 1

numeros = list()
tamanho = int(input('digite o tamanho do vetor: '))

for i in range(tamanho):
    # 0 até o valor declarado em tamanho
    valor = int(input(f'Digite o número do vetor ma posição {i}: '))
    numeros.append(valor)
print("vetor: ", numeros)
print('Posição do indice 1: ', numeros[1])

# BUSCA LINEAR
numero_pesquisar = int(input('Digite o valor a ser pesquisado no vetor: '))
posicao_resultado = -1
for i in range(tamanho):
    # 0 até o valor declarado em tamanho
    if numeros[i] == numero_pesquisar:
        posicao_resultado = i
        break
if posicao_resultado < 0:
    print('Elemento não encontrado')
else:
    print(f'Elemento encontrado no indice {posicao_resultado}')
# FIM BUSCA LINEAR