# https://www.youtube.com/watch?v=Gon0MvppfF8&t=245s

import pyowm
import eel

owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')


@eel.expose
def get_weather(place):
    manager = owm.weather_manager()
    observation = manager.weather_at_place(place)
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    return f'В городе {place} сейчас {str(round(temp, 1))} C.'

eel.init('web')
eel.start('main.html', size=(400, 400))

