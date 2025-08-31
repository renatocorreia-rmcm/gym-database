# Gym database

Implementation of a database to a fictional gym, passing through _conceitual_, _logical_ and _physical_ phases of the database project.

## Tools

SQLite3 API for python

## How to use it ?

1. Initialize the DataBase simply running `initialize.py` in `./gym-database/physical_schema/initialize.py`.

2. Have fun!
   
    Now, at main, you can run any query you want in our preloaded Database.
   
    Or check out some ready queries at `gym-database\physical_schema\querys`.

## Directory Tree

```
GYM-DATABASE
|   .gitignore
|   main.py                         # run any query you want (with database initialized)
|   README.md
|
+---conceitual_schema
|       projetoBD.eer
|       projetoBD.png
|
+---logical_schema
|       Projeto Lógico - BD.pdf
|
\---physical_schema
    |   execute_query.py            # automatize execution of string as sql query to database
    |   initialize.py               # create and populate tables
    |
    +---initialization
    |       create_tables.py
    |       populate_tables.py
    |
    \---querys                      # ready querys to test database integrity
            anti_join.py
            full_outer.py
            groupby.py
            inner_join.py
            left_outer_join.py
            semi_join.py
            subconsulta_escalar.py
            subconsulta_linha.py
            subconsulta_tabela.py
            union.py
```
