from classes.BaseDados import BaseDados
from classes.Indexador import Indexador
from classes.Interface import Interface


if __name__ == "__main__":
    indexador = Indexador()
    base_dados = BaseDados(indexador)
    interface = Interface(base_dados)

    indexador.setar_indices(base_dados.pegar_todos_dados())
    #Verifica se tem algum dado
    if indexador.index_todos:
        base_dados.setar_proximo_indice(int(indexador.pegar_maior_indice()) + 1)
    interface.menu()