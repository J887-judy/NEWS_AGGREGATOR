from flask import render_template, request, session, redirect, url_for
from database.db_utils import get_db

def favoritos():
    if "user_id" not in session:
        return redirect(url_for("login"))

    conn, cursor = get_db()

    try:
        if request.method == "POST":
            titulo = request.form.get("titulo", "").strip()
            url = request.form.get("url", "").strip()
            fonte = request.form.get("fonte", "").strip()
            data = request.form.get("data", "").strip()
            imagem = request.form.get("imagem", "").strip()

            if titulo and url:
                cursor.execute("""
                    INSERT INTO favoritos (usuario_id, titulo, url, fonte, data_publicacao, imagem)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    session["user_id"],
                    titulo,
                    url,
                    fonte,
                    data,
                    imagem
                ))
                conn.commit()

        cursor.execute("""
            SELECT titulo, url, fonte, data_publicacao, imagem
            FROM favoritos
            WHERE usuario_id = ?
        """, (session["user_id"],))

        favoritos_list = cursor.fetchall()

        return render_template(
            "favoritos.html",
            favoritos=favoritos_list,
            username=session.get("email")
        )
    except Exception as e:
        print(f"Erro ao acessar favoritos: {e}")
        return render_template("error.html", message="Erro ao acessar favoritos"), 500
    finally:
        conn.close()