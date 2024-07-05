
import csv
import os
import time
from classes.Elemento import Elemento
from classes.Indexador import Indexador


class BaseDados:

    def __init__(self, indexador):
        self.indexador = indexador
        self.proxima_matricula = 1
        self.disco = 'Disco.csv'
        self.temp_disco = 'Temp.csv'
    
    def carregar_dados_iniciais(self):
        dados_iniciais = [
            (1, 'Aurelius', 'Engenharia', 8.5, 'Feminino'),
            (2, 'Beatrix', 'Medicina', 9.2, 'Feminino'),
            (3, 'Cassiopeia', 'Direito', 7.8, 'Masculino'),
            (4, 'Dashiell', 'Engenharia', 7.0, 'Feminino'),
            (5, 'Eduardo', 'Sistemas', 9.5, 'Masculino'),
            (6, 'Finnian', 'Direito', 8.2, 'Feminino'),
            (7, 'Gwendolyn', 'Engenharia', 8.0, 'Masculino'),
            (8, 'Hugo', 'Direito', 7.5, 'Feminino'),
            (9, 'Isolde', 'Medicina', 8.7, 'Masculino'),
            (10, 'Jiliard', 'Sistemas', 9.4, 'Masculino'),
        ]

        elementos = []

        for dado in dados_iniciais:
            elemento = Elemento(*dado)
            elementos.append(elemento)

        self.adicionar_varios_elementos(elementos, True)

        print("\n10 estudantes adicionados!")
        time.sleep(1)
        
    def adicionar_elemento(self, elemento, silencioso: bool):
        #acessa o disco
        print("Acesso parcial do disco")
        time.sleep(1)

        elemento.matricula = self.proxima_matricula
        self.proxima_matricula += 1
        
        with open(self.disco, mode='a', newline='') as file:

            elementoString = [elemento.matricula, elemento.nome, elemento.curso, elemento.iaa, elemento.sexo]
            writer = csv.writer(file)
            writer.writerow(elementoString)
        
        self.indexador.indexar(elemento)

        if(not silencioso):
            print()
            print(f"Estudante adicionado com Número de Matrícula {elemento.matricula}!")
            time.sleep(1)

    def adicionar_varios_elementos(self, elementos, silencioso: bool):
        #acessa o disco
        print("Acesso parcial do disco")
        time.sleep(1)

        for elemento in elementos:
            elemento.matricula = self.proxima_matricula
            self.proxima_matricula += 1
            self.indexador.indexar(elemento)
        
        
        with open(self.disco, mode='a', newline='') as file:

            for elemento in elementos:
                elementoString = [elemento.matricula, elemento.nome, elemento.curso, elemento.iaa, elemento.sexo]
                writer = csv.writer(file)
                writer.writerow(elementoString)

        if(not silencioso):
            print()
            print(f"Estudante adicionado com Número de Matrícula {elemento.matricula}!")
            time.sleep(1)

    def remover_elemento(self, matricula):
        #acessa o disco
        print("Acesso parcial do disco")
        time.sleep(1)

        if str(matricula) not in self.indexador.pegar_todos_indices():
            print()
            print(f"O Número de Matrícula {matricula} não existe. O estudante não foi removido!")
            time.sleep(1)
            return
            
            
        with open(self.disco, mode='r', newline='') as arquivo_original, \
            open(self.temp_disco, mode='w', newline='') as arquivo_temporario:

            reader = csv.reader(arquivo_original)
            writer = csv.writer(arquivo_temporario)

            for linha in reader:
                if not linha[0].isdigit() or int(linha[0]) != matricula:
                    # Escrever a linha no arquivo temporário se não começar com a matricula
                    writer.writerow(linha)
                else:
                    elemento_removido = Elemento(matricula=linha[0], nome=linha[1],curso=linha[2],iaa=linha[3],sexo=linha[4])

        # Substituir o arquivo original pelo arquivo temporário
        os.remove(self.disco)
        os.rename(self.temp_disco, self.disco)
            

        self.indexador.remover(elemento_removido)
        print()
        print(f"Estudante com Número de Matrícula {matricula} removido!")
        time.sleep(1)

    
    def pegar_dados_disco(self, matriculas):
        #acessa o disco
        print("Acesso parcial do disco")
        time.sleep(1)
         
        dados = []

        with open(self.disco, mode='r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha[0] in matriculas:
                    elemento = Elemento(matricula=linha[0], nome=linha[1],curso=linha[2],iaa=linha[3],sexo=linha[4])
                    dados.append(elemento)
        return dados
    
    def pegar_todos_dados(self):
        #acessa o disco
        print("Acesso total do disco")
        time.sleep(1)
         
        dados = []

        with open(self.disco, mode='r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                elemento = Elemento(matricula=linha[0], nome=linha[1],curso=linha[2],iaa=linha[3],sexo=linha[4])
                dados.append(elemento)
        return dados
    
    def pegar_indices(self):
        return self.indexador.pegar_todos_indices()

    def setar_proximo_indice(self, indice):
        self.proxima_matricula = indice