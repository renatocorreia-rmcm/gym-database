from execute_query import execute_query

# Alunos que possuem algum plano assinado

query = """
SELECT nome
FROM Aluno A
WHERE EXISTS (
	SELECT 1
	FROM Assina S
	WHERE S.CPF_aluno = A.CPF_aluno);
"""

execute_query(query)