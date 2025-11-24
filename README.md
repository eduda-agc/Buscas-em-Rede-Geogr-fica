# Buscas-em-Rede-Geogr-fica

## Autores

- Christian Bernard Simas Corrêa :: 11795572
- Eduarda Almeida Garrett de Carvalho :: 14566794
- Gabriel Antunes Afonso de Araujo :: 14571077

## Sobre o projeto

Este é o trabalho final da disciplina SCC0230 - Introdução à Inteligência artifical. O código consiste da implementação de diferentes algoritmos de busca sobre uma **rede geográfica**, além de uma interface gráfica que represente a rede e a simulação de cada algoritimo, visando atingir os seguintes objetivos:

1. Obter uma representação visual clara do comportamento de cada algoritmo
2. Realizar uma comparação da computação feita por cada algoritmo em 3 experimentos distintos

### Quanto a interface

A interface desenvolvida escolher parâmetros específicos para a rede, ou gerá-los aleatóriamente, além do algoritmo a ser utilizado naquela execução. Durante o processamento, cada passo de busca será mostrado, com o grafo gerado sequindo o seguinte padrão de cores:

- **Nó azul:** Nós do grafo ainda não processados pela busca
- **Nó verde:** Nó já visitado e constituinte do caminho atual
- **Nó amarelo:** Próximo nó a ser visitado na busca
- **Nó laranja:** Frontera; Na lista de próximos nós a serem visitados
- **Nó vermelho:** Já visitado e gerou um caminho inválido

### Quanto aos experimentos

Segue a descrição dos 3 experimentos do projeto:

1. Para cada algoritmo, escolher vértices de partida e destino específicos e comparar os caminhos efetuados e resultados obtidos.
2. Rodar cada algoritmo 10 vezes para buscas entre pontos distintos de uma rede gerada com parâmetros específicos.
3. Comparar o desempenho dos algoritmos Djikstra e A* para a rede gerada no experimento *2*.

## Como rodar

Após clonar o repositório:

1. Entre no diretório `Trab/`
2. Crie um ambiente virutal do python `python3 -m venv .venv`
3. Entre no ambiente virtual `source .venv/bin/activate`
4. Instale as dependências `pip install -r requirements.txt`
5. Rode o programa com `python main.py`

Para o desenvolvimento, é possível rodar o teste de terminal com `python -m tests.bfs_test`
