# Gym database
Implementation of a database to a fictional gym, passing through _conceitual_, _logical_ and _physical_ phases of the database project.

## Tools
SQLite 3 API for python

## Directory Tree
```
gym-databse
|   .gitignore
|
+---Projeto Conceitual
|       projetoBD.eer
|       projetoBD.png
|
+---Projeto Físico
|   +---SQL
|       |   create_tables.py
|       |   main.py
|       |   populate_tables.py
|       |
|       +---querys
|       |   |   anti_join.py
|       |   |   execute_query.py
|       |   |   full_outer.py
|       |   |   groupby.py
|       |   |   inner_join.py
|       |   |   left_outer_join.py
|       |   |   semi_join.py
|       |   |   subconsulta_escalar.py
|       |   |   subconsulta_linha.py
|       |   |   subconsulta_tabela.py
|       |   |   union.py
|       |   |
|       |   \---__pycache__
|       |           execute_query.cpython-312.pyc
|       |
|       \---__pycache__
|               create_tables.cpython-312.pyc
|               populate_tables.cpython-312.pyc
|
\---Projeto Lógico
        Projeto Lógico - BD.pdf
```