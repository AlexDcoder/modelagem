'''
Quais transações em moeda Jake deve realizar de modo a
converter os investimentos feitos em ienes, rúpias e
ringgits em dólares norte-americanos para garantir que a
Grant Hill Associates tenha a quantia máxima em dólares
após todas as transações terem sido feitas?
Quanto dinheiro Jake tem de investir em obrigações do mercado norte-americano?
'''
from ortools.linear_solver import pywraplp
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, LIMITES_SOBRE_TRANSACOES
from math import inf


def resolver_problema_com_limites():
    '''
        Resolvendo o item b
    '''

    # Criando solver
    solver = pywraplp.Solver.CreateSolver("GLOP")

    # Criando variáveis
    variaveis = [
        solver.NumVar(0, inf, f"X{i_de}{i_para}")
        for i_de, _ in enumerate(MOEDAS)
        for i_para, _ in enumerate(MOEDAS)
    ]

    # Criar condições

    # Criar função objetivo
    funcao_objetivo = solver.Objective()

    # Resolver problema por minimização
    funcao_objetivo.SetMinimization()
    solver.Solve()


resolver_problema_com_limites()
