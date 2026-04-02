from typing import Any

from .data import posts
from django.shortcuts import render
from django.http import HttpRequest

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
def post(request:HttpRequest, post_id: int):
    # print('Post', id)
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    context = {
                # 'text': 'Olá Blog',
                'post': found_post,
                'title':found_post['title'] + '-',
              }

    return render(
        request,
        'blog/post.html',
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
