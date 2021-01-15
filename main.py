# https://www.youtube.com/watch?v=Gon0MvppfF8&t=245s

import pyowm

city = 'Moscow, Russia'
owm = pyowm.OWM('59ff4e66ae7a38fcb9a7a637165a4172')
manager = owm.weather_manager()

observation = manager.weather_at_place(city)
weather = observation.weather

temp = weather.temperature('celsius')['temp']

print(f'В городе {city} сейчас {str(round(temp, 2))} градусов.')