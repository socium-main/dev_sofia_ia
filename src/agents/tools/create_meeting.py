import json
from src.utils.external_apis.microsoft.graph import *

def create_meeting(subject: str, start_time:str, end_time:str, attendees_emails:list, location:str = "Online", html_content =""):
    """
    Schedules a meeting using the Microsoft Graph API.

    :param subject: Title or subject of the meeting.
    :param start_time: Start date and time of the meeting (ISO 8601 format). ex: '2024-12-12T14:00:00'
    :param end_time: End date and time of the meeting (ISO 8601 format). ex: '2024-12-12T15:00:00'
    :param attendees_emails: List of emails of the attendees.
    :param location: Location of the meeting. Default: 'Online'.
    :param html_content: Texto to be show in the meeting card Default: ''.
    :return: Response from the API.
    """
    # Microsoft Graph API endpoint for creating online meetings
    url = f"https://graph.microsoft.com/v1.0/users/{conn.USER_ID[2]}/calendar/events"

    # html_content para call apresentação sofia:
    #
    #    Segue o convite para a reunião de apresentação, bom proveito! <br>
    #    Att, Sofia.

    # Replace with a function or logic to fetch your auth token
    auth_token = auth()

    # Prepare attendees list
    lista_attendees = [
            {
        "emailAddress": {
            "address": email
        },
        "type": "required"
        }
        for email in attendees_emails
    ]

    # Set headers
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    evento = {
    "subject": subject,
    "body": {
        "contentType": "HTML",
        "content": html_content
    },
    "start": {
        "dateTime": start_time, # "2024-12-12T14:00:00"
        "timeZone": "America/Sao_Paulo"
    },
    "end": {
        "dateTime": end_time, 
        "timeZone": "America/Sao_Paulo"
    },
    "location":{
        "displayName":location
    },
    "attendees": lista_attendees,
    "isOnlineMeeting": True,
    "onlineMeetingProvider": "teamsForBusiness",
    }

    response = requests.post(url, headers=headers, data=json.dumps(evento))

    # Verificar a resposta
    if response.status_code == 201:
        print('Reuniao criada com sucesso')
        return response.json()
    else:
        print(f"Erro ao criar reuniao: {response.status_code}")
        # print(response.json())
        return response.content