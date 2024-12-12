import os
import requests


class AZURE:
    TENANT_ID = os.getenv("AZURE_TENANT_ID")
    CLIENT_ID = os.getenv("AZURE_CLIENT")
    CLIENT_SECRET = os.getenv("AZURE_SECRET_VALUE")
    SCOPE = {
        1: "Calendars.ReadWrite",
        2: "client_credentials",
        3: "organizations",
        4: ".default",
    }
    USER_ID = {1: os.getenv("AZURE_USER_ID_BRUNO"), 2: os.getenv("AZURE_USER_ID_PEDRO")}


# instancia da classe AZURE
conn = AZURE()


def auth():
    # URL para solicitar o token
    token_url = f"https://login.microsoftonline.com/{conn.TENANT_ID}/oauth2/v2.0/token"

    # Dados da solicitação
    token_data = {
        "grant_type": "client_credentials",
        "client_id": conn.CLIENT_ID,
        "client_secret": conn.CLIENT_SECRET,
        "scope": conn.SCOPE[4],
    }

    # Solicitar o token de acesso
    response = requests.post(token_url, data=token_data)
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        # print("Access Token:", access_token)
        return access_token
    else:
        print("Erro ao obter o token:", response.status_code, response.json())
        return response.json()