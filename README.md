# Gym database
Implementation of a database to a fictional gym, passing through _conceitual_, _logical_ and _physical_ phases of the database project.

## Tools
SQLite3 API for python

## Directory Tree
```
GYM-DATABASE                        
|   .gitignore
|   README.md
|
+---Projeto Conceitual                 # Conceitual Schema for DataBase
|       projetoBD.eer
|       projetoBD.png
|
+---Projeto Físico                     # Tables initialization
|   |   create_tables.py
|   |   main.py
|   |   populate_tables.py
|   |
|   \---querys                         # Miscelaneous queryes to test Schema integrity
|           anti_join.py
|           execute_query.py
|           full_outer.py
|           groupby.py
|           inner_join.py
|           left_outer_join.py
|           semi_join.py
|           subconsulta_escalar.py        
|           subconsulta_linha.py
|           subconsulta_tabela.py
|           union.py
|
\---Projeto Lógico                     # Logical Schema for DataBase
        Projeto Lógico - BD.pdf
```
