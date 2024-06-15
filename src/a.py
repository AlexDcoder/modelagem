'''
Formule o problema de Jake como um problema do fluxo de custo mínimo
e desenhe a rede para esse problema.
Identifique os nós de suprimento e de demanda para a rede.
'''
from ortools.linear_solver import pywraplp
from dados import TAXAS_DE_CAMBIO, MOEDAS
import networkx as nx
import matplotlib.pyplot as plt


solver = pywraplp.Solver.CreateSolver("GLOP")


def desenhar_fluxo():
    '''
        Visualizar o Fluxo
    '''

    G = nx.DiGraph()
    for i_de, moeda_de in enumerate(MOEDAS):
        G.add_node(moeda_de)
        for i_para, moeda_para in enumerate(MOEDAS):
            if TAXAS_DE_CAMBIO[i_de][i_para] is not None:
                G.add_edge(
                    moeda_de, moeda_para,
                    weight=TAXAS_DE_CAMBIO[i_de][i_para])

    pos = nx.circular_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color="red",
            node_size=3000, font_size=8, arrowsize=12)

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=labels, label_pos=0.23)

    plt.title("Rede de Conversão de Moedas")
    plt.show()


# desenhar_grafo()
