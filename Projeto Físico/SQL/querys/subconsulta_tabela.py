from execute_query import execute_query

# Listar todos os equipamentos usados em algum treino.

query = """ 
SELECT E.nome
FROM Equipamento E
WHERE E.ID_equipamento IN (
    SELECT T.ID_equip
    FROM TreinoEquipamento T
);

"""

execute_query(query)
