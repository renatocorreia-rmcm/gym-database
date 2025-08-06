import sqlite3

conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

# Consulta: Lista de alunos e os planos que assinaram (com desconto).
query = """
SELECT A.nome, P.valor, Pr.tx_desconto
FROM Aluno A
INNER JOIN Assina S ON A.CPF_aluno = S.CPF_aluno
INNER JOIN Plano P ON S.ID_plano = P.ID_plano
INNER JOIN Promoção Pr ON S.ID_promo = ID_promo
"""

cursor.execute(query)
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

conn.close()