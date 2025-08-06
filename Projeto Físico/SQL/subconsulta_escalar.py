from execute_query import execute_query

query = """
SELECT A.nome,
       (SELECT valor
        FROM Assina S JOIN Plano P ON S.ID_plano = P.ID_plano
        WHERE S.CPF_aluno = A.CPF_aluno
        LIMIT 1) AS valor_plano
FROM Aluno A;

"""

execute_query(query)
