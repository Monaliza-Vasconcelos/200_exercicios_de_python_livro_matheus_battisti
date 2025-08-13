def entrada_de_dados():
    n = int(input('Digite um número inteiro: ')) #Lendo um número inteiro
    n1 = float(input('Digite um número decimal: '))#Lento um número decimal
    soma = n+n1
    print(f'A soma entre {n} e {n1} é {soma}')


if __name__ == "__main__":
    entrada_de_dados()