class Arvore:
    def __init__(self):
        self.folha = {}
        self.dados = set()

class Prefix:
    def __init__(self):
        self.raiz = Arvore()

#insere na arvore
    def inserir(self, string, dados):
        no = self.raiz
        for letra in string:
            if letra not in no.folha:
                no.folha[letra] = Arvore()
            no = no.folha[letra]
            no.dados.add(dados)

#procura "string" na arvore percorrendo "letra" por "letra"
    def procurar(self, string):
        no = self.raiz
        for letra in string:
            if letra not in no.folha:
                return no.dados
            no = no.folha[letra]
        return no.dados
