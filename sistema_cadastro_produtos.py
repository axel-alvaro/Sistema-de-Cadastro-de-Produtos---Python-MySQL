import mysql.connector



conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="40028922Xx123@",
    database="portfolio_db"
)

cursor = conexao.cursor()


print("Conectado ao MySQL com sucesso!")



nome = input("Nome do produto: ")
categoria = input("Categoria: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))


sql = """
INSERT INTO produtos(nome, categoria, preco, quantidade)
VALUES (%s, %s, %s, %s)
"""


valores = (nome, categoria, preco, quantidade)


cursor.execute(sql, valores)

conexao.commit()


print("Produto cadastrado com sucesso!")


# Mostrar produtos cadastrados
cursor.execute("SELECT * FROM produtos")

produtos = cursor.fetchall()


print("\n=== PRODUTOS ===")

for produto in produtos:
    print(produto)


cursor.close()
conexao.close()