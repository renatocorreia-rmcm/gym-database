from execute_query import execute_query

# Lista todos os funcionários e, se houver, o nome do seu supervisor.

query = """ 
SELECT F1.nome AS funcionario, F2.nome AS supervisor
FROM Funcionário F1
LEFT JOIN Funcionário F2 ON F1.CPF_supervisor = F2.CPF_func;

"""

execute_query(query)
