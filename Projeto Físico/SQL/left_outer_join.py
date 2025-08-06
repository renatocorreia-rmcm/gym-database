from execute_query import execute_query

query = """ SELECT te.ID_treino
FROM
  TreinoEquipamento AS te
LEFT JOIN
  TreinoExercício AS te2 ON te.ID_treino = te2.ID_treino;

"""
execute_query(query)
