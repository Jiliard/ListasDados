import csv


class Indexador:
    def __init__(self):
        self.index_todos = []
        self.index_curso = {}
        self.index_sexo = {}
        self.index_iaa = []
        self.indices_db = "Indices.csv"

    def setar_indices(self, dados):
        for dado in dados:
            self.indexar(dado)
    
    def indexar(self, elemento):
        elemento.matricula = str(elemento.matricula)
        self.index_todos.append(elemento.matricula)
        self._adicionar_a_index(self.index_curso, elemento.curso, elemento.matricula)
        self._adicionar_a_index(self.index_sexo, elemento.sexo, elemento.matricula)
        self.index_iaa.append(elemento.matricula)
    
    def remover(self, elemento):
        self.index_todos.remove(elemento.matricula)
        self._remover_de_index(self.index_curso, elemento.curso, elemento.matricula)
        self._remover_de_index(self.index_sexo, elemento.sexo, elemento.matricula)
        self.index_iaa.remove(elemento.matricula)
    
    def _adicionar_a_index(self, index, chave, matricula):

        # caso não tenha aquela categoria
        if chave not in index:
            index[chave] = []

        index[chave].append(matricula)
    
    def _remover_de_index(self, index, chave, matricula):
        if chave in index:
            index[chave].remove(matricula)

            #se não tiver mais itens exclui a categoria
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
    
    def pegar_todos_indices(self):
      return self.index_todos
    
    def pegar_maior_indice(self):
        return self.index_todos[-1]