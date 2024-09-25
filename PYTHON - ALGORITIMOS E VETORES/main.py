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


# SELECTION SORT
#Indice do vetor
# 0 | 1 | 2 | 3 | 4
# Valores armazenados
# 5 | 2 | 4 | 6 | 1
# Apos Selection sort
# 1 | 2 | 4 | 5 | 6

for i in range(tamanho):
    indice_menor = i
    for x in range(int(i + 1), tamanho):
        if numeros[x] < numeros[indice_menor]:
            indice_menor = x
    temp = numeros[indice_menor]
    numeros[indice_menor] = numeros[i]
    numeros[i] = temp
# FIM SELECTION SORT

# BUSCA BINARIA
# Indie do vetor
# 1 | 2 | 4 | 5 | 6

resultado = -1
inicio = 0
fim = tamanho-1
meio = 0
alvo = int(input(''))
while inicio <= fim:
    meio = int((inicio + fim) / 2)
    if (numeros[meio] < alvo):
        inicio = meio + 1
    elif (numeros[meio]>alvo):
        fim = meio - 1
    else:
        resultado = meio



# FIM BUSCA BINARIA