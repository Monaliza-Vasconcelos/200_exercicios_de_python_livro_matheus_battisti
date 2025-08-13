def tipos():
    #Variáveis recebem os valores
    numero_inteiro = (2) #int
    numero_ponto_flutuante = (5.4) #float
    strings = ('Olá, muito prazer!') #string
    booleanos = (False) #booleano(True or False)
    """
    -> print
    É exibido na tela de que tipo são (float(ponto flutuante) / int(inteiro) 
    / str(string) / bool(booleano)
    """
    print(type(numero_inteiro))
    print(type(numero_ponto_flutuante))
    print(type(strings))
    print(type(booleanos))

if __name__ == "__main__":
    tipos()