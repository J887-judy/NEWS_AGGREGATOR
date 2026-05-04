import requests

API_KEY = "GlYUN4Wd5eh2hLmrgeOaInI-TTaXSCnGEFo7MADs00Jpf4mA"

def testar_api():
    print("🔄 Testando API do Currents...")

    try:
        url = "https://api.currentsapi.services/v1/latest-news"
        params = {
            "apiKey": API_KEY,
            "category": "general",
            "language": "pt"
        }

        print("🌐 Fazendo requisição...")
        response = requests.get(url, params=params, timeout=10)
        print(f"📊 Status code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            news_count = len(data.get("news", []))
            print(f"✅ Sucesso! {news_count} notícias encontradas")

            if news_count > 0:
                primeira = data['news'][0]
                print(f"📝 Título: {primeira.get('title', 'Sem título')[:60]}...")
                print(f"📄 Descrição: {primeira.get('description', 'Sem descrição')[:60]}...")
            else:
                print("⚠️  Nenhuma notícia retornada")
                print(f"📄 Resposta: {data}")
        else:
            print(f"❌ Erro: {response.status_code}")
            print(f"📄 Resposta: {response.text}")

    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    testar_api()