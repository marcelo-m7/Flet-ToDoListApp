# ToDo List App

O aplicativo foi desenvolvido em Python utilizando a biblioteca Flet e está configurado para deploy no Replit, com a porta aberta 3000. A aplicação permite autenticação via GitHub e armazena as tarefas de forma segura usando criptografia.

## Requisitos

1. **Python**: Certifique-se de que o Python 3.8 ou superior está instalado.
2. **Dependências**: Instale as bibliotecas necessárias utilizando o arquivo `docs/requirements.txt`.
3. **GitHub OAuth App**: Crie um OAuth App no GitHub para obter as credenciais necessárias (`GITHUB_CLIENT_ID` e `GITHUB_CLIENT_SECRET`).

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando no terminal dentro do ambiente virtual:

```sh
pip install -r docs/requirements.txt
```

## Configuração

### 1. Criar o arquivo `.env`

Crie um arquivo `.env` dentro da pasta `src/` com as seguintes variáveis:

```plaintext
GITHUB_CLIENT_ID="seu_client_id_aqui"
GITHUB_CLIENT_SECRET="seu_client_secret_aqui"
FERNET_KEY=""  # Opcional (será gerado automaticamente se não existir)
```

### 2. Configurar host e URL pública

Para ambientes atrás de proxies ou domínios customizados, configure a URL pública e o binding do servidor via variáveis de ambiente:

- ``APP_BASE_URL``: URL externa completa (ex.: ``https://todo.mss-7.com``). Necessária quando um proxy faz o offload de HTTPS ou expõe uma porta diferente.
- ``APP_SCHEME`` e ``PUBLIC_PORT``: opções para definir manualmente o esquema (http/https) e a porta pública quando ``APP_BASE_URL`` não for usada.
- ``HOST``: nome do host externo usado como fallback ao calcular a URL base.
- ``PORT``: porta interna de execução (padrão: ``8080``).
- ``BIND_HOST``: endereço de binding do servidor (padrão: ``0.0.0.0``). Use-o se precisar separar o host de acesso externo do endereço de escuta interno.

Certifique-se de registrar no GitHub OAuth App o ``redirect_url`` gerado a partir da URL pública: ``{APP_BASE_URL}/oauth_callback``.

## Executando a Aplicação

Para iniciar a aplicação, utilize o seguinte comando no terminal:

```sh
python src/main.py
```

A aplicação estará disponível no navegador na URL correspondente à configuração do host e porta definidos no arquivo `src/main.py`.
