import os

from dotenv import load_dotenv


def load_env_file(env_file_path="src/.env"):
    """
    Carrega variáveis de ambiente de um arquivo .env.

    Args:
        env_file_path (str): Caminho para o arquivo .env.
    """

    load_dotenv(env_file_path)


def get_env_variable(key, default=None):
    """
    Obtém uma variável de ambiente ou retorna um valor padrão.

    Args:
        key (str): Nome da variável de ambiente.
        default: Valor padrão caso a variável não exista.

    Returns:
        Valor da variável de ambiente ou o valor padrão.
    """

    return os.getenv(key, default)


def build_base_url():
    """
    Determina a URL base acessível externamente para o app.

    Respeita a variável ``APP_BASE_URL`` (útil quando a aplicação
    está atrás de um proxy) e, na ausência dela, infere o esquema e
    porta adequados a partir de ``HOST`` e ``PORT``.
    """

    app_base_url = os.getenv("APP_BASE_URL")
    if app_base_url:
        return app_base_url.rstrip("/")

    host = os.getenv("HOST", "localhost")
    scheme = os.getenv("APP_SCHEME")

    if not scheme:
        scheme = "http" if host in ("localhost", "127.0.0.1", "0.0.0.0") else "https"

    public_port = os.getenv("PUBLIC_PORT")

    if host in ("localhost", "127.0.0.1", "0.0.0.0"):
        public_port = public_port or os.getenv("PORT", "8080")

    if public_port and not ((scheme == "http" and public_port == "80") or (scheme == "https" and public_port == "443")):
        return f"{scheme}://{host}:{public_port}"

    return f"{scheme}://{host}"
