'''
Quais transações em moeda Jake deve realizar de modo a
converter os investimentos feitos em ienes, rúpias e
ringgits em dólares norte-americanos para garantir que a
Grant Hill Associates tenha a quantia máxima em dólares
após todas as transações terem sido feitas?
Quanto dinheiro Jake tem de investir em obrigações do mercado norte-americano?
'''
from ortools.graph import pywrapgraph
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, LIMITES_SOBRE_TRANSACOES


def resolver_problema_com_limites():
    '''
        Resolvendo o item b
    '''
    # Criando solver
    solver = pywrapgraph.SimpleMinCostFlow()

    # Criando variáveis

    # Criar condições

    # Criar função objetivo

    # Resolver problema por minimização


resolver_problema_com_limites()
