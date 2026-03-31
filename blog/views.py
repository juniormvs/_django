from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')

    context = {
                'text': 'Olá Blog -> Ainda continua azul'
              }

    return render(
        request,
        'blog/index.html',
        context
        )
    

def exemplo(request):
    print('exemplo')

    context = {
                'text': 'Olá Blog Exemplo -> Ainda continua azul',
                'title': 'Esta é uma página de exemplo ',
              }
    
    return render(
        request,
        'blog/exemplo.html',
        context
        )
