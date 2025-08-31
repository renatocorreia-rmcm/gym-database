from physical_schema.execute_query import execute_query

# Mostra nomes dos alunos que não têm treino atribuído

query = """
SELECT A.nome
FROM Aluno A
WHERE NOT EXISTS (
    SELECT 1 FROM Atribui AT WHERE AT.CPF_aluno = A.CPF_aluno
);
"""

execute_query(query)
