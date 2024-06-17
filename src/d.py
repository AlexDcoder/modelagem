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

solver = pywraplp.Solver.CreateSolver("GLOP")
