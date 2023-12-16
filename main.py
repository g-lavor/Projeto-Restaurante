import csv
import pandas as pd
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
        # Classe abstrata que define a estrutura para os requisitos de pesquisa
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    @abstractmethod
    def verificar(self, restaurante):
        pass

class NomeRequisitos(Requisitos):
    def verificar(self, restaurante):
        valor = self.valor.lower().replace(" ", "")  # Remover espaços e tornar minúsculo
        restaurante_nome = restaurante.nome.lower().replace(" ", "")  # Remover espaços e tornar minúsculo

        # Sempre realizar pesquisa por prefixo
        prefixo = valor
        return restaurante_nome.startswith(prefixo)

class CulinariaRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se o tipo de culinária do restaurante atende aos critérios
        return self.valor.lower() == restaurante.culinaria.lower()

class ClassificacaoRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se a classificação do restaurante atende aos critérios
        return restaurante.classificacao >= int(self.valor)

class DistanciaRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se a distância do restaurante atende aos critérios
        return restaurante.distancia <= int(self.valor)

class PrecoRequisitos(Requisitos):
    def verificar(self, restaurante):
        # Verifica se o preço do restaurante atende aos critérios
        return restaurante.preco <= float(self.valor)

class PesquisaRestaurante:
    def __init__(self, restaurantes):
        # Classe que realiza pesquisas em uma lista de restaurantes
        self.__restaurantes = restaurantes

    def realizar_pesquisa(self, *requisitos):
        # Realiza a pesquisa considerando os requisitos fornecidos
        resultados = set(self.__restaurantes)
        for requisito in requisitos:
            resultados = set(filter(requisito.verificar, resultados))
        resultados = sorted(resultados, key=lambda r: (r.distancia, -r.classificacao, r.preco))
        return resultados[:5]

def carregar_dados_csv(arquivo_restaurantes, arquivo_culinarias):
    # Carrega dados de restaurantes e culinárias a partir de arquivos CSV
    with open(arquivo_restaurantes, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dados = [dict(row) for row in reader]
    df_culinaria = pd.read_csv(arquivo_culinarias)
    mapeamento_culinaria = df_culinaria.set_index('id')['name'].to_dict()
    for restaurante in dados:
        restaurante['cuisine_id'] = mapeamento_culinaria.get(int(restaurante['cuisine_id']), restaurante['cuisine_id'])
    return [Restaurante(**restaurante) for restaurante in dados]

def realizar_pesquisa_com_usuario():
    # Realiza uma pesquisa com base nas escolhas do usuário
    restaurantes = carregar_dados_csv('restaurants.csv', 'cuisines.csv')
    pesquisa = PesquisaRestaurante(restaurantes)
    print('Como deseja realizar a pesquisa?\n1 - Nome\n2 - Culinaria\n3 - Distancia\n4 - Classificação\n5 - Preço')
    escolhas = input('Digite os números das opções desejadas, separados por vírgula (ex: 1,3,5): ')
    escolhas = [int(e) for e in escolhas.split(',') if e.isdigit() and 1 <= int(e) <= 5]
    resultados_intermediarios = []

    for escolha in escolhas:
        if escolha == 1:
            nome = input('Qual o nome do restaurante? ')
            resultados_intermediarios.append(NomeRequisitos(nome))
        elif escolha == 2:
            culinaria = input('Qual o tipo de culinária? ')
            resultados_intermediarios.append(CulinariaRequisitos(culinaria))
        elif escolha == 3:
            distancia = int(input('Qual a distância máxima (em km)? '))
            resultados_intermediarios.append(DistanciaRequisitos(distancia))
        elif escolha == 4:
            classificacao = int(input('Qual a classificação mínima (de 1 a 5)? '))
            resultados_intermediarios.append(ClassificacaoRequisitos(classificacao))
        elif escolha == 5:
            preco = float(input('Qual o preço máximo (em reais)? '))
            resultados_intermediarios.append(PrecoRequisitos(preco))
    resultado_pesquisa = pesquisa.realizar_pesquisa(*resultados_intermediarios)

    if resultado_pesquisa:
        print("Resultados da Pesquisa:\n")
        for restaurante in resultado_pesquisa:
            print(
                'Nome:', restaurante.nome, '\nDistância:', restaurante.distancia,
                '\nClassificação:', restaurante.classificacao, '\nPreço:', restaurante.preco,
                '\nCulinaria:', restaurante.culinaria
            )
            print()
            print()
    else:
        print("Sem restaurantes disponíveis")

# Chama a função para realizar a pesquisa com o usuário
realizar_pesquisa_com_usuario()
