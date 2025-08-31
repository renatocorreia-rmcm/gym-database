from physical_schema.execute_query import execute_query

# Lista de CPFs de todos os envolvidos na academia (alunos ou funcionários).

query = """ 
SELECT CPF_func AS CPF
FROM Funcionário
UNION
SELECT CPF_aluno
FROM Aluno;

"""

execute_query(query)
