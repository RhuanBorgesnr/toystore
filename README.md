# ToyStore API

## Instalação

1. Clone o repositório e acesse a pasta do projeto:
   ```bash
   git clone <repo-url>
   cd toystore
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   # ou
   pyenv virtualenv 3.7.9 toy_store
   pyenv activate toy_store
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   # Para desenvolvimento/testes:
   pip install pytest pytest-django pytest-cov model_bakery
   ```

## Como rodar o projeto

1. Acesse a pasta `api`:
   ```bash
   cd api
   ```

2. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

3. (Opcional) Popule o banco com dados de exemplo (isso irá apagar clientes e vendas existentes!):
   ```bash
   python manage.py populate_demo_data
   ```

4. Crie um superusuário para acessar o admin e gerar tokens:
   ```bash
   python manage.py createsuperuser
   ```
   Siga as instruções interativas para definir username, email, nome completo, data de nascimento e senha.

5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## Autenticação e geração de token JWT

Para acessar os endpoints protegidos, gere um token JWT usando o endpoint `/api/token/`:

- Faça uma requisição POST para `/api/token/` com seu `username` e `password`:

   ```bash
   curl -X POST http://localhost:8000/api/token/ \
     -H 'Content-Type: application/json' \
     -d '{"username": "<seu_username>", "password": "<sua_senha>"}'
   ```

- O retorno será um JSON com `access` e `refresh`. Use o valor de `access` no header `Authorization`:

   ```http
   Authorization: Bearer <access_token>
   ```

- Para acessar o admin, vá para `http://localhost:8000/admin/` e use o superusuário criado.

> **Atenção:**
> Após criar o superusuário com `python manage.py createsuperuser`, acesse o admin (`/admin/`), após será possível autenticar e obter o token JWT normalmente.

## Como rodar os testes

1. Volte para a raiz do projeto:
   ```bash
   cd ..
   ```
2. Execute:
   ```bash
   pytest --cov=.
   ```
   Os testes usam o banco em modo reutilizável e cobrem API e lógica de negócio.

## Endpoints principais
- Autenticação JWT: `/api/token/` (POST)
- Refresh do token: `/api/token/refresh/` (POST)
- Clientes: `/api/customers/`
- Vendas: `/api/sales/`
- Estatísticas de vendas por dia: `/api/sales/statistics/`
- Estatísticas de clientes: `/api/sales/customers/statistics/`

---

Pronto para uso e testes. 