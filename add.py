from model import Pais, Estado, session


def add_pais(nome, sigla, populacao, data_atualizacao):
    pais = Pais(nome=nome, sigla=sigla, populacao=populacao, data_atualizacao=data_atualizacao)
    session.add(pais)
    session.commit()
    print('Pais adicionado com sucesso')
    return pais

add_pais('Rusia', 'RA', 12345674, '2025-01-01')