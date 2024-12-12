import datetime as dt
import os
import requests
from chain.utils.misc.response_handlers import limpa_horarios


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


def get_events():
    """
        Você é uma assistente administrativa que vai ver nossos horários disponíveis e retonar uma mensagem amigável para humanos
        com o horário aberto para a próxima reunião. Não precisa mostrar todos, a menos que o usuário peça.
        Entregue resultados somente nos próximos 7 dias.
    """
    # URL para obter os eventos
    events_url = (
        f"https://graph.microsoft.com/v1.0/users/{conn.USER_ID[2]}/calendar/events"
    )

    # Obter o token de acesso
    access_token = auth()

    # Cabeçalho da solicitação
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    params = {
        # "startDateTime": datetime.now().isoformat(),
        # "endDateTime": (datetime.now() + timedelta(days=7)).isoformat(),
        "$select": "subject,start,end,attendees",
    }

    # Solicitar os eventos
    response = requests.get(events_url, headers=headers, params=params)
    if response.status_code == 200:
        formatted_events = limpa_horarios(response.json())
        return formatted_events
    else:
        print("Erro ao obter os eventos:", response.status_code, response.json())
        return response.json()


def get_schedule():
    """
        Você é uma assistente administrativa que vai ver nossos horários disponíveis e retonar uma mensagem amigável para humanos
        com o horário aberto para a próxima reunião. Não precisa mostrar todos, a menos que o usuário peça.
        Entregue resultados somente nos próximos 7 dias.

        De preferência na estrutura:
        {dia} às {hora} com {nome do usuário}, pode ser?
    """
    # Obter o token de acesso
    access_token = auth()

    # Endpoint do Microsoft Graph para /getSchedule
    url = (
        f"https://graph.microsoft.com/v1.0/users/{conn.USER_ID[1]}/calendar/getSchedule"
    )

    # Data de hoje
    today = dt.datetime.now()

    # Data de início: agora
    start_time = today.isoformat()

    # Data de término: 7 dias úteis
    end_time = (
        today + dt.timedelta(hours=1)
    ).isoformat()  # Inclui fim de semana para garantir 7 dias úteis
    # print(start_time, end_time)
    # Corpo da requisição
    payload = {
        "schedules": [
            f"{conn.USER_ID[1]}",
            f"{conn.USER_ID[2]}",
        ],  # Substitua pelo email do usuário
        "startTime": {
            "dateTime": start_time,
            "timeZone": "UTC",  # Ajuste conforme necessário
        },
        "endTime": {
            "dateTime": end_time,
            "timeZone": "UTC",
        },  # Ajuste conforme necessário
        "availabilityViewInterval": 60,  # Intervalos de 1 hora
    }

    # Cabeçalhos
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Fazer a requisição
    response = requests.post(url, json=payload, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        availability = response.json()
        return availability
    else:
        print(f"Erro: {response.status_code}")
        # print(response.json())
        return response.content


def schedule_meeting(subject, start_time, end_time, attendees_emails):
    """
    Agenda uma reunião usando a API do Microsoft Graph.

    :param access_token: Token de acesso para autenticação na API do Microsoft Graph.
    :param subject: Título ou assunto da reunião.
    :param start_time: Data e hora de início da reunião (ISO 8601 format).
    :param end_time: Data e hora de término da reunião (ISO 8601 format).
    :param attendees_emails: Lista de e-mails dos participantes.
    :return: Resposta da API.
    """

    url = (
        f"https://graph.microsoft.com/v1.0/users/{conn.USER_ID[1]}/calendar/getSchedule"
    )
    
    access_token = auth()

    # Configura os participantes
    attendees = [
        {"emailAddress": {"address": email, "name": email.split('@')[0]}, "type": "required"}
        for email in attendees_emails
    ]

    # Corpo da solicitação
    event_data = {
        "subject": subject,
        "start": {
            "dateTime": start_time,
            "timeZone": "UTC"
        },
        "end": {
            "dateTime": end_time,
            "timeZone": "UTC"
        },
        "attendees": attendees
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=event_data)

    if response.status_code == 201:
        print("Reunião criada com sucesso!")
    else:
        print("Erro ao criar a reunião:", response.json())

    return response.json()