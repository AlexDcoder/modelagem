'''
A Organização Mundial do Comércio (OMC) proíbe limites sobre transações,
pois elas promovem o protecionismo. Se não existissem limites de transação,
que método Jake deveria usar para converter em dólares as posições
atuais nas respectivas moedas asiáticas?
'''

from math import inf
from ortools.linear_solver import pywraplp
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO


def resolver_problema_sem_limites(carga_japao, carga_india, carga_malasia):
    '''
        Resolvendo o item b
    '''
    qtd_moedas = len(MOEDAS)

    # Cargas Iniciais(Em Dólares)
    carga_japao_dolar = TAXAS_DE_CAMBIO[1][3] * carga_japao
    carga_india_dolar = TAXAS_DE_CAMBIO[1][3] * carga_india
    carga_malasia_dolar = TAXAS_DE_CAMBIO[2][3] * carga_malasia

    solver = pywraplp.Solver.CreateSolver("GLOP")

    X = []

    # Capacidades em  Dólares
    for i in range(qtd_moedas):
        X.append([])
        for j in range(qtd_moedas):
            if i < 3:
                X[i].append(solver.NumVar(
                    0, inf, f"X[{i}][{j}]"))
            else:
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
                soma_custo += CUSTO_DE_TRANSACAO[i][j]*X[i][j]
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


resolver_problema_sem_limites(15000000, 10500000000.0, 28000000.0)
