from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from cadastro.forms import ContatoForm, PessoaForm
from cadastro.models import Pessoa


def index(request):

    # Recebe todas as "Pessoas" do banco de dados
    pessoas = Pessoa.objects.all()

    # Conta o total de registros
    total = len(pessoas)

    contexto = {
        'nome': 'Joquinha',
        'pessoas': pessoas,
        'total': total
    }

    return render(
        request,
        'cadastro/index.html',
        contexto
    )


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContatoForm()
    return render(
        request,
        'cadastro/contato.html',
        {
            'form': form,
            'nome': 'Joquinha'

        }
    )


@login_required
def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()
    return render(
        request,
        'cadastro/adicionar.html',
        {
            'form': form,
            'nome': 'Joquinha'

        }
    )

@login_required
def detalhe(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    return render(request,
                  'cadastro/detalhe.html',
                  {
                      'pessoa': pessoa,
                      'nome': 'Joquinha'
                  }
                  )

@login_required
def editar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('detalhe', id=id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(request,
                  'cadastro/editar.html',
                  {
                      'form': form,
                      'pessoa': pessoa,
                      'nome': 'Joquinha'
                  }
                  )

@login_required
def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('index')
    return render(
            request,
            'cadastro/deletar.html',
            {
                      'pessoa': pessoa,
                      'nome': 'Joquinha'
            }
            )
