# -*- coding: utf-8 -*-
import pickle

def load_bump_file():
    with open('/home/www/code/vkbot/weather/dump.dat', 'rb') as dump_in:
        der = pickle.load(dump_in)
    # print('Открываю файл дампа.. 14_00 - {}.'.format(der['value_14_00']))
    weather_label = der['weather_14_00']
    value_14_00 = der['value_14_00']
    value_8_00 = der['value_8_00']
    value_23_00 = der['value_23_00']

    return weather_label, value_14_00, value_8_00, value_23_00


def output_temperature_label(temperature):
    if temperature[0] == '−':
        return f'{temperature}°'
    elif temperature[0] == '0':
        return f' {temperature}°'
    else:
        return f'+{temperature}°'


def icon_output(weather_text):
    if weather_text.lower() == 'ясно':
        return '/home/www/code/vkbot/weather/sun.png'
    elif weather_text.lower() == 'малооблачно':
        return '/home/www/code/vkbot/weather/cloudy.png'
    elif weather_text.lower() == 'переменная облачность, небольшой дождь':
        return '/home/www/code/vkbot/weather/sunny_overcast.png'
    elif weather_text.lower() == 'переменная облачность, небольшой снег':
        return '/home/www/code/vkbot/weather/snow_sun.png'
    elif weather_text.lower() == 'переменная облачность':
        return '/home/www/code/vkbot/weather/mainly_cloudy.png'
    elif weather_text.lower() == 'облачно':
        return '/home/www/code/vkbot/weather/cloudy.png'
    elif weather_text.lower() == 'облачно, небольшой дождь':
        return '/home/www/code/vkbot/weather/sunny_overcast.png'
    elif weather_text.lower() == 'облачно, дождь':
        return '/home/www/code/vkbot/weather/sunny_overcast.png'
    elif weather_text.lower() == 'облачно, замерзающий дождь':
        return '/home/www/code/vkbot/weather/other_precipitation.png'
    elif weather_text.lower() == 'пасмурно':
        return '/home/www/code/vkbot/weather/mainly_cloudy.png'
    elif weather_text.lower() == 'пасмурно, небольшой дождь':
        return '/home/www/code/vkbot/weather/rain.png'
    elif weather_text.lower() == 'пасмурно, дождь':
        return '/home/www/code/vkbot/weather/rain.png'
    elif weather_text.lower() == 'пасмурно, замерзающий дождь':
        return '/home/www/code/vkbot/weather/rain.png'
    elif weather_text.lower() == 'пасмурно, небольшой снег':
        return '/home/www/code/vkbot/weather/snow.png'
    else:
        return '/home/www/code/vkbot/weather/cloudy.png'


# weather_label, value_14_00, value_8_00, value_23_00 = load_bump_file()

in_img = '/home/www/code/vkbot/weather/fon.jpg'  # фон картинки
out_img = '/home/www/code/vkbot/weather/weather_new.png'  # файл который получаем на выходе

logo = '/home/www/code/vkbot/weather/logo.png'  # логотип
position_logo = (30, 30)  # позиция логотипа

font_size = 48  # размер шрифта описание погоды
weather_label = load_bump_file()[0]  # главный тест описание погоды
weather_text = weather_label.upper()
position_weather_text = (75, 760)  # позиция гланого текста

icon = icon_output(weather_label)  # главная иконка погоды
position_icon = (125, 260)  # позиция главной иконки

value_14_00 = load_bump_file()[1]  # дневная температура
font_size_temperature_base = 250  # размер шрифта дневной температуры
temperature_base_text = output_temperature_label(value_14_00)
position_temperature_base_text = (550, 250)  # позиция дневной температуры

value_8_00 = load_bump_file()[2]
value_23_00 = load_bump_file()[3]
font_size_morning_night = 36
temperature_morning = output_temperature_label(value_8_00)
temperature_night = output_temperature_label(value_23_00)
temperature_m_n = 'Утро ' + temperature_morning + ' // ' + 'Ночь ' + temperature_night
text_temperature_m_n = temperature_m_n.upper()
position_morning_night = (75, 900)
