# Como o sqlite possui apenas a função de left outer join nativa, para se obter um rigth outer join ou um outer full join é necessário usar de alguns artifícios
#No caso do right outer join, se deve inverter as tabelas e logo após realizar o left join
#E no caso do outer full join, se deve realizar o right outer join modificado em união com o left outer join 


from execute_query import execute_query

query = """ SELECT te.ID_treino
FROM TreinoEquipamento AS te
LEFT JOIN TreinoExercício AS te2 ON te.ID_treino = te2.ID_treino

UNION

SELECT tx.ID_exercício
FROM TreinoExercício AS tx
LEFT JOIN TreinoEquipamento AS te2 ON tx.ID_treino = te2.ID_treino;
"""

execute_query(query)
