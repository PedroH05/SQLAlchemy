from sqlalchemy import create_engine, MetaData, Table, ForeignKey, Column
from sqlalchemy import Integer, String, text


engine = create_engine("sqlite:///:memory:", echo=False)

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(40)),
    Column("email_addres", String(60)),
    Column("nickname", String(50), nullable=False),
)

users_prefs = Table(
    "user_prefs",
    metadata_obj,
    Column("pref_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
    Column("pref_name", String(40), nullable=False),
    Column("pref_valeu", String(100)),
)

print("\nInfo da tabela users_prefs")
print(users_prefs.primary_key)
print(users_prefs.constraints)

print("\nTabelas no metadata:")
print(metadata_obj.tables)

for table in metadata_obj.sorted_tables:
    print(table.name)

# cria tabelas
metadata_obj.create_all(engine)


with engine.begin() as conn:
    conn.execute(
        text("insert into user (user_id, user_name, email_addres, nickname) values (:id, :name, :email, :nick)"),
        {"id": 2, "name": "Maria", "email": "email@email.com", "nick": "Ma"},
    )

    print("\nExecutando statement sql")
    result = conn.execute(text("select * from user"))
    for row in result:
        print(row)


