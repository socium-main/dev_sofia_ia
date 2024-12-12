from datetime import datetime
import pytz


def get_current_time():
    """
        Função que retorna o horário atual em UTC-3.
    """
    # Define o fuso horário para UTC-3
    utc_minus_3 = pytz.timezone("America/Sao_Paulo")

    # Obtém o horário atual no fuso horário UTC-3
    current_time_utc_minus_3 = datetime.now(utc_minus_3)

    # retorna o horário formatado
    return current_time_utc_minus_3.strftime("%d-%m-%y %H:%M:%S")

