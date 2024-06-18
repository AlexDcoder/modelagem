'''
A Organização Mundial do Comércio (OMC) proíbe limites sobre transações,
pois elas promovem o protecionismo. Se não existissem limites de transação,
que método Jake deveria usar para converter em dólares as posições
atuais nas respectivas moedas asiáticas?
'''
from ortools.graph import pywrapgraph
from dados import TAXAS_DE_CAMBIO, MOEDAS, CUSTO_DE_TRANSACAO, LIMITES_SOBRE_TRANSACOES


def resolver_questoes_sem_os_limites():
    '''
        Resolvendo item c
    '''
    # Criando solver
    solver = pywrapgraph.SimpleMinCostFlow()

    # Criando variáveis

    # Criar condições

    # Criar função objetivo
