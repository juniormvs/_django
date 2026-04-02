from .data import posts
from django.shortcuts import render

# Create your views here.

#Blog
def blog(request):
    print('blog')

    context = {
                # 'text': 'Olá Blog',
                'posts': posts
              }

    return render(
        request,
        'blog/index.html',
        context
        )

# Post    
def post(request, id):
    print('Post', id)

    context = {
                # 'text': 'Olá Blog',
                'posts': posts
              }

    return render(
        request,
        'blog/index.html',
        context
        )
    
# Exemplo
def exemplo(request):
    print('exemplo')

    context = {
                'title': 'Esta é uma página de exemplo -',
                'text': 'Olá Blog Exemplo -> Ainda continua azul',
              }
    
    return render(
        request,
        'blog/exemplo.html',
        context
        )
