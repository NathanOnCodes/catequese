# Backend Catequese

Backend para sistema de gestão de catequese, desenvolvido com Django e Django Ninja.

## Tecnologias

- **Django** - Framework web Python
- **Django Ninja** - API REST com FastAPI-like syntax
- **Django REST Framework** - API REST
- **Simple JWT** - Autenticação JWT
- **SQLite** - Banco de dados (configurável)

## Configuração

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install django django-ninja djangorestframework djangorestframework-simplejwt python-dotenv django-cors-headers
   ```
4. Configure o arquivo `.env` com suas variáveis de ambiente
5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Endpoints de Autenticação

- `POST /api/auth/login` - Login com username e password
- `POST /api/auth/refresh` - Refresh do token JWT
- `GET /api/auth/me` - Dados do usuário autenticado

## Estrutura do Projeto

```
backend_catequese/
├── auth/              # App de autenticação
│   ├── routes/        # Endpoints da API
│   └── schemas/       # Schemas de validação
├── core/              # Configurações do projeto
├── .env               # Variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo git
└── manage.py          # Script de gerenciamento Django
```
