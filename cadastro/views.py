
from django.shortcuts import render


def index(request):

    contexto = {
        'nome': 'Joca',
        'idade': 30,
    }

    return render(
        request,
        'cadastro/index.html',
        contexto
    )


def contato(request):

    contexto = dict()
    return render(
        request,
        'cadastro/contato.html',
        contexto
    )
