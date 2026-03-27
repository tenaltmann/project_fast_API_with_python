from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey       # Column, String, Integer, Boolean, Float - são os tipos de dados que serão usados tabelas      ForeingKey = func usado para fazer a conexão entre as tabelas
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType


# criando a conexão com o banco de dados 
db = create_engine("sqlite:///banco.db")    # apontamento do caminho do banco de dados


# criando a base de dados
Base = declarative_base()       # Base sera a variavel que vai permitir a criação da tabela no banco, por isso deve ser passada como parametro nas classes

# criando as classes / tabelas do banco de dados

# Classe usuário
class Usuario(Base):
    __tablename__= "usuarios"       # por padrao a tabela pega o nome definido da classe em lowercase, ja com o __tablename__ conseguimos escolher o nome da tabela) 

    # restrição de como o banco de dados será construido
    id = Column ("id", Integer, primary_key=True, autoincrement=True)      # ("id", Integer, primary_key=True, autoincrement=True)     => a coluna id sera a chave primaria da classe para que não haja repetição, e autoincrement serve criar o proximo uaurio em ordem numerica     
    nome  =Column("nome", String, nullable=False)     #    id = Column ("id", Integer, nullable=False)    |    id= Column => essa coluna tera um id unico         ("id", Integer, nullable=False)     => sera um inteiro e NÃO pode ser nulo (ou seja, não pode ser criada sem este item)
    email =Column("email", String, nullable=False)
    senha =Column("senha", String, nullable=False)
    ativo =Column("ativo", Boolean)
    admin =Column("admin", Boolean, default=False)      # ("admin", Boolean, default=False)    => default=False por padrão este parametro sera falso, ou seja nao será admin por padrão

    # restrição de como a função será construida
    def __init__ (self, nome, email, senha, ativo=True, admin=False):      # função executada sempre na criação do usuário, e recebe self como parametro por que se refere a ele mesmo, por padrao toda funçao dentro de uma classe tem o parametro self para dizer respeio a classe que voce esta editando no momento

        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

# Classe pedido
class Pedido(Base):
    __tablename__= "pedidos"

    # TUPLA DE TUPLAS para definir o status do pedido para impossibilitar um status diferente dos predeterminados
    STATUS_PEDIDO = (
          #chave        #valor
        ("PENDENDTE", "PENDENDTE")
        ("CANCELADO", "CANCELADO")
        ("FINALIZADO","FINALIZADO")
    )


    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column ("status", ChoiceType(STATUS_PEDIDO))           # ChoiceType - limita o status aos 3 tipos definidos em STATUS_PEDIDO 
    usuario = Column("usuario", ForeignKey("usuarios.id"))          # ForeignKey - O ForeignKey("usuarios.id") referencia o nome da tabela e a coluna no banco de dados
    preco = Column("preco", Float)

    def __init__ (self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario 
        self.status = status 
        self.preco = preco

# Classe ItensPedido

class ItensPedido(Base):
    __tablename__= "itens_pedido"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column ("quantidade", Integer)
    sabor = Column ("sabor", String )
    tamanho = Column ("tamanho")
    preco_unitario = ("preco_unitario",Float)
    pedido = ("pedido", ForeignKey("pedidos.id"))

        
# executando a criação dos metadados do banco (Cria efetivamenet o banco de dados)