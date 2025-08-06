from execute_query import execute_query

query = """
SELECT A.nome, P.valor, Pr.tx_desconto
FROM Aluno A
INNER JOIN Assina S ON A.CPF_aluno = S.CPF_aluno
INNER JOIN Plano P ON S.ID_plano = P.ID_plano
INNER JOIN Promoção Pr ON S.ID_promo = Pr.ID_promo
"""

execute_query(query)
