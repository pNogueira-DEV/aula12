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
    

class Curso(Base):
    __tablename__ = "cursos"

    #Como cria uma coluna
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)



    #Função para imprimir
    def __repr__(self):
        return f"ID: {self.id} - NOME: {self.nome}"
    




#Tabela Intermediaria
inscricoes = Table(
    "inscricoes", #nome da tabela
    Base.metadata,
    Column("aluno_id", Integer,ForeignKey("alunos.id"), primary_key=True),
    Column("curso_id", Integer,ForeignKey("cursos.id"), primary_key=True),
)




#Conxão com db
engine = create_engine("sqlite:///gestap_escolar.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)