-- Tabela de utilizadores
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

-- Tabela de categorias preferidas
CREATE TABLE IF NOT EXISTS categorias_preferidas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    categoria TEXT NOT NULL,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);

-- Tabela de favoritos
CREATE TABLE IF NOT EXISTS favoritos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    url TEXT NOT NULL,
    fonte TEXT,
    data_publicacao TEXT,
    imagem TEXT,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);
