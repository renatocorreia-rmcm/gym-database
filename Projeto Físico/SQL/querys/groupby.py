from execute_query import execute_query

query = """
SELECT ID_uni, AVG(salário) AS media_salarial
FROM Funcionário
GROUP BY ID_uni
HAVING AVG(salário) > 3000;
"""

execute_query(query)
