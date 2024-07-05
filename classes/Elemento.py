from dataclasses import dataclass


@dataclass
class Elemento:
    def __init__(self, matricula, nome, curso, iaa, sexo):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.iaa = iaa
        self.sexo = sexo