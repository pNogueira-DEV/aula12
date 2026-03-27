#relacionamento muitos para muitos (N:N)

#Estudante se inscrevem em cursos
#um estudante pode fazer vários cursos
#um curso pode ter vários estudantes





#forma simples:
# A relação não precisa guardar dados extras
#só fazer o relacionmento 



from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship



Base = declarative_base()



#tabelas curso e aluno
class Aluno(Base):
    __tablename__ = "alunos"




    #Como cria uma coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)



    #Função para imprimir
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"