var_global = str('Olá pessoal') #Variável global
def var_local():
    n = str('N') #Variável local
    print(f'A variável {n} é local, pois só poderá ser utilizada dentro da função')
    print(f'Já a variável global pode ser utilizada em todo o código, {var_global}')


if __name__ == "__main__":
    var_local()


print(f'Já a variável global pode ser utilizada em todo o código, {var_global}')

"""
    ->Caso adicione a variável n que está dentro da função aqui no programa principal
    vai retornar um NameError, pois a variável só vai existir enquanto a função estiver
    rodando...
"""

#teste