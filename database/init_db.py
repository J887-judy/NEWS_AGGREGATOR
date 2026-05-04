import sqlite3

def init_db():
    conn = sqlite3.connect("news_aggregator.db")
    cursor = conn.cursor()

    # Ler o schema.sql e executar
    with open("database/schema.sql", "r", encoding="utf-8") as f:
        schema = f.read()
        cursor.executescript(schema)

    conn.commit()
    conn.close()
    print("Base de dados inicializada com sucesso!")

if __name__ == "__main__":
    init_db()
