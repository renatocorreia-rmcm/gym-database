from physical_schema.execute_query import execute_query

query = """ 
SELECT nome
FROM Funcionário
WHERE salário = (
    SELECT MAX(salário)
    FROM Funcionário
);
"""

execute_query(query)  # pass any query you want!
