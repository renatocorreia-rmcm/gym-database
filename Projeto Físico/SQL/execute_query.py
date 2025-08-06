import sqlite3


def execute_query(query):
    conn = sqlite3.connect("academia.db")
    cursor = conn.cursor()

    try:
        cursor.execute(query)

        # Captura os nomes das colunas
        colunas = [desc[0] for desc in cursor.description]

        # Resultados como lista de dicionários (opcional, mas mais legível)
        resultados = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

        print(f"\nConsulta executada com sucesso:\n{query}\n")
        for linha in resultados:
            print(linha)

    except Exception as e:
        print("Erro ao executar a consulta:", e)
    finally:
        conn.close()
