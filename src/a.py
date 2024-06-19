'''
    Formule o problema de Jake como um problema do fluxo de custo mínimo
    e desenhe a rede para esse problema.
    Identifique os nós de suprimento e de demanda para a rede.
'''
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, \
    LIMITES_SOBRE_TRANSACOES


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
            if i_de != 7:
                if i_de == i_para:
                    funcao_objetivo += f"0 * X{i_de}{i_para} + "
                else:
                    funcao_objetivo += f"{CUSTO_DE_TRANSACAO[i_de]
                                          [i_para]} * X{i_de}{i_para} + "
            else:
                if i_de == i_para:
                    funcao_objetivo += f"0 * X{i_de}{i_para}"
                else:
                    funcao_objetivo += f"{CUSTO_DE_TRANSACAO[i_de]
                                          [i_para]} * X{i_de}{i_para} + "
    print("[VARIÁVEIS]\n")
    pprint(variaveis)
    # Definindo Condições

    for i in range(3):
        for j in range(len(LIMITES_SOBRE_TRANSACOES[0])):
            if LIMITES_SOBRE_TRANSACOES[i][j] is not None:
                condicoes += f"X{i}{j}  - "\
                    f"X{j}{i}  <= " \
                    f"{LIMITES_SOBRE_TRANSACOES[i][j]}\n"

    for i in range(3):
        condicoes += "\n"
        for j in range(len(LIMITES_SOBRE_TRANSACOES[0])):
            if j < 7:
                if i == j:
                    condicoes += f"0 * X{i}{j} + "
                else:
                    condicoes += f"{CUSTO_DE_TRANSACAO[i]
                                    [j]} * X{i}{j} + "
            else:
                if i == j:
                    condicoes += f"0 * X{i}{j} = CARGA VÉRTICE {i}"
                else:
                    condicoes += f"{CUSTO_DE_TRANSACAO[i]
                                    [j]} * X{i}{j} = CARGA VÉRTICE {i}"

    condicoes += "\n"

    print("\n[FUNÇÃO OBJETIVO]\n")
    print(funcao_objetivo)

    print("\n[CONDIÇÕES]\n")
    print(condicoes)


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
            else:
                G2.add_edge(
                    moeda_de, moeda_para,
                    weight=0)

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


modelando_contexto()

desenhar_fluxo_custo()
