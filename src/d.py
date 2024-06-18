'''
Em resposta ao mandado da OMC proibindo limites sobre transações,
o governo da Indonésia introduz um novo imposto que leva a um aumento de 500%
nos custos de transação para transações de rúpias visando proteger a
moeda local. Dados esses novos custos de transação, mas sem limites sobre as
transações, que transações de câmbio Jake deveria realizar de modo
a converter suas posições em moedas asiáticas das
respectivas moedas para dólares?
'''
from ortools.linear_solver import pywraplp
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, LIMITES_SOBRE_TRANSACOES
from math import inf
from pprint import pprint
from copy import deepcopy


def resolver_questoes_com_imposto_aumentado():
    '''
        Resolvendo item d
    '''
    novos_custos_de_transação = deepcopy(CUSTO_DE_TRANSACAO)

    novos_custos_de_transação[1] = [
        x * 5 if x is not None else None for x in novos_custos_de_transação[1]]
    for i in range(8):
        novos_custos_de_transação[i][1] = novos_custos_de_transação[1][i]

    pprint(novos_custos_de_transação)
    solver = pywraplp.Solver.CreateSolver("GLOP")


resolver_questoes_com_imposto_aumentado()
