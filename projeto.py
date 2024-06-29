class Elemento:
    def __init__(self, matricula, nome, curso, iaa, sexo):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.iaa = iaa
        self.sexo = sexo


class BaseDados:
    def __init__(self):
        self.elementos = []
        self.indexador = Indexador()
        self.proxima_matricula = 1 
    
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
        for dado in dados_iniciais:
            self.adicionar_elemento(Elemento(*dado))
        
    def adicionar_elemento(self, elemento):
        elemento.matricula = self.proxima_matricula
        self.proxima_matricula += 1
        
        self.elementos.append(elemento)
        self.indexador.indexar(elemento)
        print(f"Estudante adicionado com Número de Matrícula {elemento.matricula}!")

    def remover_elemento(self, matricula):
        elemento = None
        
        for el in self.elementos:
            if el.matricula == matricula:
                elemento = el
                break
        
        if elemento is not None:
            self.elementos.remove(elemento)
            self.indexador.remover(elemento)
            print(f"Estudante com Número de Matrícula {matricula} removido!")

        else:
            print(f"O Número de Matrícula {matricula} não existe. O estudante não foi removido!")

    def listar_elementos(self):
        if self.elementos:
            for elemento in self.elementos:
                print(f"Matrícula: {elemento.matricula}, Nome: {elemento.nome}, Curso: {elemento.curso}, IAA: {elemento.iaa}, Sexo: {elemento.sexo}")
    
        else:
            print("Sem estudantes adicionados!")
        

class Indexador:
    def __init__(self):
        self.index_curso = {}
        self.index_sexo = {}
        self.index_iaa = []
    
    def indexar(self, elemento):
        self._adicionar_a_index(self.index_curso, elemento.curso, elemento)
        self._adicionar_a_index(self.index_sexo, elemento.sexo, elemento)
        self.index_iaa.append(elemento)
    
    def remover(self, elemento):
        self._remover_de_index(self.index_curso, elemento.curso, elemento)
        self._remover_de_index(self.index_sexo, elemento.sexo, elemento)
        self.index_iaa.remove(elemento)
    
    def _adicionar_a_index(self, index, chave, elemento):
        if chave not in index:
            index[chave] = []
        index[chave].append(elemento)
    
    def _remover_de_index(self, index, chave, elemento):
        if chave in index:
            index[chave].remove(elemento)
            if not index[chave]:
                del index[chave]
    
    def busca_simples(self, campo, valor, comparador=None):
        if campo == 'curso':
            return self.index_curso.get(valor, [])
        
        elif campo == 'sexo':
            return self.index_sexo.get(valor, [])
        
        elif campo == 'iaa':
            if comparador == 'menor':
                return [el for el in self.index_iaa if el.iaa < valor]
            elif comparador == 'maior':
                return [el for el in self.index_iaa if el.iaa > valor]
            elif comparador == 'igual':
                return [el for el in self.index_iaa if el.iaa == valor]
    
    def busca_composta(self, campo1, valor1, comparador1, campo2, valor2, comparador2):
        resultados1 = set(self.busca_simples(campo1, valor1, comparador1))
        resultados2 = set(self.busca_simples(campo2, valor2, comparador2))
        return resultados1.intersection(resultados2)


class Interface:
    def __init__(self):
        self.base_dados = BaseDados()
        
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Carregar Dados Iniciais")
            print("2. Adicionar Elemento")
            print("3. Remover Elemento")
            print("4. Buscar Simples")
            print("5. Buscar Composta")
            print("6. Listar Todos os Elementos")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")
            
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
                self.base_dados.listar_elementos()
            elif opcao == '7':
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
        self.base_dados.adicionar_elemento(elemento)
    
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


if __name__ == "__main__":
    interface = Interface()
    interface.menu()
