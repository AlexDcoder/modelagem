'''
Definindo os dados das questões
'''

Matriz = list[list[int | float | None]]

MOEDAS = [
    "Iene", "Rúpia", "Ringgit", "Dólar Americano",
    "Dólar Canadense", "Euro", "Libra", "Peso"
]

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
    [None, 0.5/100, 0.5/100, 0.4/100, 0.4/100, 0.4/100, 0.25/100, 0.5/100],
    [0.5/100, None, 0.7/100, 0.5/100, 0.3/100, 0.3/100, 0.75/100, 0.75/100],
    [0.5/100, 0.7/100, None, 0.7/100, 0.7/100, 0.4/100, 0.45/100, 0.5/100],
    [0.4/100, 0.5/100, 0.7/100, None, 0.05/100, 0.1/100, 0.1/100, 0.1/100],
    [0.4/100, 0.3/100, 0.7/100, 0.05/100, None, 0.2/100, 0.1/100, 0.1/100],
    [0.4/100, 0.3/100, 0.4/100, 0.1/100, 0.2/100, None, 0.05/100, 0.5/100],
    [0.25/100, 0.75/100, 0.45/100, 0.1/100, 0.1/100, 0.05/100, None, 0.5/100],
    [0.5/100, 0.75/100, 0.5/100, 0.1/100, 0.1/100, 0.5/100, 0.5/100, None]
]

# Matriz de limites sobre transações equivalentes a USUS$ 1000
LIMITES_SOBRE_TRANSACOES: Matriz = [
    [None, 5000*10**3, 5000*10**3, 2000*10**3, 2000 *
        10**3, 2000*10**3, 2000*10**3, 4000*10**3],
    [5000*10**3, None, 2000*10**3, 200*10**3, 200 *
        10**3, 1000*10**3, 500*10**3, 200*10**3],
    [3000*10**3, 4500*10**3, None, 1500*10**3, 1500 *
        10**3, 2500*10**3, 1000*10**3, 1000*10**3],
]
