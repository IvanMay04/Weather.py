import pyowm
city = input('Какой город вас интересует?:')
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("В городе" + city + "сейчас температура" + str(temperature) + "по Цельсию.")
print("Также,в указанном городе" + w.get_detailed_status())
