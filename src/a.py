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
from time import sleep


def modelando_contexto():
    '''
        Modelando contexto somente no quesito visual
    '''
    variaveis = []
    funcao_objetivo = "(MIN) F(x) = "
    condicoes = ""

    # Definindo as variáveis

    for i_de, moeda_de in enumerate(MOEDAS):
        for i_para, moeda_para in enumerate(MOEDAS):
            variaveis.append(f"{moeda_de}->{moeda_para}: X{i_de}{i_para}")

    # Definindo função objetivo
    for i_de, moeda_de in enumerate(MOEDAS):
        for i_para, moeda_para in enumerate(MOEDAS):
            if i_para == 3:
                if i_de != 7:
                    if CUSTO_DE_TRANSACAO[i_de][i_para] is not None:
                        funcao_objetivo += f"{CUSTO_DE_TRANSACAO[i_de]
                                              [i_para]} * X{i_de}{i_para} + "
                else:
                    if CUSTO_DE_TRANSACAO[i_de][i_para] is not None:
                        funcao_objetivo += f"{CUSTO_DE_TRANSACAO[i_de]
                                              [i_para]} * X{i_de}{i_para}"

    # Definindo Condições

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

# (X * CUSTO_DE)*TAXA_PARA(EM DÓLAR) --> MANTER DÓLAR

# Ringgit Dólar
# 1000*0,7/100 --> 7 Ringgits * 0,2 --> 1,4 Dólares --> o quanto paga para passar de ringitt pra dólar

# Ringgit Euro Dolar
# 1000 * 0,4/100 -> 4 ringitss * 0,2 --> 0,8 Dólares

# Fazer conversões nos limites porque tá em dólar
# PDF SÓ PRO A


def desenhar_fluxo_taxa():
    '''
        Visualizar o Fluxo da Taxa de Transação
    '''

    G1 = nx.DiGraph()
    for i_de, moeda_de in enumerate(MOEDAS):
        G1.add_node(moeda_de)
        for i_para, moeda_para in enumerate(MOEDAS):
            if TAXAS_DE_CAMBIO[i_de][i_para] is not None:
                G1.add_edge(
                    moeda_de, moeda_para,
                    weight=TAXAS_DE_CAMBIO[i_de][i_para])
            else:
                G1.add_edge(
                    moeda_de, moeda_para,
                    weight=(1 / TAXAS_DE_CAMBIO[i_para][i_de]))

    pos = nx.circular_layout(G1)
    labels = nx.get_edge_attributes(G1, 'weight')

    nx.draw(G1, pos, with_labels=True, node_color="red",
            node_size=2000, font_size=8, arrowsize=12)

    nx.draw_networkx_edge_labels(
        G1, pos, edge_labels=labels, label_pos=0.23,
        font_size=7)

    plt.title("Rede de Conversão de Moedas - Taxa de Transação")
    plt.show()


def desenhar_fluxo_custo():
    '''
        Visualizar o Fluxo da Custo de Transação
    '''
    G2 = nx.Graph()
    for i_de, moeda_de in enumerate(MOEDAS):
        G2.add_node(moeda_de)
        for i_para, moeda_para in enumerate(MOEDAS):
            if CUSTO_DE_TRANSACAO[i_de][i_para] is not None:
                G2.add_edge(
                    moeda_de, moeda_para,
                    weight=CUSTO_DE_TRANSACAO[i_de][i_para])

    pos = nx.circular_layout(G2)
    labels = nx.get_edge_attributes(G2, 'weight')

    nx.draw(G2, pos, with_labels=True, node_color="red",
            node_size=2000, font_size=8, arrowsize=12)

    nx.draw_networkx_edge_labels(
        G2, pos, edge_labels=labels, label_pos=0.23,
        font_size=7)

    pos = nx.circular_layout(G2)
    labels = nx.get_edge_attributes(G2, 'weight')

    nx.draw(G2, pos, with_labels=True, node_color="blue",
            node_size=2000, font_size=8, arrowsize=12)

    nx.draw_networkx_edge_labels(
        G2, pos, edge_labels=labels, label_pos=0.23,
        font_size=7)

    plt.title("Rede de Conversão de Moedas - Custo de transacao")
    plt.show()


print(modelando_contexto())

# Apresenta o grafo da taxa de câmbio
# desenhar_fluxo_taxa()

# # Ao fechar a aba do grafo da taxa esse outro aparecerá
# desenhar_fluxo_custo()
