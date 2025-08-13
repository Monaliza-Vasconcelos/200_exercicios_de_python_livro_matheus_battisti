def conversao_de_tipos():
    n = 5.6 
    conversao_int = int(n)#Convertendo float para int
    print(f'Valor float {conversao_int}')
    print(type(conversao_int))
    f = float(5) #Convertendo int para float
    print(f)
    print(type(f))

    #Duas formas diferentes, a primeira guarda o valor como float e depois converte
    #A segunda já converte diretamente
if __name__== "__main__":
    conversao_de_tipos()