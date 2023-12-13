import csv
import pandas as pd
from functools import reduce
from abc import ABC, abstractmethod

class Restaurante:
    def __init__(self, name, customer_rating, distance, price, cuisine_id):
        self.__nome = name
        self.__classificacao = int(customer_rating)
        self.__distancia = int(distance)
        self.__preco = float(price)
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

class NomeRequisitos(Requisitos):
    def verificar(self, restaurante):
        return self.valor.lower() in restaurante.nome.lower()

class CulinariaRequisitos(Requisitos):
    def verificar(self, restaurante):
        return self.valor.lower() == restaurante.culinaria.lower()

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

def carregar_dados_csv(arquivo_restaurantes, arquivo_culinarias):
    with open(arquivo_restaurantes, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dados = [dict(row) for row in reader]

    # Carregar os dados do arquivo de culinária em um DataFrame do pandas
    df_culinaria = pd.read_csv(arquivo_culinarias)

    # Criar um dicionário a partir do DataFrame para mapear 'id' para 'name'
    mapeamento_culinaria = df_culinaria.set_index('id')['name'].to_dict()

    # Substituir os IDs de culinária pelos nomes correspondentes usando o dicionário de mapeamento
    for restaurante in dados:
        # Trocar o cuisine_id pelo nome correspondente usando o dicionário
        restaurante['cuisine_id'] = mapeamento_culinaria.get(int(restaurante['cuisine_id']), restaurante['cuisine_id'])
    return [Restaurante(**restaurante) for restaurante in dados]


def find_intersection(lists):
    if not lists:
        return []
    restaurant_sets = [set(stream) for stream in lists]
    intersection = reduce(lambda set1, set2: set1.intersection(set2), restaurant_sets)
    return list(intersection)

def realizar_pesquisa_com_usuario():
    # Carregar dados do arquivo CSV
    restaurantes = carregar_dados_csv('restaurants.csv', 'cuisines.csv')

    # Criar instância da classe de Pesquisa
    pesquisa = PesquisaRestaurante(restaurantes)

    
    # Perguntar ao usuário como eles querem pesquisar
    print('Como deseja realizar a pesquisa ?\n1 - Nome\n2 - Culinaria\n3 - Distancia\n4 - Classificação\n5 - Preço\n6 - Tudo')
    escolha = int(input())

    # Dependendo da escolha do usuário, perguntar o valor específico para o critério e realizar a pesquisa apropriada
    if escolha == 1:
        nome = input('Qual o nome do restaurante? ')
        resultado_pesquisa = pesquisa.realizar_pesquisa(NomeRequisitos(nome))
    elif escolha == 2:
        culinaria = input('Qual o tipo de culinária? ')
        resultado_pesquisa = pesquisa.realizar_pesquisa(CulinariaRequisitos(culinaria))
    elif escolha == 3:
        distancia = int(input('Qual a distância máxima (em km)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(DistanciaRequisitos(distancia))
    elif escolha == 4:
        classificacao = int(input('Qual a classificação mínima (de 1 a 5)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(ClassificacaoRequisitos(classificacao))
    elif escolha == 5:
        preco = float(input('Qual o preço máximo (em reais)? '))
        resultado_pesquisa = pesquisa.realizar_pesquisa(PrecoRequisitos(preco))
    elif escolha == 6:
        nome = input('Qual o nome do restaurante? ')
        culinaria = input('Qual o tipo de culinária? ')
        distancia = int(input('Qual a distância máxima (em km)? '))
        classificacao = int(input('Qual a classificação mínima (de 1 a 5)? '))
        preco = float(input('Qual o preço máximo (em reais)? '))
        resultado_nome = pesquisa.realizar_pesquisa(NomeRequisitos(nome))
        resultado_culinaria = pesquisa.realizar_pesquisa(CulinariaRequisitos(culinaria))
        resultado_distancia = pesquisa.realizar_pesquisa(DistanciaRequisitos(distancia))
        resultado_classificacao = pesquisa.realizar_pesquisa(ClassificacaoRequisitos(classificacao))
        resultado_preco = pesquisa.realizar_pesquisa(PrecoRequisitos(preco))
        resultado_pesquisa = find_intersection([resultado_nome, resultado_culinaria, resultado_distancia, resultado_classificacao, resultado_preco])

# Exibir resultados da pesquisa
    print("Resultados da Pesquisa:")
    for restaurante in resultado_pesquisa:
        print('Nome:',restaurante.nome, '\nDistância:',restaurante.distancia, '\nClassificação:',restaurante.classificacao, '\nPreço:',restaurante.preco, '\nCulinaria:',restaurante.culinaria)
        print()
        print()

realizar_pesquisa_com_usuario()
