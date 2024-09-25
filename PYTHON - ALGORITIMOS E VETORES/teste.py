class Produto:
    def __init__(self, id, nome, quantidade):
        self.__id = id
        self.__nome = nome
        self.__quantidade = quantidade
        
    @property
    def id(self):
        return self.__id
    
    @property
    def nome(self):
        return self.__nome
        
    @property
    def quantidade(self):
        return self.__quantidade
        
    @id.setter
    def id(self, id):
        self.__id = id
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade
        
if __name__ == '__main__':
    
    t = int(input())
    produtos = list()
    for i in range(t):
        id, nome, quantidade = input().split(' ')
        
        produto = Produto(int(id), nome, int(quantidade))
        produtos.append(produto)
        
    for i in range(len(produtos)):
        indice = i
        for j in range(i + 1, len(produtos)):
            if (produtos[j].quantidade > produtos[indice].quantidade):
                indice = j
            elif (produtos[j].quantidade == produtos[indice].quantidade):
                if (produtos[j].nome < produtos[indice].nome):
                    indice = j
                elif (produtos[j].nome == produtos[indice].nome):
                    if(produtos[j].id < produtos[indice].id):
                        indice = j
        
        temp = produtos[i]
        produtos[i] = produtos[indice]
        produtos[indice] = temp
    
    for p in produtos:
        print(p.nome)