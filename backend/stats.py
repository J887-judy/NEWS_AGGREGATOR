from flask import render_template, session, redirect, url_for
from database.db_utils import get_db

def estatisticas():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn, cursor = get_db()

    try:
        cursor.execute("SELECT COUNT(*) FROM favoritos WHERE usuario_id = ?",
                       (session["user_id"],))
        total_favoritos = cursor.fetchone()[0]

        cursor.execute("""
            SELECT categoria, COUNT(categoria)
            FROM categorias_preferidas
            WHERE usuario_id = ?
            GROUP BY categoria
        """, (session["user_id"],))
        categorias = cursor.fetchall()

        cursor.execute("""
            SELECT titulo, COUNT(titulo)
            FROM favoritos
            GROUP BY titulo
            ORDER BY COUNT(titulo) DESC
            LIMIT 5
        """)
        populares = cursor.fetchall()

        return render_template(
            "estatisticas.html",
            total_favoritos=total_favoritos,
            categorias=categorias,
            populares=populares,
            username=session.get("email")
        )
    except Exception as e:
        print(f"Erro ao gerar estatísticas: {e}")
        return render_template("error.html", message="Erro ao gerar estatísticas"), 500
    finally:
        conn.close()