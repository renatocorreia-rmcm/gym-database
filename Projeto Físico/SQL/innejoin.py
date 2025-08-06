import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

# Consulta INNER JOIN entre duas tabelas: clientes e pedidos
query = """
SELECT clientes.nome, pedidos.data_pedido
FROM clientes
INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;
"""

cursor.execute(query)
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conn.close()