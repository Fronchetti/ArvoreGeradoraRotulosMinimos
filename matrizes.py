from networkx import Graph

def gera_grafo(dados, ordem):
    grafo = Graph()
    grafo.add_nodes_from(range(1, ordem+1))
    for l in range(1, ordem):
        cols = [col for col in range(l+1, ordem+1)]
        edges = [(l, c, peso) for c, peso in zip(cols, dados[l-1]) if peso != 0]
        grafo.add_weighted_edges_from(edges)
    return grafo

def inicializa(entrada):
    arquivo = open(entrada)
    linhas = arquivo.readlines()
    ordem = [int(item) for item in linhas[0][:-1].split(' ')][0]
    grafos = []
    dados = []
    for linha in linhas[1:]:
        if linha == '\n':
            grafos.append(gera_grafo(dados, ordem))
            dados = []
            continue
        dados.append([int(item) for item in linha[:-2].split(' ')])

    # mostra as arestas do primeiro grafo e o peso
    for n, vizinhos in grafos[0].adjacency_iter():
        for vizinho, attr in vizinhos.items():
            peso = attr['weight']
            print('{}-{}: {}'.format(n, vizinho, peso))

if __name__ == '__main__':
    from sys import argv
    inicializa(argv[1])