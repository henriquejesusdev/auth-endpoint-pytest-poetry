# Auth Endpoint + Pytest (Poetry)

Projeto de exemplo para validar um **endpoint de autenticação** (sucesso e erro) usando **pytest**.

## Requisitos do exercício
- Existe um usuário fixo com email e senha pré-definidos.
- Endpoint `/auth` valida credenciais:
  - **200** com token + mensagem quando correto
  - **401** quando incorreto

## Estrutura

```text
.
├── src/
│   └── auth_app/
│       ├── __init__.py
│       └── app.py
└── tests/
    └── test_auth.py
```

## Como rodar

```bash
poetry install
poetry run pytest
```

## Credenciais corretas (fixas)
- email: `user@example.com`
- senha: `123456`
