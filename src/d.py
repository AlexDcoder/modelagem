'''
Em resposta ao mandado da OMC proibindo limites sobre transações,
o governo da Indonésia introduz um novo imposto que leva a um aumento de 500%
nos custos de transação para transações de rúpias visando proteger a
moeda local. Dados esses novos custos de transação, mas sem limites sobre as
transações, que transações de câmbio Jake deveria realizar de modo
a converter suas posições em moedas asiáticas das
respectivas moedas para dólares?
'''
from math import inf
from copy import deepcopy
from ortools.linear_solver import pywraplp
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO


def resolver_questoes_com_imposto_aumentado(carga_japao, carga_malasia,
                                            carga_india):
    '''
        Resolvendo item d
    '''
    # Criando novo imposto para as rúpias
    novos_custos_transacao = deepcopy(CUSTO_DE_TRANSACAO)

    novos_custos_transacao[1] = [
        x * 6 if x is not None else None for x in novos_custos_transacao[1]]
    for i in range(8):
        novos_custos_transacao[i][1] = novos_custos_transacao[1][i]

    qtd_moedas = len(MOEDAS)

    # Cargas Iniciais(Em Dólares)
    carga_japao_dolar = TAXAS_DE_CAMBIO[0][3] * carga_japao
    carga_india_dolar = TAXAS_DE_CAMBIO[1][3] * carga_india
    carga_malasia_dolar = TAXAS_DE_CAMBIO[2][3] * carga_malasia

    solver = pywraplp.Solver.CreateSolver("GLOP")

    X = []

    # Capacidades em  Dólares
    for i in range(qtd_moedas):
        X.append([])
        for j in range(qtd_moedas):
            X[i].append(solver.NumVar(0, inf, f"X[{i}][{j}]"))

    c_dolar = solver.NumVar(0, solver.Infinity(), "c_dolar")

    # Constraints
    for i in range(qtd_moedas):
        somaEntrada = 0
        somaSaida = 0
        for j in range(qtd_moedas):
            somaSaida += X[i][j]
            somaEntrada += X[j][i]
        if i == 0:
            solver.Add(somaSaida-somaEntrada == carga_japao_dolar)
        elif i == 1:
            solver.Add(somaSaida-somaEntrada == carga_india_dolar)
        elif i == 2:
            solver.Add(somaSaida-somaEntrada == carga_malasia_dolar)
        elif i == 3:
            solver.Add(somaSaida-somaEntrada == -1*(
                carga_japao_dolar + carga_india_dolar + carga_malasia_dolar))
        else:
            solver.Add(somaSaida-somaEntrada == 0)

    soma_custo = 0

    for i in range(qtd_moedas):
        for j in range(qtd_moedas):
            if i != j:
                soma_custo += novos_custos_transacao[i][j]*X[i][j]
            else:
                soma_custo += (0*X[i][j])

    solver.Add(c_dolar == soma_custo)
    solver.Minimize(c_dolar)
    solver.Solve()

    for i in range(qtd_moedas):
        for j in range(qtd_moedas):
            print(X[i][j].solution_value(), end=' ')
        print()
    print(c_dolar.solution_value())


resolver_questoes_com_imposto_aumentado(15000000, 10500000000.0, 28000000.0)
