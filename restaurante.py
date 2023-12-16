class Restaurante:
    def __init__(self, name, customer_rating, distance, price, cuisine_id):
        # Inicializa um objeto Restaurante com os atributos fornecidos.
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