from django.urls import path, include
from tools.views import converter_currencies, conventer_to_pdf

app_name = 'tools'

urlpatterns = [
    path('converter', converter_currencies, name='converter'),
    path('converter_to_pdf', conventer_to_pdf, name='converter_to_pdf'),
]
