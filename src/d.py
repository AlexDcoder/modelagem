'''
Em resposta ao mandado da OMC proibindo limites sobre transações,
o governo da Indonésia introduz um novo imposto que leva a um aumento de 500%
nos custos de transação para transações de rúpias visando proteger a
moeda local. Dados esses novos custos de transação, mas sem limites sobre as
transações, que transações de câmbio Jake deveria realizar de modo
a converter suas posições em moedas asiáticas das
respectivas moedas para dólares?
'''
from copy import deepcopy
from ortools.graph.python import min_cost_flow
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, \
    LIMITES_SOBRE_TRANSACOES


def resolver_questoes_com_imposto_aumentado():
    '''
        Resolvendo item d
    '''
    novos_custos_transacao = deepcopy(CUSTO_DE_TRANSACAO)

    novos_custos_transacao[1] = [
        x * 5 if x is not None else None for x in novos_custos_transacao[1]]
    for i in range(8):
        novos_custos_transacao[i][1] = novos_custos_transacao[1][i]

    # Criando solver
    solver = min_cost_flow.SimpleMinCostFlow()

    # Criando variáveis

    # Criar condições

    # Criar função objetivo


resolver_questoes_com_imposto_aumentado()
