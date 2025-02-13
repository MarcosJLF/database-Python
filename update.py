from model import Pais, Estado, session


try:
    pais = session.query(Pais).filter(Pais.nome == 'Brasil').first()
    pais.nome = 'brasil'
    session.commit()
    print('Pais atualizado com sucesso')
except Exception as e:
    session.rollback()
    print(f'Erro ao deletar o pais: {e}')
finally:
    session.close()
# pais('Brasil')    
# paises()