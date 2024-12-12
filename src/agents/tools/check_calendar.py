import requests


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
        #"startDateTime": dt.datetime.now().isoformat(),
        #"endDateTime": (dt.datetime.now() + dt.timedelta(days=7)).isoformat(),
        "$select": "subject,start,end,attendees",
    }

    # Solicitar os eventos
    response = requests.get(events_url, headers=headers, params=params)

    if response.status_code == 200:
        formatted_events = limpa_horarios(response)
        print(formatted_events)
        return formatted_events
    else:
        print("Erro ao obter os eventos:", response.status_code, response.json())
        return response.json()

