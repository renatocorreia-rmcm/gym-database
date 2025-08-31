# Gym database

Implementation of a database to a fictional gym, passing through _conceitual_, _logical_ and _physical_ schemas of the database project.

## Tools

SQLite3 API for python

## How to use it ?

1. Initialize the DataBase simply running `initialize.py` in `./gym-database/physical_schema/initialize.py`.
   
<img width="1920" height="1080" alt="initialize script" src="https://github.com/user-attachments/assets/d9a19fdd-609f-4ea8-9cd8-579bd2d9b6f9" />
Result of initialize.py script. <br> <br>

<img width="1920" height="1080" alt="created  db" src="https://github.com/user-attachments/assets/cf843975-d43d-42fa-a1dd-2ef618fa8b21" />
DataBase schema was created. <br> <br>

<img width="1920" height="1080" alt="populated  db" src="https://github.com/user-attachments/assets/28b4ba17-3c38-41db-86e5-fd09dcce028b" />
DataBase was also populated. <br> <br>

2. Have fun!
   
    Now, at main, you can run any query you want in our preloaded Database.
    <img width="1920" height="1080" alt="executing queries" src="https://github.com/user-attachments/assets/185d2810-2efd-4536-9870-8d49cb3a7dfa" />
   
    Or check out some ready queries at `gym-database\physical_schema\querys`.
    <img width="1920" height="1080" alt="Ready querie" src="https://github.com/user-attachments/assets/70bc1ec7-09ab-4e74-9dcd-5a536151dc23" />









   

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
    \---querys                      # ready queries to test database integrity
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
