from model import Pais, Estado, session


def add_pais(nome, sigla, populacao, data_atualizacao):
    pais = Pais(nome=nome, sigla=sigla, populacao=populacao, data_atualizacao=data_atualizacao)
    session.add(pais)
    session.commit()
    return pais

add_pais('argentina', 'ARG', 44938712, '2020-01-01')