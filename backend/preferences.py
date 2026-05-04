from flask import render_template, request, session, redirect, url_for
from database.db_utils import get_db

def personalizacao():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn, cursor = get_db()

    try:
        if request.method == "POST":
            categorias = request.form.getlist("categorias")

            cursor.execute(
                "DELETE FROM categorias_preferidas WHERE usuario_id = ?",
                (session["user_id"],)
            )

            for cat in categorias:
                cat = cat.strip()
                if cat:
                    cursor.execute(
                        "INSERT INTO categorias_preferidas (usuario_id, categoria) VALUES (?, ?)",
                        (session["user_id"], cat)
                    )

            conn.commit()
            return redirect(url_for("home"))

        return render_template("personalizacao.html")
    except Exception as e:
        print(f"Erro na personalização: {e}")
        return render_template("error.html", message="Erro ao atualizar preferências"), 500
    finally:
        conn.close()


def get_user_categories(usuario_id):
    conn, cursor = get_db()

    try:
        cursor.execute(
            "SELECT categoria FROM categorias_preferidas WHERE usuario_id = ?",
            (usuario_id,)
        )
        return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Erro ao obter categorias: {e}")
        return []
    finally:
        conn.close()