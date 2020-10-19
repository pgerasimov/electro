from bs4 import BeautifulSoup
import requests


# Get average temp by month
def getdata(url):
    url = url
    weather = []

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    all_data = soup.findAll('td', class_='val')

    for i in range(len(all_data)):
        if all_data[i].text is not None:
            weather.append(all_data[i].text)

    day_temp = float(weather[0].split('°')[0])
    night_temp = float(weather[1].split('°')[0])

    avg_temp = (round(day_temp + night_temp)) / 2

    return avg_temp


# Month map

month_map = {'01': 'january', '02': 'february', '03': 'march', '04': 'april', '05': 'may', '06': 'june', '07': 'july',
             '08': 'august', '09': 'september', '10': 'october', '11': 'november', '12': 'december'}
temp_map = {}

url = 'http://russia.pogoda360.ru/640764/'

for i in month_map.items():
    temp_map[i[0]] = getdata(url + i[1])


