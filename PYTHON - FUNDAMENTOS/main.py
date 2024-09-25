from usuario import Usuario

continuar = 1
lista_usuarios = []
while continuar == 1:
    try:
        nome = input('Insira o nome: ')
        idade = int(input('Insira a idade: '))
        sobrenome = input('Insira o sobrenome: ')
        
        usuario = Usuario(nome, idade, sobrenome)
        lista_usuarios.append(usuario)
        print(f'Olá {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}')

        continuar = int(input('\nPara criar um novo usuario digite 1: '))
    except ValueError:
        print('Você deve informar um número valido')
else:
    print('\nLista de usuarios cadastrados')
    for i in lista_usuarios:
        print(f'Nome completo {i.nome} {i.sobrenome} - idade {i.idade}')
    print('O loop entrou no else')
