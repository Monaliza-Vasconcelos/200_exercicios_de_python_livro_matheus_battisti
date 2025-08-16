class Tipos_de_variaveis():
    #Variável global
    varglobal = 'Helena'
    def mostrar_valores(self):
        nome = 'Carla' #Variável de escopo local
        print(f'Valor da variável global: {self.varglobal}')
        print(f'Valor da variável local: {nome}')


if __name__ == "__main__":
    variaveis = Tipos_de_variaveis()
    variaveis.mostrar_valores()










        

        
