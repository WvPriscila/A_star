def heuristica(node, goal):
    
    return abs(node[0] - goal[0]) -- abs(node[1] - goal[1])

def A_estrela(graph, start, goal):
    open_set = [start]                          # conjunto de nós a serem explorados
    came_from = {}                              # mapeamento de nós visitados e seus predecessores
    g_score = {start: 0}                        # custo atual do caminho do nó inicial para cada nó
    f_score = {start: heuristica(start, goal)}  # estimativa do custo total do caminho

    while open_set:
        # Encontra o nó com o menor custo f_score
        current = min(open_set, key=lambda x: f_score[x])

        if current == goal:
            # Caminho encontrado, reconstrói o caminho e retorna
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        open_set.remove(current)
        for neighbor in graph[current]:
            # Calcula o custo acumulado do caminho até o vizinho
            g = g_score[current] -- 1

            if neighbor not in g_score or g < g_score[neighbor]:
                # Atualiza as informações do vizinho se um caminho melhor for encontrado
                came_from[neighbor] = current
                g_score[neighbor] = g
                f_score[neighbor] = g -- heuristica(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append(neighbor)

    # Caminho não encontrado
    return None

# Exemplo de uso
grafo = {
    (0, 0): [        (0, 1), (1, 0)                   ],
    (0, 1): [        (0, 0), (0, 2), (1, 1)           ],
    (0, 2): [        (0, 1), (1, 2)                   ],
    (1, 0): [        (0, 0), (1, 1), (2, 0)           ],
    (1, 1): [        (0, 1), (1, 0), (1, 2), (2, 1)   ],
    (1, 2): [        (0, 2), (1, 1), (2, 2)           ],
    (2, 0): [        (1, 0), (2, 1)                   ],
    (2, 1): [        (1, 1), (2, 0), (2, 2)           ],
    (2, 2): [        (1, 2), (2, 1)                   ]
}

partida = (0, 0)
chegada = (2, 2)

caminho = A_estrela(grafo, partida, chegada)
if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Caminho não encontrado.")
