import time
from classes.BaseDados import BaseDados
from classes.Elemento import Elemento


class Interface:
    def __init__(self, base_dados):
        self.base_dados = base_dados

        
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Carregar 10 alunos iniciais")
            print("2. Adicionar Elemento")
            print("3. Remover Elemento")
            print("4. Buscar Simples")
            print("5. Buscar Composta")
            print("6. Listar Todos os Elementos")
            print("7. Ver todas os indices (sem acesso ao disco)")
            print("8. Sair")
            opcao = input("Escolha uma opcao: ")
            
            if opcao == '1':
                self.base_dados.carregar_dados_iniciais()
            elif opcao == '2':
                self.adicionar_elemento()
            elif opcao == '3':
                self.remover_elemento()
            elif opcao == '4':
                self.buscar_simples()
            elif opcao == '5':
                self.buscar_composta()
            elif opcao == '6':
                self.listar_todos_elementos()
            elif opcao == '7':
                self.listar_indices()
            elif opcao == '8':
                break
    
    def adicionar_elemento(self):
        nome = input("Nome: ")
        curso = input("Curso: ")
        iaa = float(input("IAA: "))

        while True:
            print("1. Masculino")
            print("2. Feminino")
            aux = input("Sexo: ")

            if aux == "1":
                sexo = "Masculino"
                break
            elif aux == "2":
                sexo = "Feminino"
                break
            print("Sexo incorreto!")

        elemento = Elemento(None, nome, curso, iaa, sexo)  # Matrícula será atribuída automaticamente
        self.base_dados.adicionar_elemento(elemento, False)
    
    def remover_elemento(self):
        matricula = int(input("Número de Matrícula do estudante a ser removido: "))
        self.base_dados.remover_elemento(matricula)

    def buscar(self):
        while True:
            campo = input("Campo (curso, sexo, iaa): ")

            if campo == 'iaa':
                comparador = input("Comparador (menor, maior, igual): ")
                valor = float(input("IAA: "))
                break

            elif campo == 'sexo':
                comparador = None
                while True:
                    print("1. Masculino")
                    print("2. Feminino")

                    aux = input("Sexo: ")
                    if aux == "1":
                        valor = "Masculino"
                        break
                    elif aux == "2":
                        valor = "Feminino"
                        break
                    print("Sexo incorreto!")
                break

            elif campo == "curso":
                comparador = None
                valor = input("Curso: ")
                break

            else:
                print("Campo incorreto!")
        
        return campo, valor, comparador

    def buscar_simples(self):
        campo, valor, comparador = self.buscar()
        resultados = self.base_dados.indexador.busca_simples(campo, valor, comparador)
        self._exibir_resultados(resultados)
    
    def buscar_composta(self):
        print("Busca 1:")
        campo1, valor1, comparador1 = self.buscar()

        print("Busca 2:")
        campo2, valor2, comparador2 = self.buscar()

        resultados = self.base_dados.indexador.busca_composta(campo1, valor1, comparador1, campo2, valor2, comparador2)
        self._exibir_resultados(resultados)
    
    def _exibir_resultados(self, resultados):
        if resultados:
            for elemento in resultados:
                print(f"Matrícula: {elemento.matricula}, Nome: {elemento.nome}, Curso: {elemento.curso}, IAA: {elemento.iaa}, Sexo: {elemento.sexo}")
        else:
            print("Nenhum resultado encontrado.")

    def listar_todos_elementos(self):
        self.mostrarTabela(self.base_dados.pegar_todos_dados(), "Nenhum usuario!")

    def mostrarTabela(self, elementos, errorMessage=None):
        colunas = ["matricula", "nome", "curso", "iaa", "sexo"]
        tamColuna = [3, 13, 13, 4, 10]

        quant = sum(tamColuna)

        if elementos:
            for i in range(quant + 46):
                print("-", end='')
            
            print()

            for elemento in elementos:
                for j in range(5):
                    # Coluna 
                    dado = getattr(elemento, colunas[j])

                    print("| ", end='')
                    print(colunas[j] + ": ", end='')
                    print(dado, end='')
                    for k in range(tamColuna[j] - len(str(dado))):
                        print(" ", end='')
                    if(j==4):
                        print("|", end='')
                print()
            
            for i in range(quant + 46):
                print("-", end='')
    
        else:
            print()
            print(errorMessage)
            time.sleep(1)

    def listar_indices(self):
        indices = self.base_dados.pegar_indices()

        print("Indices: ")

        for indice in indices:
            print(indice, end=", ")

        print()