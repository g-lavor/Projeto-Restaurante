import csv
import pandas as pd
from restaurante import Restaurante
from requisitos import NomeRequisitos, CulinariaRequisitos, ClassificacaoRequisitos, DistanciaRequisitos, PrecoRequisitos
from pesquisa_restaurante import PesquisaRestaurante

def carregar_dados_csv(arquivo_restaurantes, arquivo_culinarias):
    # Carrega dados de restaurantes e culinárias a partir de arquivos CSV.
    with open(arquivo_restaurantes, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dados = [dict(row) for row in reader]
    df_culinaria = pd.read_csv(arquivo_culinarias)
    mapeamento_culinaria = df_culinaria.set_index('id')['name'].to_dict()
    for restaurante in dados:
        restaurante['cuisine_id'] = mapeamento_culinaria.get(int(restaurante['cuisine_id']), restaurante['cuisine_id'])
    return [Restaurante(**restaurante) for restaurante in dados]

def realizar_pesquisa_com_usuario():
    # Realiza uma pesquisa com base nas escolhas do usuário.
    restaurantes = carregar_dados_csv('restaurants.csv', 'cuisines.csv')
    pesquisa = PesquisaRestaurante(restaurantes)
    
    print('Como deseja realizar a pesquisa?\n1 - Nome\n2 - Culinaria\n3 - Distancia\n4 - Classificação\n5 - Preço')
    
    # Pede as escolhas do usuário
    escolhas = None
    
    while escolhas is None:
        escolhas_str = input('Digite os números das opções desejadas, separados por vírgula (ex: 1,3,5): ')
        escolhas = [int(e) for e in escolhas_str.split(',') if e.isdigit() and 1 <= int(e) <= 5]

        if len(escolhas) != len(escolhas_str.split(',')):
            print('Entrada inválida. Escolha apenas números de 1 a 5.')
            escolhas = None  # Reinicia o loop se a entrada for inválida

    resultados_intermediarios = []

    for escolha in escolhas:
        if escolha == 1:
            nome = input('Qual o nome do restaurante? ')
            resultados_intermediarios.append(NomeRequisitos(nome))
        elif escolha == 2:
            culinaria = input('Qual o tipo de culinária? ')
            resultados_intermediarios.append(CulinariaRequisitos(culinaria))
        elif escolha == 3:
            try:
                distancia = int(input('Qual a distância máxima (em km)? '))
                resultados_intermediarios.append(DistanciaRequisitos(distancia))
            except ValueError:
                print('Entrada inválida. Certifique-se de inserir um número válido para a distância.')
                return  # Retorna, interrompendo a função se a entrada for inválida
        elif escolha == 4:
            try:
                classificacao = int(input('Qual a classificação mínima (de 1 a 5)? '))
                resultados_intermediarios.append(ClassificacaoRequisitos(classificacao))
            except ValueError:
                print('Entrada inválida. Certifique-se de inserir um número válido para a classificação.')
                return  # Retorna, interrompendo a função se a entrada for inválida
        elif escolha == 5:
            try:
                preco = float(input('Qual o preço máximo (em reais)? '))
                resultados_intermediarios.append(PrecoRequisitos(preco))
            except ValueError:
                print('Entrada inválida. Certifique-se de inserir um número válido para o preço.')
                return  # Retorna, interrompendo a função se a entrada for inválida

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

if __name__ == "__main__":
    realizar_pesquisa_com_usuario()
    # Chama a função para realizar a pesquisa com o usuário
