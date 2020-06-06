# -*- coding: utf-8 -*-
# scripts create images weather
from PIL import Image, ImageDraw, ImageFont
import config_image as conf


def create_image(input_image, output_image, logo_image, position_logo, icon_weather, position_icon):
    image = Image.open(input_image)
    logo_base = Image.open(logo_image)
    icon = Image.open(icon_weather)
    width, height = image.size

    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    transparent.paste(image, (0, 0))
    transparent.paste(logo_base, position_logo, logo_base)
    transparent.paste(icon, position_icon, icon)
    transparent.save(output_image)


def add_text_image(output_image, font_size, label_text, position):
    image = Image.open(output_image)
    font = ImageFont.truetype('/home/www/code/vkbot/weather/Gilroy.otf', font_size)
    color_text = (0, 0, 0) # black
    draw = ImageDraw.Draw(image)
    draw.text(position, label_text, fill=color_text, font=font)
    image.save(output_image)


def main():
    weather_label, value_14_00, value_8_00, value_23_00 = conf.load_bump_file()
    weather_text = weather_label.upper()
    icon = conf.icon_output(weather_label)
    temperature_base_text = conf.output_temperature_label(value_14_00)

    temperature_morning = conf.output_temperature_label(value_8_00)
    temperature_night = conf.output_temperature_label(value_23_00)
    temperature_m_n = 'Утро ' + temperature_morning + ' // ' + 'Ночь ' + temperature_night
    text_temperature_m_n = temperature_m_n.upper()

    create_image(conf.in_img, conf.out_img, conf.logo, conf.position_logo, icon, conf.position_icon)
    add_text_image(conf.out_img, conf.font_size, weather_text, conf.position_weather_text)
    add_text_image(conf.out_img, conf.font_size_temperature_base, temperature_base_text, conf.position_temperature_base_text)
    add_text_image(conf.out_img, conf.font_size_morning_night, text_temperature_m_n, conf.position_morning_night)


if __name__ == '__main__':
    main()