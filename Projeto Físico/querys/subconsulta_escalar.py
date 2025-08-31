from execute_query import execute_query

# Nome do funcionário com o maior salário.

query = """ 
SELECT nome
FROM Funcionário
WHERE salário = (
    SELECT MAX(salário)
    FROM Funcionário
);
"""

execute_query(query)
