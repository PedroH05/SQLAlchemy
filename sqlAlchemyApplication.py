import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import func


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fullname =  Column(String, nullable=False)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    #atributos
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"

print(User.__tablename__)
print(Address.__tablename__)

#conex'ao com o banco de dados
engine = create_engine("sqlite://")

#criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

#depreciado - sera removido em futuro realease
#print(engine.table_names())

#investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

#schemas
with Session(engine) as session:
    juliana = User(
        name="Juliana",
        fullname="Juliana Mascarenhas",
        address=[Address(email_address="julianam@email.com")]
    )

    sandy = User(
        name="Sandy",
        fullname="Sandy Cardoso",
        address=[
            Address(email_address="sandy@email.br"),
            Address(email_address="sandyc@email.org")
        ]
    )

    patrick = User(
        name="Patrick",
        fullname="Patrick Cardoso"
    )

    session.add_all([juliana, sandy, patrick])
    session.commit()

    stmt = select(User).where(User.name.in_(["Juliana", "Sandy"]))
    print("\nRecuperando usuarios a partir de condicao de filtragem.")
    for user in session.scalars(stmt):
        print(user)

    stmt_address = select(Address).where(Address.user_id.in_([2]))
    print("\nRecuperando os enderecos de email de sandy")
    for address in session.scalars(stmt_address):
        print(address)

print()

order_stmt_cresc = select(User).order_by(User.fullname)
print("\nRecuperando info de maneira ordenada crescente")
for result in session.scalars(order_stmt_cresc):
    print(result)

order_stmt = select(User).order_by(User.fullname.desc())
print("\nRecuperando info de maneira ordenada decrescente")
for result in session.scalars(order_stmt):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print()
    print(result)

#print(select(User.fullname, Address.email_address).join_from(Address, User))

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)


stmt_count = select(func.count('*')).select_from(User)
print("\ntotal de instancias em users")
for result in session.scalars(stmt_count):
    print(result)
