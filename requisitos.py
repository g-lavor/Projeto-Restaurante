from abc import ABC, abstractmethod

class Requisitos(ABC):
    def __init__(self, valor):
        # Classe abstrata que define a estrutura para os requisitos de pesquisa.
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    @abstractmethod
    def verificar(self, restaurante):
        pass

class NomeRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se o nome do restaurante atende aos critérios.
        valor = self.valor.lower().replace(" ", "")
        restaurante_nome = restaurante.nome.lower().replace(" ", "")
        prefixo = valor
        return restaurante_nome.startswith(prefixo)

class CulinariaRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se o tipo de culinária do restaurante atende aos critérios.
        return self.valor.lower() == restaurante.culinaria.lower()

class ClassificacaoRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se a classificação do restaurante atende aos critérios.
        return restaurante.classificacao >= int(self.valor)

class DistanciaRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se a distância do restaurante atende aos critérios.
        return restaurante.distancia <= int(self.valor)

class PrecoRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se o preço do restaurante atende aos critérios.
        return restaurante.preco <= float(self.valor)