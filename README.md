# 📰 News Aggregator com Flask + Currents API + OpenAI

Este projeto é um agregador de notícias com autenticação de utilizadores, personalização por categorias e sistema de favoritos.  
Foi desenvolvido em **Python (Flask)** com integração à **Currents API** e funcionalidades inteligentes via **OpenAI API**.

---

## 🚀 Funcionalidades

### 1. Autenticação de Utilizadores
- Registo com nome completo, email e palavra-passe (armazenada com hash via `bcrypt`).
- Login com email e palavra-passe.
- Logout que termina a sessão.
- Persistência da sessão durante a navegação.
- Apenas utilizadores autenticados podem:
  - Guardar categorias preferidas.
  - Marcar artigos como favoritos.
  - Visualizar lista de favoritos.

### 2. Consulta e Exibição de Notícias
- Notícias atuais exibidas em **cards responsivos**.
- Cada card mostra: **imagem, título, descrição, resumo automático, fonte, data e link**.
- Filtro por categoria via botões.
- Paginação ou infinite scroll para navegar entre páginas de notícias.

### 3. Gestão de Preferências e Favoritos
- Página de **Personalização** para selecionar categorias favoritas.
- Preferências podem ser modificadas a qualquer momento.
- Botão “Salvar nos Favoritos” em cada card.
- Página **Favoritos** lista apenas os artigos guardados, com opção de remover.
- Armazenamento em **SQLite**.

### 4. Personalização de Conteúdo
- Página inicial mostra **primeiro as notícias das categorias favoritas** do utilizador.
- O utilizador pode navegar por outras categorias.
- Preferências são lembradas entre sessões.

### 5. Funcionalidade Inteligente
🧠 Inteligência Artificial (LOCAL – SEM OPENAI)

Este projeto utiliza **IA local baseada em Transformers**, eliminando a necessidade de APIs externas pagas.

### ✔ Funcionalidades de IA:
- Resumo automático de notícias
- Recomendações baseadas em interesses
- Análise de sentimento de texto

### ⚙ Tecnologia usada:
- `transformers`
- `torch`
- Modelo: `google/flan-t5-small`
---

## 📂 Estrutura do Projeto
news_aggregator/
├── frontend/               # Interface (HTML, CSS, JS)
├── backend/                # Lógica da aplicação (Flask)
├── database/               # Persistência (SQLite)
├── utils/                  # Funcionalidades auxiliares (IA, validação, erros)
├── requirements.txt        # Dependências
└── README.md               # Documentação

---

## ⚙️ Instalação e Configuração

### 1. Clone o repositório

```bash
git clone <seu-repo>
cd news_aggregator
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

```env
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-aqui-mude-em-producao
API_KEY=sua-api-key-currents-aqui
HF_TOKEN=seu-token-hf-aqui (opcional)
```

#### Obtendo as chaves:

**API_KEY (Currents API):**
1. Acesse https://currentsapi.services/
2. Crie uma conta e obtenha sua API key
3. Cole a chave no arquivo `.env`

**HF_TOKEN (Hugging Face - Opcional):**
1. Acesse https://huggingface.co/settings/tokens
2. Crie um novo token de acesso
3. Cole no `.env` para evitar limitações de taxa

### 5. Inicialize o banco de dados

```bash
python database/init_db.py
```

### 6. Execute a aplicação

```bash
python main.py
```

A aplicação estará disponível em: **http://127.0.0.1:5000**

---

## 🚨 Solução de Problemas

### "Sem notícias disponíveis"
- ✅ Verifique se adicionou uma `API_KEY` válida no `.env`
- ✅ Certifique-se de que selecionou categorias em "Preferências"
- ✅ Verifique sua conexão de internet
- ✅ Recarregue a página (F5)

### Modelo de IA carrega lentamente
- A primeira execução faz download do modelo (~350MB)
- Depois fica armazenado em cache localmente
- Usando `HF_TOKEN` melhora a velocidade de download

---

## 📝 Estrutura do Projeto

```
news_aggregator/
├── main.py                 # Entrada principal da aplicação
├── requirements.txt        # Dependências Python
├── .env.example           # Exemplo de variáveis de ambiente
│
├── backend/               # Lógica de negócio
│   ├── __init__.py
│   ├── auth.py           # Autenticação (login/registro)
│   ├── news.py           # Busca de notícias
│   ├── preferences.py    # Gerenciamento de preferências
│   ├── favorites.py      # Gestão de favoritos
│   └── stats.py          # Estatísticas do usuário
│
├── database/             # Persistência
│   ├── __init__.py
│   ├── db_utils.py       # Utilidades de conexão BD
│   ├── init_db.py        # Inicialização do BD
│   └── schema.sql        # Schema do banco
│
├── utils/                # Utilidades
│   ├── ai_utils.py       # Funções de IA (resumo, recomendação, sentimento)
│   ├── validators.py     # Validação de entradas
│   └── error_handler.py  # Tratamento de erros
│
├── templates/            # HTML
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── personalizacao.html
│   ├── favoritos.html
│   ├── estatisticas.html
│   ├── ajuda.html        # Central de Ajuda
│   └── error.html
│
└── static/               # CSS/JS
    ├── style.css         # Estilos
    └── app.js            # JavaScript
```