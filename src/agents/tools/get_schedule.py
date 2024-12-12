import datetime as dt
import requests


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
            "timeZone": "America/Sao_Paulo",  # Ajuste conforme necessário
        },
        "endTime": {
            "dateTime": end_time,
            "timeZone": "America/Sao_Paulo",
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

