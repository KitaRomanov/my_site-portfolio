import pyowm


def weather():
    city = 'Moscow, Russia'
    owm = pyowm.OWM("f54e699b269349167766a4a5226fda1e")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    return round(temp)


class WeatherMixin:
    temp = weather()

    def get_context_data(self, **kwargs):
        context = super(WeatherMixin, self).get_context_data(**kwargs)
        context['current_temp'] = self.temp
        return context
