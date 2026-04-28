# Flask CRUD App

Projeto didático de **CRUD completo com Flask + SQLite**, ideal para iniciantes aprenderem desenvolvimento web com Python.

## 🚀 Funcionalidades

- ✅ Criar produtos
- ✅ Listar produtos
- ✅ Editar produtos
- ✅ Excluir produtos
- ✅ Banco de dados SQLite
- ✅ Templates HTML
- ✅ CSS básico
- ✅ Estrutura simples e organizada

---

# 📁 Estrutura do Projeto

```bash
flask_crud/
│── venv/
│── app.py
│── database.db
│── requirements.txt
│── README.md
│── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
│── static/
│   └── style.css

⚙️ Requisitos
Python 3.10+
pip

🔧 Instalação
1. Clonar projeto
git clone https://github.com/seuusuario/flask_crud.git
cd flask_crud
2. Criar ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Instalar dependências
pip install flask

ou

pip install -r requirements.txt
▶️ Executar Projeto
python app.py

Acesse no navegador:

http://127.0.0.1:5000
🗃️ Banco de Dados

O projeto usa SQLite.

O arquivo será criado automaticamente:

database.db

Tabela:

produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL
)
📌 Rotas
Método	Rota	Função
GET	/	Listar produtos
GET/POST	/add	Adicionar produto
GET/POST	/edit/<id>	Editar produto
GET	/delete/<id>	Excluir produto
📚 Tecnologias Utilizadas
Python
Flask
SQLite
HTML5
CSS3
🎯 Objetivo Educacional

Este projeto foi criado para ensinar:

Rotas Flask
Templates Jinja2
Formulários HTML
CRUD completo
Banco SQLite
Organização de projeto
🔥 Melhorias Futuras
Login de usuário
Bootstrap
SQLAlchemy
API REST
Upload de imagens
Busca de produtos
Paginação
👨‍💻 Autor

Rodrigo Barbosa

📄 Licença

MIT