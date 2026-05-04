import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN", "")
modelo = None


def _carregar_modelo():
    global modelo
    if modelo is not None:
        return modelo

    try:
        if HF_TOKEN:
            os.environ["HUGGINGFACEHUB_API_TOKEN"] = HF_TOKEN

        from transformers import pipeline
        modelo = pipeline("text-generation", model="distilgpt2")
        return modelo
    except Exception as e:
        print(f"Aviso: não foi possível carregar o modelo de IA. Fallback será usado. Erro: {e}")
        modelo = None
        return None


def gerar_resumo(titulo, descricao):
    modelo_atual = _carregar_modelo()
    if not modelo_atual:
        return descricao[:120] + "..."

    try:
        prompt = f"Resuma em uma frase: Título: {titulo}. Descrição: {descricao}"
        result = modelo_atual(prompt, max_length=60)
        return result[0]["generated_text"]
    except Exception as e:
        print(f"Erro ao gerar resumo: {e}")
        return descricao[:120] + "..."


def recomendar_artigos(categorias, favoritos):
    try:
        prompt = f"Com base em {categorias} e favoritos {favoritos}, sugira 3 artigos."
        result = modelo(prompt, max_length=120)
        return result[0]["generated_text"]
    except:
        return "Sem recomendações disponíveis"


def analisar_sentimento(texto):
    try:
        prompt = f"Classifica o sentimento: positivo, negativo ou neutro. Texto: {texto}"
        result = modelo(prompt, max_length=20)
        return result[0]["generated_text"]
    except:
        return "neutro"