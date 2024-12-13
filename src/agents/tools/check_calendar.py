import requests
from src.utils.external_apis.microsoft.graph import *
from src.utils.misc.response_handlers import *
from langchain_core.tools import tool
# Import things that are needed generically
# from langchain.pydantic_v1 import Field
from langchain.tools import tool
import json


def check_calendar()-> json:
    """
    Recebe e formata horários dos eventos de calendário dos donos da Socium.

    Ela formata os dados dos eventos e os retorna como um objeto JSON. Em caso de erro, retorna
    a resposta de erro.

    Retorna:
        json: Um objeto JSON contendo os eventos de calendário formatados, ou a resposta de erro
        caso a solicitação falhe.

    Lança:
        Exception: Se houver um problema com a autenticação ou a solicitação à API.

    Exemplo:
        >> check_calendar()
        {
            "retorno da funcao": {
                "meetings": [
                    {
                        "end": {
                            "dateTime": "Thu, 19 Dec 2024 11:30:00 GMT"
                        },
                        "start": {
                            "dateTime": "Thu, 19 Dec 2024 11:00:00 GMT"
                        }
                    },
                    {
                        "end": {
                            "dateTime": "Wed, 18 Dec 2024 11:30:00 GMT"
                        },
                        "start": {
                            "dateTime": "Wed, 18 Dec 2024 11:00:00 GMT"
                        }
                    }
                ],
                "never_available": {
                    "end": "14:00",
                    "start": "12:00"
                },
                "working_hours": {
                    "end": "18:00",
                    "start": "10:00"
                }
            }
        }

    Notas:
        - Certifique-se de que a função `auth()` esteja implementada corretamente para obter o token de acesso.
        - A função `limpa_horarios()` deve ser definida para lidar com a lógica de formatação dos eventos.

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

