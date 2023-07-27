from django.shortcuts import render
from djangoconvertvdoctopdf.convertor import StreamingConvertedPdf
import requests
from tools.forms import FileForm
from django import forms


def converter_currencies(request):
    response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
    currencies = response.get('rates')

    if request.method == "GET":
        context = {
            'currencies': currencies
        }
        return render(request=request, template_name='tools/currency_converter.html', context=context)

    if request.method == "POST":
        if request.POST.get('summ').isdigit():
            from_summ = float(request.POST.get('summ'))
        else:
            from_summ = ""
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        if len(str(from_summ)) > 0:
            converted = round((currencies[to_curr] / currencies[from_curr]) * float(from_summ), 2)
        else:
            converted = 'Некорректно введеное число'

        context = {
            'currencies': currencies,
            'converted': converted
        }

        return render(request=request, template_name='tools/currency_converter.html', context=context)


def conventer_to_pdf(request):
    form = FileForm(request.POST, request.FILES)

    if request.method == "GET":
        context = {
            'form': form
        }

        return render(request=request, template_name='tools/conventer_to_pdf.html', context=context)
    else:
        if form.is_valid():
            r_file = request.FILES['file']
            if r_file.name.split('.')[-1] in ('doc', 'docm', 'docx'):
                inst = StreamingConvertedPdf(r_file)
                return inst.stream_content()
            else:
                error_text = 'Выбранный файл не является файлом word. Корректные форматы "doc", "docm" и "docx"'
                context = {
                    'form': form,
                    'error_text': error_text,
                           }
                return render(request=request, template_name='tools/conventer_to_pdf.html', context=context)


