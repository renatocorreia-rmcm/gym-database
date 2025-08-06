from execute_query import execute_query

# Nome e salário do funcionário que ganha mais.

query = """ 
SELECT nome, salário
FROM Funcionário
ORDER BY salário DESC
LIMIT 1;

"""

execute_query(query)
