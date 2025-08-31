from execute_query import execute_query

# Média salarial dos funcionários por unidade, listando apenas unidades com média acima de 3000.

query = """
SELECT ID_uni, AVG(salário) AS media_salarial
FROM Funcionário
GROUP BY ID_uni
HAVING AVG(salário) > 3000;
"""

execute_query(query)
