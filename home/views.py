from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def home(request):
    print('home/index.html')
    return render(
        request,
        'home/index.html'
        )