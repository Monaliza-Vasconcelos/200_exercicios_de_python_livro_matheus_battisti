def operacoes_aritmeticas():
    n1 = 3
    n2 = 2

    #Incluindo diretamente no print
    print(f'A soma de {n1} e {n2} é: {n1+n2}')
    print(f'Subtraindo {n1} por {n2} temos: {n1 - n2}')
    print(f'Multiplicando {n1} por {n2} temos: {n1*n2}')
    print(f'Dividindo {n1} por {n2} temos {n1/n2}')
    print(f'Módulo de {n1} por {n2} é: {n1%n2}')

    #Criando variáveis para guardar valores
    soma = n1 + n2
    subtração = n1 - n2
    multiplicação = n1 * n2
    divisão = n1 / n2 #Divisão inteira
    módulo = n1 % n2 #Resto da divisão

    print(f'Soma: {soma}')
    print(f'Subtração: {subtração}')
    print(f'Multiplicação: {multiplicação}')
    print(f'Divisão: {divisão}')
    print(f'Módulo: {módulo}')


if __name__ == "__main__":
    operacoes_aritmeticas()