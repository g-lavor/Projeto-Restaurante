class PesquisaRestaurante:
    def __init__(self, restaurantes):
        # Inicializa um objeto PesquisaRestaurante com uma lista de restaurantes.
        self.__restaurantes = restaurantes

    def realizar_pesquisa(self, *requisitos):
        # Realiza a pesquisa considerando os requisitos fornecidos.
        resultados = set(self.__restaurantes)
        for requisito in requisitos:
            resultados = set(filter(requisito.verificar, resultados))
        resultados = sorted(resultados, key=lambda r: (r.distancia, -r.classificacao, r.preco))
        return resultados[:5]