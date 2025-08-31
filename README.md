# Gym database

Implementation of a database to a fictional gym, passing through _conceitual_, _logical_ and _physical_ phases of the database project.

## Tools

SQLite3 API for python

## How to use it ?

Initialize the DataBase simply running `initialize.py` in `./gym-database/physical_schema/initialize.py`.

Now, at main, you can run any query you want in our preloaded Database. Or check out some ready queries at `gym-database\physical_schema\querys`.


## Directory Tree

```
GYM-DATABSE
|   .gitignore
|   main.py
|   README.md
|
|
+---conceitual_schema
|       projetoBD.eer
|       projetoBD.png
|
+---logical_schema
|       Projeto Lógico - BD.pdf
|
\---physical_schema
    |   execute_query.py
    |   initialize.py
    |
    +---initialization
    |   |   create_tables.py
    |   |   populate_tables.py
    |   |
    |   \---__pycache__
    |           create_tables.cpython-312.pyc
    |           populate_tables.cpython-312.pyc
    |
    +---querys
    |       anti_join.py
    |       full_outer.py
    |       groupby.py
    |       inner_join.py
    |       left_outer_join.py
    |       semi_join.py
    |       subconsulta_escalar.py
    |       subconsulta_linha.py
    |       subconsulta_tabela.py
    |       union.py
    |
    \---__pycache__
            execute_query.cpython-312.pyc
            initialize.cpython-312.pyc
```