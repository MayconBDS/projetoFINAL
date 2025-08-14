from django.shortcuts import render

def fale_conosco(request):
    return render(request, 'contact/fale_conosco.html')
