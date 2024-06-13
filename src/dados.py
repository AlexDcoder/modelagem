'''
Definindo os dados das questões
'''

Matriz = list[list[int | float | None]]

# Matriz com taxas de câmbio
TAXAS_DE_CAMBIO: Matriz = [
    [1, 50, 0.04, 0.008, 0.01, 0.0064, 0.0048, 0.0768],
    [None, 1, 0.0008, 0.00016, 0.0002, 0.000128, 0.000096, 0.001536],
    [None, None, 1, 0.2, 0.25, 0.16, 0.12, 1.92],
    [None, None, None, 1, 1.25, 0.8, 0.6, 9.6],
    [None, None, None, None, 1, 0.64, 0.48, 7.68],
    [None, None, None, None, None, 1, 0.75, 12],
    [None, None, None, None, None, None, 1, 16],
    [None, None, None, None, None, None, None, 1],
]

# Matriz de custo de transação percentual
CUSTO_DE_TRANSACAO: Matriz = [
    [None, 0.5, 0.5, 0.4, 0.4, 0.4, 0.25, 0.5],
    [None, None, 0.7, 0.5, 0.3, 0.3, 0.75, 0.75],
    [None, None, None, 0.7, 0.7, 0.4, 0.45, 0.5],
    [None, None, None, None, 0.05, 0.1, 0.1, 0.1],
    [None, None, None, None, None, 0.2, 0.1, 0.1],
    [None, None, None, None, None, None, 0.05, 0.5],
    [None, None, None, None, None, None, None, 0.5],
    [None, None, None, None, None, None, None, None,]
]

# Matriz de limites sonre transações equivalentes a USUS$ 1000
LIMITES_SOBRE_TRANSACOES: Matriz = [
    [None, 5000, 5000, 2000, 2000, 2000, 2000, 4000],
    [5000, None, 2000, 200, 200, 1000, 500, 200],
    [3000, 4500, None, 1500, 1500, 2500, 1000, 1000],
]
