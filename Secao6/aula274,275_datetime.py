# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pw.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

from pytz import timezone

data = datetime(2023, 4, 3)
data = datetime(2023, 4, 3, 12, 21, 21)
print(data)

data_str_data = '2023-04-03 12:21:21'
data_str_fmt = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
print(type(data))

data = datetime.now(timezone('America/Sao_Paulo'))
print(data)

data = datetime.now(timezone('Asia/Tokyo'))
print(data)

data = datetime(2023, 4, 3, 12, 21, 21, tzinfo=timezone('Asia/Tokyo'))
print(data)

data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1680536642.654921))
