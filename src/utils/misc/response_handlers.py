from datetime import datetime, timedelta


def limpa_horarios(response):
    """
        Função que limpa a resposta do LLM de horários disponíveis para reuniões.
    """
    # Ensure response is a list and contains dictionaries
    if not isinstance(response, list):
        return {"error": "Invalid response format"}, 400

    parsed_response = []

    for meet in response:
        if not isinstance(meet, dict):
            continue  # Skip invalid entries

        # print(meet)

        parsed_response_item = {
            #'name': meet.get('subject', 'Unknown'),
            'start': meet.get('start', 'Unknown'),
            'end': meet.get('end', 'Unknown')
        }

        parsed_response.append(parsed_response_item)

    # Subtract 3 hours from all dateTime fields
    for meeting in parsed_response:
        for key in ["start", "end"]:
            original_datetime = datetime.strptime(meeting[key]["dateTime"], "%Y-%m-%dT%H:%M:%S.%f0")
            updated_datetime = original_datetime - timedelta(hours=3)
            meeting[key]["dateTime"] = updated_datetime
            meeting[key].pop("timeZone")

    # Filter out meetings on Saturdays and Sundays and adjust dateTime fields
    parsed_response = [
        meeting for meeting in parsed_response
        if meeting["start"]["dateTime"].weekday() < 5 and meeting["start"]["dateTime"] > datetime.now()
    ]

    return {
            "meetings": parsed_response,
            "working_hours": {
                        "start": "10:00",
                        "end": "18:00"
                    },
            "never_available": {
                        "start": "12:00",
                        "end": "14:00"
                    }
        }