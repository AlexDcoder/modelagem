'''
Formule o problema de Jake como um problema do fluxo de custo mínimo
e desenhe a rede para esse problema.
Identifique os nós de suprimento e de demanda para a rede.
'''
from ortools.linear_solver import pywraplp
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, LIMITES_SOBRE_TRANSACOES
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint


def modelando_contexto():
    '''
        Modelando contexto somente no quesito visual
    '''
    variaveis = []
    funcao_objetivo = "F(x) = "
    condicoes = ""

    for i_de, moeda_de in enumerate(MOEDAS):
        for i_para, moeda_para in enumerate(MOEDAS):
            if TAXAS_DE_CAMBIO[i_de][i_para] is not None:
                variaveis.append(f"{moeda_de}->{moeda_para}: X{i_de}{i_para}")
                if CUSTO_DE_TRANSACAO[i_de][i_para] is not None:
                    if i_para == 7 and i_de == 7:
                        funcao_objetivo += f"{TAXAS_DE_CAMBIO[i_de][i_para] * CUSTO_DE_TRANSACAO[i_de][i_para]}"\
                            f"*X{i_de}{i_para}"
                    else:
                        funcao_objetivo += f"{TAXAS_DE_CAMBIO[i_de][i_para] * CUSTO_DE_TRANSACAO[i_de][i_para]}"\
                            f"*X{i_de}{i_para} + "
                else:
                    if i_para == 7 and i_de == 7:
                        funcao_objetivo += f"{TAXAS_DE_CAMBIO[i_de][i_para]}"\
                            f"*X{i_de}{i_para}"
                    else:
                        funcao_objetivo += f"{TAXAS_DE_CAMBIO[i_de][i_para]}"\
                            f"*X{i_de}{i_para} + "

    for i in range(3):
        for j in range(len(LIMITES_SOBRE_TRANSACOES[0])):
            if LIMITES_SOBRE_TRANSACOES[i][j] is not None:
                condicoes += f"X{i}{j} <= " \
                    f"{LIMITES_SOBRE_TRANSACOES[i][j]}\n"

    return f"""
[VARIÁVEIS]

{variaveis}

[FUNÇÃO OBJETIVO]

{funcao_objetivo}

[CONDIÇÕES]

{condicoes}
    """


def desenhar_fluxo():
    '''
        Visualizar o Fluxo
    '''

    G = nx.DiGraph()
    for i_de, moeda_de in enumerate(MOEDAS):
        G.add_node(moeda_de)
        for i_para, moeda_para in enumerate(MOEDAS):
            if TAXAS_DE_CAMBIO[i_de][i_para] is not None:
                if CUSTO_DE_TRANSACAO[i_de][i_para] is not None:
                    G.add_edge(
                        moeda_de, moeda_para,
                        weight=(
                            TAXAS_DE_CAMBIO[i_de][i_para] *
                            CUSTO_DE_TRANSACAO[i_de][i_para]
                        ))
                else:
                    G.add_edge(
                        moeda_de, moeda_para,
                        weight=TAXAS_DE_CAMBIO[i_de][i_para])

    pos = nx.circular_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, with_labels=True, node_color="red",
            node_size=2000, font_size=8, arrowsize=12)

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=labels, label_pos=0.23,
        font_size=7)

    plt.title("Rede de Conversão de Moedas")
    plt.show()


print(modelando_contexto())
desenhar_fluxo()
