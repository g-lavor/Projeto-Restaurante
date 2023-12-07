import csv
from abc import ABC, abstractmethod

class Restaurante:
    def __init__(self, name, customer_rating, distance, price, cuisine_id):
        self.__nome = name
        self.__classificacao = int(customer_rating)
        self.__distancia = int(distance)
        self.__preco = int(price)
        self.__culinaria = cuisine_id

    # Métodos getter para acessar os atributos privados
    @property
    def nome(self):
        return self.__nome
    @property
    def classificacao(self):
        return self.__classificacao
    @property
    def distancia(self):
        return self.__distancia
    @property
    def preco(self):
        return self.__preco
    @property
    def culinaria(self):
        return self.__culinaria

class Requisitos(ABC):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    @abstractmethod
    def verificar(self, restaurante):
        pass

class ClassificacaoRequisitos(Requisitos):
    def verificar(self, restaurante):
        return restaurante.classificacao >= int(self.valor)

class DistanciaRequisitos(Requisitos):
    def verificar(self, restaurante):
        return restaurante.distancia <= int(self.valor)

class PrecoRequisitos(Requisitos):
    def verificar(self, restaurante):
        return restaurante.preco <= float(self.valor)

class PesquisaRestaurante:
    def __init__(self, restaurantes):
        self.__restaurantes = restaurantes

    def realizar_pesquisa(self, *requisitos):
        resultados = self.__restaurantes[:]
        for requisito in requisitos:
            resultados = [restaurante for restaurante in resultados if requisito.verificar(restaurante)]
        resultados.sort(key=lambda r: (r.distancia, -r.classificacao, r.preco))
        return resultados[:5]

def carregar_dados_csv(arquivo):
    with open(arquivo, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dados = [dict(row) for row in reader]
    return [Restaurante(**restaurante) for restaurante in dados]

def realizar_pesquisa_com_usuario():
    # Carregar dados do arquivo CSV
    restaurantes = carregar_dados_csv('restaurants.csv')

    # Criar instância da classe de Pesquisa
    pesquisa = PesquisaRestaurante(restaurantes)

    # Perguntar ao usuário como eles querem pesquisar
    print('Como deseja realizar a pesquisa ?\n1 - Distancia\n2 - Classificação\n3 - Preço\n4 - Tudo')
    escolha = int(input())

    # Dependendo da escolha do usuário, perguntar o valor específico para o critério e realizar a pesquisa apropriada
    if escolha == 1:
        distancia = int(input('Qual a distância máxima (em km)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(DistanciaRequisitos(distancia))
    elif escolha == 2:
        classificacao = int(input('Qual a classificação mínima (de 1 a 5)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(ClassificacaoRequisitos(classificacao))
    elif escolha == 3:
        preco = float(input('Qual o preço máximo (em reais)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(PrecoRequisitos(preco))
    elif escolha == 4:
        distancia = int(input('Qual a distância máxima (em km)? '))
        classificacao = int(input('Qual a classificação mínima (de 1 a 5)? '))
        preco = float(input('Qual o preço máximo (em reais)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(DistanciaRequisitos(distancia), ClassificacaoRequisitos(classificacao), PrecoRequisitos(preco))

    # Exibir resultados da pesquisa
    print("Resultados da Pesquisa:")
    for restaurante in resultado_pesquisa:
        print('Nome:',restaurante.nome, '\nDistância:',restaurante.distancia, '\nClassificação:',restaurante.classificacao, '\nPreço:',restaurante.preco, '\nCulinaria:',restaurante.culinaria)
        print()
        print()

# Iniciar a pesquisa com o usuário
realizar_pesquisa_com_usuario()
