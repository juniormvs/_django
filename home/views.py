from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def home(request):
    print('home')

    context = {
                'text': 'Olá Home -> Ainda continua azul'
              }

    return render(
        request,
        'home/index.html',
        context

        )