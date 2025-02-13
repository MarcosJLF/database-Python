from model import Pais, Estado, session

try:
    pais = session.query(Pais).filter(Pais.nome == 'brasil').first()
    session.delete(pais)
    session.commit()
    print('Pais deletado com sucesso')
except Exception as e:
    session.rollback()
    print(f'Erro ao deletar o pais: {e}')
finally:
    session.close()
# pais('Brasil')