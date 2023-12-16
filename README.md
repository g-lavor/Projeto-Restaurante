# Projeto-Restaurante

Este projeto implementa um sistema simples de pesquisa de restaurantes em Python. Ele permite ao usuário realizar pesquisas com base em diferentes critérios, como nome, tipo de culinária, distância, classificação e preço.

## Conteúdo do Repositório

- 'restaurante.py': Este arquivo contém a definição da classe Restaurante, que representa um restaurante. Cada restaurante tem atributos como nome, classificação, distância, preço e tipo de culinária. Os métodos getter são fornecidos para acessar esses atributos.
- 'requisitos.py': Neste arquivo, são definidas classes abstratas e subclasses para requisitos de pesquisa. Cada tipo de requisito (nome, culinária, classificação, etc.) herda da classe abstrata Requisitos e implementa o método verificar para realizar a verificação específica.
- 'pesquisa_restaurante.py': Implementação da classe PesquisaRestaurante, que é responsável por realizar pesquisas em uma lista de restaurantes com base nos requisitos fornecidos. Os resultados são classificados por distância, classificação e preço.
- 'main.py': Este arquivo implementa a interação com o usuário. Pergunta ao usuário como eles desejam realizar a pesquisa, coleta as escolhas do usuário e realiza a pesquisa com base nesses critérios.
- 'cuisines.cvs': Arquivo CSV com dados sobre os tipos de culinária utilizados no programa.
- 'restaurants.csv': Arquivo CSV que contém informações sobre todos os restaurantes disponíveis.
- 'README.md': Arquivo de instruções detalhado que fornece uma visão geral do projeto, instruções sobre como executá-lo, detalhes sobre a estrutura do repositório, e quaisquer suposições feitas durante o desenvolvimento.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale a biblioteca pandas usando o comando `pip install pandas` ou `pip3 install pandas`.
3. Execute o programa principal com o comando `python main.py` ou `python3 main.py`.

## Suposições

- Ao iniciar o projeto, foi evidente que a implementação utilizando tabela hash poderia proporcionar um desempenho superior nas operações de busca. No entanto, a complexidade relacionada à implementação desse método, incluindo a gestão de colisões, tornou-se uma consideração significativa.

- Diante dessa análise, optamos por adotar a estrutura de lista. Apesar de apresentar uma redução de desempenho em situações que envolvem grandes volumes de objetos, a implementação em lista oferece simplicidade e clareza. Essa escolha facilita a visualização e compreensão do código, tornando-o mais acessível para manutenção e compreensão futura.

- Ao finalizar foi notável que, embora a implementação em listas de objetos tenha atendido aos requisitos do projeto atual, essa escolha pode não ser a mais adequada para uma aplicação mais robusta. 
