import os
from flask import Flask, redirect, render_template, session, url_for
from dotenv import load_dotenv
from backend import auth, news, preferences, favorites, stats

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

app.secret_key = os.getenv("SECRET_KEY", "dev-key-change-in-production")

@app.route("/")
def index():
    return redirect("/home")

@app.route("/ajuda")
def ajuda():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("ajuda.html", username=session.get("email"))

app.add_url_rule("/login", view_func=auth.login, methods=["GET", "POST"])
app.add_url_rule("/register", view_func=auth.register, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=auth.logout)
app.add_url_rule("/home", view_func=news.home)
app.add_url_rule("/personalizacao", view_func=preferences.personalizacao, methods=["GET", "POST"])
app.add_url_rule("/favoritos", view_func=favorites.favoritos, methods=["GET", "POST"])
app.add_url_rule("/estatisticas", view_func=stats.estatisticas)

if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=debug_mode)
