from model import Pais, Estado, session


def paises():
    paises = session.query(Pais).all()
    for pais in paises:
        print(pais.nome, pais.sigla, pais.populacao, pais.data_atualizacao)


# estados = session.query(Estado).all()

# for estado in estados:
#     print(estado.nome, estado.sigla, estado.pais.nome)

def pais(nome):
    pais = session.query(Pais).filter(Pais.nome == nome).first()
    print(pais.nome, pais.sigla, pais.populacao, pais.data_atualizacao)


pais('Brasil')


session.close()