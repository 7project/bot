# -*- coding: utf-8 -*-
import requests
import pickle
from bs4 import BeautifulSoup as bs


headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

base_url = 'https://www.gismeteo.ru/weather-chelyabinsk-4565/'

base_url_tomorrow = 'https://www.gismeteo.ru/weather-chelyabinsk-4565/tomorrow/'

config_temp = dict.fromkeys(['value_8_00', 'value_14_00', 'value_23_00', 'weather_14_00'], '')

def gismeteo_parse(url, headers):
    session = requests.Session()
    request = session.get(url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.text, 'html.parser')
        temperature = soup.find_all('span', {'class':'unit unit_temperature_c'})
        value_8_00 = checking_str_for_number(temperature[8].text)
        value_14_00 = checking_str_for_number(temperature[10].text)
        value_23_00 = checking_str_for_number(temperature[13].text)
        # заполняем словарь ключами значение
        config_temp['value_8_00'] = value_8_00
        config_temp['value_14_00'] = value_14_00
        config_temp['value_23_00'] = value_23_00

        print('Температура в 8:00 : {}°, 14:00 : {}°, 23:00 : {}°.'.format(config_temp['value_8_00'], config_temp['value_14_00'], config_temp['value_23_00']))
        print(type(config_temp['value_14_00']))
        precipitation = soup.find_all('span', {'class':'tooltip'})
        value_14_00_preprecipitation = precipitation[4].attrs['data-text']
        print(f'Сегодня днем : {value_14_00_preprecipitation}')

        config_temp['weather_14_00'] = value_14_00_preprecipitation
        # сохраняем словарь в файл
        with open('/home/www/code/vkbot/weather/dump.dat', 'wb') as dump_out:
            pickle.dump(config_temp, dump_out)
            dump_out.close()
    else:
        print(f'Error code - {request.status_code}')


def checking_str_for_number(string):
    if string[0] == '+':
        return string[1:]
    else:
        return string


if __name__ == '__main__':
    gismeteo_parse(base_url_tomorrow, headers)