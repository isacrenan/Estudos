#criando classes 

class Pessoa:
    def __init__(self, nome, idade, curso, linguagem, carro):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.linguagem = linguagem
        self.carro = carro
                 
         
    def Estudar(self):
            print(f'{self.nome} está estudando Python')
    
    def Idade(self):
        print(f'{self.nome} tem {self.idade} anos')       
    
    def Carro(self):
        print(f'{self.nome} tem um {self.carro}') 
    
    def EstudarMaria(self):
            print(f'{self.nome} está estudando Java')


isac_renan =Pessoa(' Isac', 29, 'ADS', 'Python', 'Corsa')
maria_joana =Pessoa('Maria', 35, 'ADM', 'Java', 'GOL')


Pessoa.Estudar(isac_renan), Pessoa.Idade(isac_renan), Pessoa.Carro(isac_renan)

Pessoa.EstudarMaria(maria_joana), Pessoa.Idade(maria_joana), Pessoa.Carro(maria_joana)

