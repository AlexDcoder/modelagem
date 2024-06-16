'''
Quais transações em moeda Jake deve realizar de modo a
converter os investimentos feitos em ienes, rúpias e
ringgits em dólares norte-americanos para garantir que a
Grant Hill Associates tenha a quantia máxima em dólares
após todas as transações terem sido feitas?
Quanto dinheiro Jake tem de investir em obrigações do mercado norte-americano?
'''
from ortools.linear_solver import pywraplp


solver = pywraplp.Solver.CreateSolver("GLOP")


def resolver_problema_com_limites():
    # Criando variáveis
    variaveis = [
        solver.IntVar(0, inf, f"{moeda_de}->{moeda_para}")
        for i_de, moeda_de in enumerate(MOEDAS)
        for i_para, moeda_para in enumerate(MOEDAS)
        if TAXAS_DE_CAMBIO[i_de][i_para] != 0
    ]
    # Criar condições

    # Criar função objetivo
    funcao_objetivo = solver.Objective()
