import traceback
import os
import requests
from flask import render_template, request, session, redirect, url_for
from dotenv import load_dotenv
from backend.preferences import get_user_categories
from utils.ai_utils import gerar_resumo

# carregar variáveis do .env
load_dotenv()

# definir a chave da API
API_KEY = os.getenv("API_KEY") or os.getenv("CURRENTS_API", "")

DEFAULT_CATEGORIES = ["general", "technology", "business", "sports", "health", "science", "entertainment"]


# 🔥 Currents API real
def buscar_noticias(categoria=None):
    if not API_KEY:
        error = "API key ausente: defina API_KEY ou CURRENTS_API no arquivo .env"
        print(error)
        return [], error

    try:
        url = "https://api.currentsapi.services/v1/latest-news"
        params = {
            "apiKey": API_KEY,
            "language": "pt"
        }
        if categoria:
            params["category"] = categoria

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            error = data.get("message") or f"Erro na Currents API: status {response.status_code}"
            print(error)
            return [], error

        noticias = []
        for item in data.get("news", []):
            noticias.append({
                "titulo": item.get("title", "Sem título"),
                "descricao": item.get("description", "Sem descrição"),
                "fonte": item.get("author", "Desconhecido"),
                "data_publicacao": item.get("published"),
                "imagem": item.get("image", "https://via.placeholder.com/300"),
                "url": item.get("url", "#")
            })

        return noticias, None

    except Exception as e:
        error = f"Erro Currents API: {e}"
        print(error)
        return [], error



# 🧠 HOME
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    categoria = request.args.get("categoria")
    noticias = []
    errors = []
    info_message = None

    try:
        if not categoria:
            categorias = get_user_categories(session["user_id"])
            if not categorias:
                categorias = DEFAULT_CATEGORIES
                info_message = "Nenhuma preferência encontrada. Mostrando categorias padrão."

            for cat in categorias:
                noticias_cat, erro = buscar_noticias(cat)
                noticias.extend(noticias_cat)
                if erro:
                    errors.append(f"{cat}: {erro}")
        else:
            noticias, erro = buscar_noticias(categoria)
            if erro:
                errors.append(erro)
            if not noticias and not info_message:
                info_message = f"Nenhuma notícia encontrada para a categoria '{categoria}'."

        # IA (com fallback seguro)
        for n in noticias:
            try:
                n["resumo"] = gerar_resumo(n["titulo"], n["descricao"])
            except Exception:
                n["resumo"] = n["descricao"][:120]

        error_messages = errors if errors else None

        return render_template(
            "home.html",
            noticias=noticias,
            username=session.get("email"),
            info_message=info_message,
            error_messages=error_messages
        )

    except Exception as e:
      print("Erro no home:", e)
      traceback.print_exc()   # <-- isto mostra o traceback completo no terminal
      return render_template("home.html", noticias=[], username=session.get("email"))
# if categoria and categoria.lower() not in item.get("title", "").lower():
#     continue

