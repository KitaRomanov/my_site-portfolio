from django.views.generic.base import TemplateView
from django.shortcuts import render

from common.views import TitleMixin
from common.weather_time import WeatherMixin


class IndexView(TitleMixin, WeatherMixin, TemplateView):
    template_name = 'information/index.html'
    title = 'Главная страница'


class ContactView(TitleMixin, TemplateView):
    template_name = 'information/contact.html'
    title = 'Контакты'


class ProjectsView(TitleMixin, TemplateView):
    template_name = 'information/projects.html'
    title = 'Проекты'


class StackView(TitleMixin, TemplateView):
    template_name = 'information/stack.html'
    title = 'Стак технологий'



