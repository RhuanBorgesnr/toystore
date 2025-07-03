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

## Banco de Dados e Inicialização Rápida

Esta aplicação utiliza o banco de dados SQLite. O arquivo `db.sqlite3` já está incluso no repositório para facilitar os testes e a validação.

Você pode iniciar a aplicação de duas formas:

### 1. Utilizando o banco incluso (`db.sqlite3`)

O banco já contém dados de exemplo e dois usuários padrão:

- **Usuário:** usuario_teste
- **Senha:** teste123
- **Token de autenticação (usuario_teste):** eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzgzMTA5MTIyLCJpYXQiOjE3NTE1NzMxMjIsImp0aSI6IjVlOTlmZmFiNjhjYjQ2NzBhYmM2NzNkZjg1NmIwMThhIiwidXNlcl9pZCI6MzF9.ZcQ1wIYnnnoPH5CYlWxNYZ93aro89fUtMnd9hbIUatY



> Este token deve ser colocado no arquivo `.env`, por exemplo:
>
> ```env
> REACT_APP_JWT_TOKEN=SEU_TOKEN_AQUI
> ```

Assim, é possível autenticar e testar a API imediatamente.

### 2. Criando tudo do zero

Se preferir iniciar com um banco limpo, siga os comandos abaixo:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Após criar o superusuário, gere seu próprio token de autenticação e atualize o `.env` com ele.

---

📝 **Atenção:** Esta documentação permite que avaliadores testem a API tanto com o banco pronto quanto a partir de uma instalação limpa, garantindo praticidade e flexibilidade no processo de validação.

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

## Autenticação e Token

Após criar o usuário e gerar o token de autenticação, adicione o token ao arquivo `.env` na raiz do frontend (ui/), por exemplo:

```
REACT_APP_API_TOKEN=seu_token_aqui
```

Certifique-se de reiniciar o servidor do frontend após alterar o .env.

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

