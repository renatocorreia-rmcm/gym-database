from execute_query import execute_query

query = """ SELECT Treino.equipamento.ID_treino, TreinoExercício.ID_exercício
FROM TreinoEquipamento
LEFT JOIN TreinoEquipamento ON TreinoEquipamento.ID_treino = TreinoExercício.ID_treino
"""

execute_query(query)