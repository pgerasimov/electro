import requests

r = requests.get('https://api.weather.yandex.ru/v1/forecast?lat=52.886894&lon=40.509112&limit=1&hours=false&extra=false}')

print(r)
