from execute_query import execute_query

# Nome e salário do funcionário que ganha mais.

query = """ 
SELECT nome, salário
FROM Funcionário
WHERE (salário, nome) = (
  SELECT MAX(salário), nome
  FROM Funcionário
);

"""

execute_query(query)
