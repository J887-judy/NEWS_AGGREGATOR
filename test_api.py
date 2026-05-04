import os
import requests
from dotenv import load_dotenv

print("🔄 Iniciando teste da API...")

load_dotenv()

API_KEY = os.getenv("API_KEY") or os.getenv("CURRENTS_API", "")
print(f"🔑 API_KEY presente: {bool(API_KEY)}")

def testar_api():
    if not API_KEY:
        print("❌ API key ausente")
        return

    print(f"🔑 API Key encontrada: {API_KEY[:10]}...")

    try:
        url = "https://api.currentsapi.services/v1/latest-news"
        params = {
            "apiKey": API_KEY,
            "category": "general",
            "language": "pt"
        }

        print("🌐 Fazendo requisição para Currents API...")
        response = requests.get(url, params=params, timeout=10)
        print(f"📊 Status code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            news_count = len(data.get("news", []))
            print(f"✅ Sucesso! Encontradas {news_count} notícias")
            if news_count > 0:
                print(f"📝 Primeira notícia: {data['news'][0]['title'][:50]}...")
            else:
                print("⚠️  Nenhuma notícia retornada pela API")
                print(f"📄 Resposta completa: {data}")
        else:
            print(f"❌ Erro na API: {response.text}")

    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    testar_api()