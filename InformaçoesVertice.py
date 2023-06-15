from collections import deque

def ler_arquivo_grafo(nome_arquivo):
    grafo = {}
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            vertices = linha.strip().split()
            vertice_origem = int(vertices[0])
            vertice_destino = int(vertices[1])

            if vertice_origem not in grafo:
                grafo[vertice_origem] = {'sucessores': set(), 'predecessores': set()}

            if vertice_destino not in grafo:
                grafo[vertice_destino] = {'sucessores': set(), 'predecessores': set()}

            grafo[vertice_origem]['sucessores'].add(vertice_destino)
            grafo[vertice_destino]['predecessores'].add(vertice_origem)

    return grafo

def grau_saida(grafo, vertice):
    if vertice in grafo:
        return len(grafo[vertice]['sucessores'])
    else:
        return 0

def grau_entrada(grafo, vertice):
    if vertice in grafo:
        return len(grafo[vertice]['predecessores'])
    else:
        return 0

def conjunto_sucessores(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]['sucessores']
    else:
        return set()

def conjunto_predecessores(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]['predecessores']
    else:
        return set()

def busca_profundidade(grafo, vertice):
    visitados = set()
    resultado = []

    def dfs(v):
        visitados.add(v)
        resultado.append(v)

        for sucessor in grafo[v]['sucessores']:
            if sucessor not in visitados:
                dfs(sucessor)

    if vertice in grafo:
        dfs(vertice)

    return resultado

def busca_largura(grafo, vertice):
    visitados = set()
    resultado = []
    fila = deque()

    if vertice not in grafo:
        return resultado

    fila.append(vertice)
    visitados.add(vertice)

    while fila:
        v = fila.popleft()
        resultado.append(v)

        for sucessor in grafo[v]['sucessores']:
            if sucessor not in visitados:
                visitados.add(sucessor)
                fila.append(sucessor)

    return resultado

def eh_conexo(grafo):
    visitados = set()
    fila = deque()

    # Selecionar um vértice qualquer como ponto de partida
    vertice_inicial = next(iter(grafo.keys()))

    fila.append(vertice_inicial)
    visitados.add(vertice_inicial)

    while fila:
        v = fila.popleft()

        for sucessor in grafo[v]['sucessores']:
            if sucessor not in visitados:
                visitados.add(sucessor)
                fila.append(sucessor)

    return len(visitados) == len(grafo)

def eh_ciclico(grafo):
    visitados = set()
    em_processamento = set()

    def tem_ciclo(v):
        visitados.add(v)
        em_processamento.add(v)

        for sucessor in grafo[v]['sucessores']:
            if sucessor not in visitados:
                if tem_ciclo(sucessor):
                    return True
            elif sucessor in em_processamento:
                return True

        em_processamento.remove(v)
        return False

    for vertice in grafo.keys():
        if vertice not in visitados:
            if tem_ciclo(vertice):
                return True

    return False

# Exemplo de uso
nome_arquivo = input("Digite o nome do arquivo: ")

grafo = ler_arquivo_grafo(nome_arquivo)

resp = False

while resp == False:
    vertice = int(input("Digite o número do vértice: "))
    resp = vertice in grafo

    if resp == True:
        print("\nInformações do vértice:")
        print("Grau de saída:", grau_saida(grafo, vertice))
        print("Grau de entrada:", grau_entrada(grafo, vertice))
        print("Conjunto de sucessores:", conjunto_sucessores(grafo, vertice))
        print("Conjunto de predecessores:", conjunto_predecessores(grafo, vertice))
        print("Busca em profundidade:", busca_profundidade(grafo, vertice))
        print("Busca em largura:", busca_largura(grafo, vertice))

        if eh_conexo(grafo):
            print("O grafo é conexo")
        else:
            print("O grafo não é conexo")

        if eh_ciclico(grafo):
            print("O grafo é cíclico")
        else:
            print("O grafo não é cíclico")
    else:
        print("O vértice informado não pertence à base de dados. Por favor, informe outro vértice.")
